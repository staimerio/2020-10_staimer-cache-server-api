# Services
from retic.services.responses import success_response_service, error_response_service

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

        """Transform the data"""
        _file_data = _file_req.content

        """Return data"""
        return success_response_service(data=_file_data)
    except Exception as error:
        return error_response_service(msg=str(error))
