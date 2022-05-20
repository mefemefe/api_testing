"""
Create and send HTTP requests to the services through this module.

Classes:
    RequestManager

"""
import requests
import json

from main.utils.api_exceptions import RestError
from main.utils.common_globals import HEADERS, DEFAULT_API_URL, API_VERSION
from main.utils.meta_classes import Singleton


class RequestManager(metaclass=Singleton):
    """Module in charge of the execution of REST requests"""
    
    def __init__(self, base_url=DEFAULT_API_URL, version=API_VERSION):
        """ Construct the necessary attributes for the Request Manager. 
        
        :param base_url:  str  The URL of the API to which the requests are to be sent
        :param version:   str  The API version
        """
        self.base_url = f"{base_url}/{version}"
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def do_request(self, method, endpoint, payload=None, **kwargs):
        """Send REST request to the specified endpoint.
        
        :param method:    str   Request method name such as GET, POST, PUT, DELETE, PATCH
        :param endpoint:  str   Endpoint of service to which the request will be sent
        :param payload:   dict  Data or payload send along with the REST request
        :param kwargs:    dict  Data that will be considered as query parameters
        :return: Tuple that contains the status code and the response.
        """
        endpoint_url = f"{self.base_url}/{endpoint}"

        if method in ['POST', 'PUT']:
            response = self.session.request(method, endpoint_url, data=json.dumps(payload), params=kwargs)
        else:
            response = self.session.request(method, endpoint_url, params=kwargs)

        if not response.ok:
            raise RestError(response.status_code, endpoint_url, response)

        return response.status_code, response.json()

    def get_request(self, endpoint, **kwargs):
        """Method to send GET requests to the specified endpoint
        
        :param endpoint:  str   Endpoint of service to which the request will be sent
        :param kwargs:    dict  Data that will be considered as query parameters
        :return: Tuple that contains the status code and the response.
        """
        return self.do_request('GET', endpoint, **kwargs)

    def post_request(self, endpoint, payload=None, **kwargs):
        """Method to send POST requests to the specified endpoint
        
        :param endpoint:  str   Endpoint of service to which the request will be sent
        :param payload:   dict  Data or payload send along with the REST request
        :param kwargs:    dict  Data that will be considered as query parameters
        :return: Tuple that contains the status code and the response.
        """
        return self.do_request('POST', endpoint, payload=payload, **kwargs)

    def put_request(self, endpoint, payload=None, **kwargs):
        """Method to send PUT requests to the specified endpoint
        
        :param endpoint:  str   Endpoint of service to which the request will be sent
        :param payload:   dict  Data or payload send along with the REST request
        :param kwargs:    dict  Data that will be considered as query parameters
        :return: Tuple that contains the status code and the response.
        """
        return self.do_request('PUT', endpoint, payload=payload, **kwargs)

    def delete_request(self, endpoint):
        """Method to send DELETE requests to the specified endpoint
        
        :param endpoint:  str   Endpoint of service to which the request will be sent
        :return: Tuple that contains the status code and the response.
        """
        return self.do_request('DELETE', endpoint)


if __name__ == '__main__':
    # This section helps to test the module, make sure the env variable PYTHONPATH exists 
    # to be able to execute only this module.
    # PYTHONPATH=<Full path to bootcamp04-trello folder>
    request = RequestManager()
    status_code, response = request.get_request('members/me/boards?fields=name')
    print(status_code)
    print(response)
