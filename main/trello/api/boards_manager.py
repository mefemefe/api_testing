"""
Module to manage Trello Boards through the API

Classes:
    BoardsManager
"""
from main.trello.api.rest_base_manager import RESTBaseManager

# endpoint formats
BOARDS = 'boards'


class BoardsManager(RESTBaseManager):
    """Class which can be used to manage Trello Boards through the API"""

    def __init__(self, method=None):
        """ Construct the necessary attributes for the BoardsManager

        :param method: obj  RequestManager object which is used to handle the API requests
        """
        super().__init__(method)

    def get_board(self, id_name, fields='all', **kwargs):
        """ Get a Board data by its ID

        :param id_name: str   ID or name of the Board
        :param fields:  str   All or a comma-separated list of board fields
        :param kwargs:  dict  Data that will be considered as query parameters
        :return: Tuple that contains the status code and the response.
        """
        endpoint = f"{BOARDS}/{id_name}"

        # join dicts, add/replace the 'fields' query param if it was passed
        if isinstance(fields, str):
            kwargs = {**kwargs, 'fields': fields}

        status_code, response = self.method.get_request(endpoint, **kwargs)

        return status_code, response

    def create_board(self, name, description=None, id_organization=None, **kwargs):
        """ Create a new Board

        :param name:             str   Name for the new Board
        :param description:      str   A description for the new Board
        :param id_organization:  str   ID of the organization the new board will beong to
        :param kwargs:           dict  Data that will be considered as part of the payload
        :return: Tuple that contains the status code and the response.
        """
        endpoint = f"{BOARDS}"

        payload = {
            "name": name,
            "desc": description,
            "idOrganization": id_organization,
        }
        # join dicts, add/replace the 'fields' query param if it was passed
        if kwargs:
            payload = {**kwargs, **payload}

        status_code, response = self.method.post_request(endpoint, payload=payload)

        return status_code, response

    def copy_board(self, name, id_board):
        """ Create a new Board based on an existing Board

        :param name:      str   Name for the new Board        
        :param id_board:  str   Id of the source board from which the same information will be copied
        :return: Tuple that contains the status code and the response.
        """
        kwargs = {
            "idBoardSource": id_board
        }
        return self.create_board(name, **kwargs)

    def delete_board(self, id_name):
        """ Delete a Board by its ID

        :param id_name:  str   ID of the board that will be deleted
        :return: Tuple that contains the status code and the response.
        """
        endpoint = f"{BOARDS}/{id_name}"
        return self.method.delete_request(endpoint)
