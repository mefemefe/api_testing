"""
Module to manage Trello Boards through the API

Classes:
    MembersManager

"""
from main.trello.api.rest_base_manager import RESTBaseManager

MEMBERS = 'members'
MEMBERS_BOARDS = "members/{id}/boards"

class MembersManager(RESTBaseManager):    
    """Class which can be used to manage Trello Members through the API"""

    def __init__(self, method=None):
        """ Construct the necessary attributes for the BoardsManager

        :param method: obj  RequestManager object which is used to handle the API requests
        """
        super().__init__(method)

    def get_boards(self, id_name='me', fields='all', **kwargs):
        """ Get Boards that Member belongs to

        :param id_name: str   ID or name of the Member
        :param fields:  str   All or a comma-separated list of board fields
        :param kwargs:  dict  Data that will be considered as query parameters
        :return: Tuple that contains the status code and the response.
        """
        endpoint = MEMBERS_BOARDS.format(id=id_name)

        # join dicts, add/replace the 'fields' query param if it was passed
        if isinstance(fields, str):            
            kwargs = {**kwargs, 'fields': fields}

        status_code, response = self.method.get_request(endpoint, **kwargs)

        return status_code, response

    def get_member(self, id_name='me', fields='all', **kwargs):
        """ Get a Member data by its ID

        :param id_name: str   ID or name of the Member
        :param fields:  str   All or a comma-separated list of board fields
        :param kwargs:  dict  Data that will be considered as query parameters
        :return: Tuple that contains the status code and the response.
        """
        endpoint = f"{MEMBERS}/{id_name}"
                
        # join dicts, add/replace the 'fields' query param if it was passed
        if isinstance(fields, str):
            kwargs = {**kwargs, 'fields': fields}
        
        status_code, response = self.method.get_request(endpoint, **kwargs)
    
        return status_code, response


if __name__ == '__main__':
    # This section helps to test the module, make sure the env variable PYTHONPATH exists 
    # to be able to execute only this module.
    # PYTHONPATH=<Full path to bootcamp04-trello folder>
    member = MembersManager()
    print(member.get_member(fields="aaId,initials", tokens='all'))
