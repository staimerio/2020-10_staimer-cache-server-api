# Retic
from retic import env, App as app

# Services
from retic.services.responses import success_response_service, error_response_service
from retic.services.general.json import jsonify, parse

# Requests
import requests

# Constants
URL_SENDFILES_PHOTOS = app.apps['backend']['sendfiles']['base_url'] + \
    app.apps['backend']['sendfiles']['photos']
URL_SENDFILES_PHOTOS_FOLDER = app.apps['backend']['sendfiles']['base_url'] + \
    app.apps['backend']['sendfiles']['photos_folder']


def get_from_params(album, filename):
    """Get a file from a url

    :param source: URL that will be use to get the file
    """

    try:
        """Prepare the payload"""
        _url = "{0}/{1}/{2}".format(
            URL_SENDFILES_PHOTOS,
            album,
            filename
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
            _file_req.headers['custom_headers']) or _file_req.headers
        """Define the response object"""
        _response = {
            u'body': _file_req.content,
            u'headers': _response_headers,
        }

        """Return data"""
        return success_response_service(data=_response)
    except Exception as error:
        return error_response_service(msg=str(error))


def get_from_folder_params(album, code, filename):
    """Get a file from a url

    :param source: URL that will be use to get the file
    """

    try:
        """Prepare the payload"""
        _url = "{0}/{1}/{2}/{3}".format(
            URL_SENDFILES_PHOTOS_FOLDER,
            album,
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
            _file_req.headers['custom_headers']) or _file_req.headers
        """Define the response object"""
        _response = {
            u'body': _file_req.content,
            u'headers': _response_headers,
        }

        """Return data"""
        return success_response_service(data=_response)
    except Exception as error:
        return error_response_service(msg=str(error))
