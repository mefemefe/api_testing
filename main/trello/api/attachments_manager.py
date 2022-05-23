from main.trello.api.rest_base_manager import RESTBaseManager
from main.utils.common_globals import HEADERS, DEFAULT_API_URL, API_VERSION


class AttachmentsManager(RESTBaseManager):

    def __init__(self, method=None):
        super().__init__(method)

    def get_all_attachments(self, card_id):
        """ Get all attachments of a card by its ID,
        :param card_id: str   ID of the card
        :return: Tuple that contains the status code and the response."""

        endpoint = f'cards/{card_id}/attachments'
        status_code, response = self.method.get_request(endpoint)

        return status_code, response

    def get_attachment(self, card_id ,attachment_id):
        """ Get a specific attachment from a specific card,
        :param card_id:       str    ID of the card
        :param attachment_id: str    ID of the attachment
        :return:              Tuple  that contains the status code and the response."""

        endpoint = f'cards/{card_id}/attachments/{attachment_id}'
        status_code, response = self.method.get_request(endpoint)

        return status_code, response

    def create_attachment_from_url(self, url, card_id, name, set_cover=False):
        """ Create a new attachment from an URL,
        :param card_id:       str    ID of the card
        :param name:          str    Name of the attachment
        :param set_cover:     bool   If True, the attachment will be set as the cover of the card
        :param url:           str    URL of the attachment
        :return:              Tuple  that contains the status code and the response."""

        endpoint = f'cards/{card_id}/attachments'
        payload = {
            "url": url, 
            "name": name,
            "setCover": set_cover
        }
        status_code, response = self.method.post_request(endpoint, payload=payload)

        return status_code, response

    def create_attachment_from_file(self, path, card_id, name, set_cover=False):
        """ Create a new attachment from a file,
        :param card_id:       str    ID of the card
        :param name:          str    Name of the attachment
        :param set_cover:     bool   If True, the attachment will be set as the cover of the card
        :param path:          str    Path of the file
        :return:              Tuple  that contains the status code and the response."""
        
        endpoint = f'{DEFAULT_API_URL}/{API_VERSION}/cards/{card_id}/attachments'

        post_files = {
        "file": open(path, "rb"),
        }
        payload = {
            "name": name,
            "setCover": set_cover
        }

        # 'Content-Type' header is temporarily removed in order to upload a file, then it's restored.
        self.method.session.headers.pop('Content-Type')
        response = self.method.session.post(endpoint, data=payload, files=post_files)
        self.method.session.headers.update(HEADERS)

        return response

    def delete_attachment(self, card_id, attachment_id):
        """ Delete a specific attachment from a specific card,
        :param card_id:       str    ID of the card
        :param attachment_id: str    ID of the attachment
        :return:              Tuple  that contains the status code and the response."""

        endpoint = f'cards/{card_id}/attachments/{attachment_id}'
        status_code, response = self.method.delete_request(endpoint)

        return status_code, response
