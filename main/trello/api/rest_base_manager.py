"""
Module to manage Trello Boards through the API

Classes:
    RESTBaseManager

"""
from main.core.rest.request_manager import RequestManager


class RESTBaseManager:
    """Base Class which can be used to manage Trello objects through the API"""
    
    def __init__(self, request_method=None):
        """ Construct the necessary attributes for the manager
        
        :param method: obj  RequestManager object which is used to handle the API requests
        """
        # Use the passed RequestManager object
        if isinstance(request_method, RequestManager):
            self.method = request_method
        else:
            self.method = RequestManager()
