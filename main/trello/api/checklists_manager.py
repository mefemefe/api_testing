from main.trello.api.rest_base_manager import RESTBaseManager

class ChecklistsManager(RESTBaseManager):

    def __init__(self, method=None):
        super().__init__(method)

    def get_checklists(self, card_id, check_items='all', checkitem_fields='all', fields='all'):
        """ Get all checklists of a card by its ID,
        :param card_id:          str   ID of the card
        :param check_items:      str   Whether to include checkitems or not: {all, none}
        :param checkitem_fields: str   Fields to return for checkitems: {all, name, nameData, pos, state, type}
        :param fields:           str   Fields to return for checklists: {all, id, data, date, idMemberCreator, type}
        :return:                 Tuple that contains the status code and the response."""

        endpoint = f'cards/{card_id}/checklists'
        params = {
            'checkItems': check_items,
            'checkItem_fields': checkitem_fields,
            'fields': fields
        }
        status_code, response = self.method.get_request(endpoint, **params)

        return status_code, response

    def get_checklist(self, checklist_id, check_items='all', checkitem_fields='all', fields='all'):
        """ Get a specific checklist by its ID,
        :param checklist_id:     str   ID of the checklist
        :param check_items:      str   Whether to include checkitems or not: {all, none}
        :param checkitem_fields: str   Fields to return for checkitems: {all, name, nameData, pos, state, type}
        :param fields:           str   Fields to return for checklists: {all, id, data, date, idMemberCreator, type}
        :return:             Tuple that contains the status code and the response."""

        endpoint = f'checklists/{checklist_id}'
        params = {
            "checkItems": check_items,
            "checkItem_fields": checkitem_fields,
            "fields": fields
        }
        status_code, response = self.method.get_request(endpoint, **params)

        return status_code, response

    def create_checklist(self, card_id, name, pos="bottom", id_source=None):
        """ Create a new checklist for a specific card,
        :param card_id: str   ID of the card
        :param name:    str   Name of the checklist
        :return:        Tuple that contains the status code and the response."""

        endpoint = f'checklists'
        payload = {
            "idCard": card_id,
            "name": name,
            "pos": pos
        }
        if id_source:
            payload["idSource"] = id_source
        
        status_code, response = self.method.post_request(endpoint, payload=payload)

        return status_code, response

    def update_checklist(self, checklist_id, name=None, pos=None):
        """ Update a specific checklist,
        :param checklist_id: str   ID of the checklist
        :param name:         str   Name of the checklist
        :param pos:          str   Position of the checklist
        :return:             Tuple that contains the status code and the response."""

        endpoint = f'checklists/{checklist_id}'
        payload = {}
        if name:
            payload["name"] = name
        if pos:
            payload["pos"] = pos
        
        status_code, response = self.method.put_request(endpoint, payload=payload)

        return status_code, response

    def delete_checklist(self, checklist_id):
        """ Delete a specific checklist,
        :param checklist_id:  str   ID of the checklist
        :return:             Tuple that contains the status code and the response."""

        endpoint = f'checklists/{checklist_id}'
        status_code, response = self.method.delete_request(endpoint)

        return status_code, response

    def get_all_checkitems(self, checklist_id):
        """ Get all checkitems of a checklist by its ID,
        :param checklist_id: str   ID of the checklist
        :return:             Tuple that contains the status code and the response."""

        endpoint = f'checklists/{checklist_id}/checkItems'
        status_code, response = self.method.get_request(endpoint)

        return status_code, response

    def get_checkitem(self, checklist_id, checkitem_id):
        """ Get a specific checkitem by its ID,
        :param checklist_id: str   ID of the checklist
        :param checkitem_id: str   ID of the checkitem
        :return:             Tuple that contains the status code and the response."""

        endpoint = f'checklists/{checklist_id}/checkItems/{checkitem_id}'
        status_code, response = self.method.get_request(endpoint)

        return status_code, response

    def create_checkitem(self, checklist_id, name, pos="bottom", checked=False):
        """ Create a new checkitem for a specific checklist,
        :param checklist_id: str   ID of the checklist
        :param name:         str   Name of the checkitem
        :param pos:          str   Position of the item in the list: {top, bottom, or a positive number}
        :param checked:      bool  Whether the checkitem is checked or not
        :return:             Tuple that contains the status code and the response."""

        endpoint = f'checklists/{checklist_id}/checkItems'
        payload = {
            "name": name,
            "pos": pos,
            "checked": checked
        }
        status_code, response = self.method.post_request(endpoint, payload=payload)

        return status_code, response

    def update_checkitem(self, card_id, checkitem_id, name=None, pos=None, state=None):
        """ Update a specific checkitem,
        :param card_id:      str   ID of the card
        :param checkitem_id: str   ID of the checkitem
        :param name:         str   Name of the checkitem
        :param pos:          str   Position of the item in the list: {top, bottom, or a positive number}
        :param state:        str   Whether the checkitem is checked or not: {complete, incomplete}
        :return:             Tuple that contains the status code and the response."""

        endpoint = f'cards/{card_id}/checkItem/{checkitem_id}'
        payload = {}
        if name:
            payload["name"] = name
        if pos:
            payload["pos"] = pos
        if state:
            payload["state"] = state
        
        status_code, response = self.method.put_request(endpoint, payload=payload)

        return status_code, response

    def delete_checkitem_card(self, card_id, checkitem_id):
        """ Delete a specific checkitem,
        :param card_id:      str   ID of the card
        :param checkitem_id: str   ID of the checkitem
        :return:             Tuple that contains the status code and the response."""

        endpoint = f'cards/{card_id}/checkItem/{checkitem_id}'
        status_code, response = self.method.delete_request(endpoint)

        return status_code, response

    def delete_checkitem_checklist(self, checklist_id, checkitem_id):
        """ Delete a specific checkitem,
        :param checklist_id: str   ID of the checklist
        :param checkitem_id: str   ID of the checkitem
        :return:             Tuple that contains the status code and the response."""

        endpoint = f'checklists/{checklist_id}/checkItems/{checkitem_id}'
        status_code, response = self.method.delete_request(endpoint)

        return status_code, response