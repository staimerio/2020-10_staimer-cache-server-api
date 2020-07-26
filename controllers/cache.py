# Retic
from retic import Request, Response, Next

# Services
from retic.services.validations import validate_obligate_fields
from retic.services.responses import error_response_service, success_response_service
import services.cache.cache as cache
import services.files.files as files


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
        """Response a file data to client"""
        return res.set_status(200).send(_file_cache['data'])

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

    """Response to client the file"""
    res.set_status(200).send(_file_req['data'])


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
