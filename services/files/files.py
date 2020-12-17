# Services
from retic.services.responses import success_response_service, error_response_service
from retic.services.general.json import jsonify, parse

# Requests
import requests


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
