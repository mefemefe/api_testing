from behave import fixture
from main.core.rest.request_manager import RequestManager
from main.trello.api.attachments_manager import AttachmentsManager
from main.trello.api.checklists_manager import ChecklistsManager
from main.trello.api.boards_manager import BoardsManager
from main.trello.api.members_manager import MembersManager

def before_all(context):
    context.request_manager = RequestManager()
    context.boards_manager = BoardsManager(context.request_manager)
    context.members_manager = MembersManager(context.request_manager)
    context.checklists_manager = ChecklistsManager(context.request_manager)
    context.attachments_manager = AttachmentsManager(context.request_manager)
    _, context.board = context.request_manager.post_request('boards/', payload={'name': 'Behave board'})
    _, context.lists = context.request_manager.get_request(f"boards/{context.board['id']}/lists")
    context.list = context.lists[0]

def after_all(context):
    context.request_manager.delete_request('boards/' + context.board['id'])