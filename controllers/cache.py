# Retic
from retic import Request, Response, Next

# Services
from retic.services.validations import validate_obligate_fields
from retic.services.responses import error_response_service, success_response_service
from services.cache import cache
from services.files import files, photos


def get_by_id(req: Request, res: Response):
    """Get a file from his Id"""

    """Check that all params are valid"""
    _validate = validate_obligate_fields({
        u'source': req.headers['source'] if "source" in req.headers else None,
    })

    """Si existen problemas, retornar un mensaje de error"""
    if _validate["valid"] is False:
        return res.bad_request(
            error_response_service(
                "The header {} is necesary.".format(_validate["error"])
            )
        )

    """Find file in the cache storage"""
    _file_cache = cache.get_by_id_cache(req.param('file'))

    """If it's exists, response to client"""
    if _file_cache['valid']:
        _headers = {**_file_cache['data']['headers']}
        """Response a file data to client"""
        res.set_headers(_headers)
        return res.set_status(200).send(_file_cache['data']['body'])

    """If it's not exists, get from the source main server"""
    _file_req = files.get_from_source(
        req.headers['source']
    )

    """Check if the file exists"""
    if not _file_req['valid']:
        """If it isn't exists, response to client an error"""
        return res.not_found(_file_req)

    """Save file in the cache storage"""
    cache.save_file_cache(
        req.param('file'),
        _file_req['data']
    )

    _headers = {**_file_req['data']['headers']}
    res.set_headers(_headers)
    _binary = _file_req['data']['body']
    """Response to client the file"""
    res.set_status(200).send(_binary)


def get_photos_by_id(req: Request, res: Response):
    """Find file in the cache storage"""
    _cahe_filename = req.param("album") + req.param("filename")

    _file_cache = cache.get_by_id_cache(_cahe_filename)

    """If it's exists, response to client"""
    if _file_cache['valid']:
        _headers = {**_file_cache['data']['headers']}
        """Response a file data to client"""
        res.set_headers(_headers)
        return res.set_status(200).send(_file_cache['data']['body'])

    """If it's not exists, get from the source main server"""
    _file_req = photos.get_from_params(
        req.param("album"), req.param("filename")
    )

    """Check if the file exists"""
    if not _file_req['valid']:
        """If it isn't exists, response to client an error"""
        return res.not_found(_file_req)

    """Save file in the cache storage"""
    cache.save_file_cache(
        _cahe_filename,
        _file_req['data']
    )

    _headers = _file_req['data']['headers']
    res.set_headers(_headers)
    _binary = _file_req['data']['body']
    """Response to client the file"""
    res.set_status(200).send(_binary)


def get_photos_folder_by_id(req: Request, res: Response):
    """Find file in the cache storage"""
    _cahe_filename = req.param(
        "album") + req.param("code") + req.param("filename")

    _file_cache = cache.get_by_id_cache(_cahe_filename)

    """If it's exists, response to client"""
    if _file_cache['valid']:
        _headers = {**_file_cache['data']['headers']}
        """Response a file data to client"""
        res.set_headers(_headers)
        return res.set_status(200).send(_file_cache['data']['body'])

    """If it's not exists, get from the source main server"""
    _file_req = photos.get_from_folder_params(
        req.param("album"), req.param("code"), req.param("filename")
    )

    """Check if the file exists"""
    if not _file_req['valid']:
        """If it isn't exists, response to client an error"""
        return res.not_found(_file_req)

    """Save file in the cache storage"""
    cache.save_file_cache(
        _cahe_filename,
        _file_req['data']
    )

    _headers = _file_req['data']['headers']
    res.set_headers(_headers)
    _binary = _file_req['data']['body']
    """Response to client the file"""
    res.set_status(200).send(_binary)


def get_media_by_id(req: Request, res: Response):
    """Get a file from his Id"""

    """Find file in the cache storage"""
    _file_cache = cache.get_by_id_cache(req.param('file'))

    """If it's exists, response to client"""
    if _file_cache['valid']:
        _headers = {**_file_cache['data']['headers']}
        """Response a file data to client"""
        res.set_headers(_headers)
        return res.set_status(200).send(_file_cache['data']['body'])

    """If it's not exists, get from the source main server"""
    _file_req = files.get_from_code(
        req.param('file')
    )

    """Check if the file exists"""
    if not _file_req['valid']:
        """If it isn't exists, response to client an error"""
        return res.not_found(_file_req)

    """Save file in the cache storage"""
    cache.save_file_cache(
        req.param('file'),
        _file_req['data']
    )

    _headers = {**_file_req['data']['headers']}
    res.set_headers(_headers)
    _binary = _file_req['data']['body']
    """Response to client the file"""
    res.set_status(200).send(_binary)


def get_files_folder_by_id(req: Request, res: Response):
    """Find file in the cache storage"""
    _cahe_filename = req.param(
        "folder") + req.param("code") + req.param("filename")

    _file_cache = cache.get_by_id_cache(_cahe_filename)

    """If it's exists, response to client"""
    if _file_cache['valid']:
        _headers = {**_file_cache['data']['headers']}
        """Response a file data to client"""
        res.set_headers(_headers)
        return res.set_status(200).send(_file_cache['data']['body'])

    """If it's not exists, get from the source main server"""
    _file_req = files.get_from_folder_params(
        req.param("folder"), req.param("code"), req.param("filename")
    )

    """Check if the file exists"""
    if not _file_req['valid']:
        """If it isn't exists, response to client an error"""
        return res.not_found(_file_req)

    """Save file in the cache storage"""
    cache.save_file_cache(
        _cahe_filename,
        _file_req['data']
    )

    _headers = _file_req['data']['headers']
    res.set_headers({**_headers})
    _binary = _file_req['data']['body']
    """Response to client the file"""
    res.set_status(200).send(_binary)


def clean_cache_files(req: Request, res: Response):
    """Delete all cache for files"""

    """Delete all files cache"""
    _deleted_cache = cache.clean_cache_files()

    """Check if it has any problem"""
    if not _deleted_cache['valid']:
        res.bad_request(_deleted_cache)
    else:
        """Response to client"""
        res.ok(
            success_response_service(
                msg="Cache deleted."
            )
        )


def get_stream_by_code(req: Request, res: Response):
    """Get a file from his Id"""

    """Find file in the cache storage"""
    _file_exists = cache.get_by_id_cache(
        req.param('file'), has_headers=False, extension='.mp4')

    """If it's exists, response to client"""
    if _file_exists['valid']:
        return res.redirect(_file_exists['data']['url'])

    """If it's not exists, get from the source main server"""
    _file_req = files.get_from_code(
        req.param('file')
    )

    """Check if the file exists"""
    if not _file_req['valid']:
        """If it isn't exists, response to client an error"""
        return res.not_found(_file_req)

    """Save file in the cache storage"""
    cache.save_file_cache(
        req.param('file'),
        _file_req['data'],
        has_headers=False, extension='.mp4'
    )

    return res.redirect(_file_req['data']['url'])


def download_stream_by_code(req: Request, res: Response):
    """Get a file from his Id"""

    """Find file in the cache storage"""
    _file_exists = cache.get_by_id_cache(
        req.param('file'), has_headers=False, extension='.mp4')

    """If it's exists, response to client"""
    if _file_exists['valid']:
        _data_response = {
            'url': _file_exists['data']['url']
        }
        return res.ok(_data_response)

    """If it's not exists, get from the source main server"""
    _file_req = files.get_from_code(
        req.param('file'),
        extension='.mp4'
    )

    """Check if the file exists"""
    if not _file_req['valid']:
        """If it isn't exists, response to client an error"""
        return res.not_found(_file_req)

    """Save file in the cache storage"""
    cache.save_file_cache(
        req.param('file'),
        _file_req['data'],
        has_headers=False, extension='.mp4'
    )

    _data_response = {
        'url': _file_req['data']['url']
    }
    return res.ok(_data_response)
