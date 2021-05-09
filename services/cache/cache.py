"""Services for the Cache controller"""

# Logging
import logging

# Retic
from retic import env, App as app

# Services
from retic.services.responses import success_response_service, error_response_service
from retic.services.general.json import parse, jsonify

# Utils
from services.general.general import get_content_from_file, save_content_in_file
from services.general.general import isfile, rmtree, mkdir, isdir

# Constants
CACHE_FOLDER_PATH = app.config.get('CACHE_FOLDER_PATH')
CACHE_BASE_PATH = app.config.get('CACHE_BASE_PATH')


def get_by_id_cache(file, has_headers=True, extension=''):
    """Find a file on cache storage

    :param file: Id of the file, it's the name in the cache storage
    """
    try:
        """Prepara all parameters"""
        _filepath = "{0}/{1}{2}".format(CACHE_FOLDER_PATH, file, extension)
        if has_headers:
            _filepath_headers = "{0}-headers".format(_filepath)

        """Check if the file exists"""
        _exists = isfile(_filepath)

        """If it is'nt exists, return a error"""
        #logging.warning('*****************************************')
        #logging.warning('_exists')
        #logging.warning(_exists)
        if not _exists:
            return error_response_service(msg='Not found.')

        """If it exists do the following"""
        """Open file"""
        _bfile = get_content_from_file(_filepath, 'rb')
        if has_headers:
            _headers = get_content_from_file(_filepath_headers, 'r')
            _headers_json = parse(_headers)

        """If it exists do the following"""
        _url = "{0}/{1}{2}".format(CACHE_BASE_PATH, file, extension)

        """Define response"""
        _response = {
            u'body': _bfile,
            u'headers': _headers_json if has_headers else {},
            u'exists': _exists,
            u'url': _url,
        }
        """Return the file"""
        return success_response_service(
            data=_response)
    except Exception as error:
        return error_response_service(msg=str(error))


def save_file_cache(file, response, has_headers=True, extension=''):
    """Save a file in cache storage

    :param filepath: Path of the file to write information.
    :param bfile: File to save
    """
    """Prepara all parameters"""
    _filepath = "{0}/{1}{2}".format(CACHE_FOLDER_PATH, file, extension)
    if has_headers:
        _filepath_headers = "{0}-headers".format(_filepath)
    #logging.warning('*****************************************')
    #logging.warning('_filepath')
    #logging.warning(_filepath)

    """Check if the file exists"""
    _exists = isdir(CACHE_FOLDER_PATH)

    """If it is'nt exists, return a error"""
    #logging.warning('*****************************************')
    #logging.warning('_exists')
    #logging.warning(_exists)
    if _exists:
        """Save file"""
        save_content_in_file(_filepath, response['body'], mode='wb')
        if has_headers:
            save_content_in_file(_filepath_headers, jsonify(
                response['headers']
            ), mode='w')


def clean_cache_files():
    """Delete the files cache folder"""
    try:
        """Check if the file exists"""
        _exists = isdir(CACHE_FOLDER_PATH)

        """If it is'nt exists, return a error"""
        if not _exists:
            raise Exception("Bad request.")

        """Delete the cache folder for files"""
        rmtree(CACHE_FOLDER_PATH)

        """Create the cache folder for files"""
        mkdir(CACHE_FOLDER_PATH)

        """Response to request"""
        return success_response_service(
            msg="Files deleted."
        )
    except Exception as err:
        return error_response_service(
            msg=str(err)
        )
