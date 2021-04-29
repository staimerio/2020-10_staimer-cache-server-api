# Retic
from retic import env, App as app

# Services
from retic.services.responses import success_response_service, error_response_service
from retic.services.general.json import jsonify, parse

# Requests
import requests

# contants
URL_SENDFILES_FILES_FOLDER = app.apps['backend']['sendfiles']['base_url'] + \
    app.apps['backend']['sendfiles']['files_folder']
URL_SENDFILES_DOWNLOADS_FILES = app.apps['backend']['sendfiles']['base_url'] + \
    app.apps['backend']['sendfiles']['downloads_files']
CACHE_FOLDER_PATH = app.config.get('CACHE_FOLDER_PATH')
CACHE_BASE_PATH = app.config.get('CACHE_BASE_PATH')


def get_from_source(source):
    """Get a file from a url

    :param source: URL that will be use to get the file
    """

    try:
        """Prepare the payload"""
        _url = source

        """Fetch file from the URL"""
        _file_req = requests.get(
            _url
        )

        """Check if the response is valid"""
        if _file_req.status_code != 200:
            """Return error if the response is invalid"""
            return _file_req.json()

        _response_headers = parse(
            _file_req.headers['custom_headers']) if 'custom_headers' in _file_req.headers else _file_req.headers
        """Define the response object"""
        _response = {
            u'body': _file_req.content,
            u'headers': _response_headers,
        }

        """Return data"""
        return success_response_service(data=_response)
    except Exception as error:
        return error_response_service(msg=str(error))


def get_from_folder_params(folder, code, filename):
    """Get a file from a url

    :param source: URL that will be use to get the file
    """

    try:
        """Prepare the payload"""
        _url = "{0}/{1}/{2}/{3}".format(
            URL_SENDFILES_FILES_FOLDER,
            folder,
            code,
            filename,
        )

        """Fetch file from the URL"""
        _file_req = requests.get(
            _url
        )

        """Check if the response is valid"""
        if _file_req.status_code != 200:
            """Return error if the response is invalid"""
            return _file_req.json()

        _response_headers = parse(
            _file_req.headers['custom_headers']) if 'custom_headers' in _file_req.headers else _file_req.headers
        """Define the response object"""
        _response = {
            u'body': _file_req.content,
            u'headers': _response_headers,
        }

        """Return data"""
        return success_response_service(data=_response)
    except Exception as error:
        return error_response_service(msg=str(error))


def get_from_code(code, extension):
    """Get a file from a url

    :param source: URL that will be use to get the file
    """

    try:
        """Prepare the payload"""
        _url = "{0}/{1}".format(
            URL_SENDFILES_DOWNLOADS_FILES,
            code,
        )

        """Fetch file from the URL"""
        _file_req = requests.get(
            _url
        )

        """Check if the response is valid"""
        if _file_req.status_code != 200:
            """Return error if the response is invalid"""
            return _file_req.json()

        _response_headers = parse(
            _file_req.headers['custom_headers']) if 'custom_headers' in _file_req.headers else _file_req.headers
            
        _url_file = "{0}/{1}{2}".format(CACHE_BASE_PATH, code, extension)
        """Define the response object"""
        _response = {
            u'body': _file_req.content,
            u'headers': _response_headers,
            u'url': _url_file,
        }

        """Return data"""
        return success_response_service(data=_response)
    except Exception as error:
        return error_response_service(msg=str(error))
