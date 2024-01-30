import requests
import time

def _jsonResponse(func: callable) -> dict:
    def jsonResponse(*args, **kwargs):
        raw = func(*args, **kwargs)
        return raw.json()

    return jsonResponse


def _retryableRequest(func: callable) -> requests.Response:
    def retryableRequest(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.status_code == 429:
            time.sleep(2)
            return retryableRequest(*args, **kwargs)
        else:
            return response
        
    return retryableRequest


def _throwableRequest(func: callable) -> requests.Response:
    def throwableRequest(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise e
        
    return throwableRequest


class HTTPRequests:
    def __init__(self, baseURL: str) -> None:
        """
        The constructor for the `HTTPRequests` class.
        It takes a `baseURL` parameter that represents the base URL of a website or API.
        
        Args:
            baseURL (str): The base URL of a website or API.
        """
        self.baseURL = baseURL

    @_jsonResponse
    @_retryableRequest
    @_throwableRequest
    def get(self, url: str) -> requests.Response:
        """
        The function `get` sends a GET request to a specified URL and returns the response.
        
        Args:
            url (str): The `url` parameter is a string that represents the specific endpoint or path of the
            API that you want to make a GET request to

        Returns:
            requests.Response: a `requests.Response` object.
        """
        return requests.get(f'{self.baseURL}{url}')