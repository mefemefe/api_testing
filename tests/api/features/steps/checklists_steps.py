import re
from behave import given, when, then, step
from main.trello.api.checklists_manager import ChecklistsManager
from main.core.rest.request_manager import RequestManager
from main.utils.api_exceptions import RestError

request_manager = RequestManager()
checklist_manager = ChecklistsManager()

@given('I created a checklist on a new card')
def step_impl(context):
    _, card = request_manager.post_request('cards', payload={'name': 'New card', 'idList': "627ee9268cea2a5a877b8b40"})
    context.card = card
    _, checklist = checklist_manager.create_checklist(context.card['id'], 'New checklist')
    context.checklist = checklist

@when('I send a "{method}" request to "{endpoint}"')
def step_impl(context, method, endpoint):
    replacements = re.findall(r'\{(.*?)\}', endpoint) 
    for replacement in replacements:
        endpoint = endpoint.replace("{" + replacement + "}", getattr(context, replacement)['id'])
    payload = {}
    if context.table:
        for row in context.table:
            key, value = row['Key'], row['Value']
            if "{id}" in value:
                value = getattr(context, value.split(':')[1])['id']
            payload[key] = value
    context.status_code, context.response = request_manager.do_request(method, endpoint, payload)
    
@then('I receive a list with at least one checklist')
def step_impl(context):
    assert len(context.response) > 0, 'No checklists were found'

@step('the status code is "{status_code}"')
def step_impl(context, status_code):
    assert context.status_code == int(status_code), 'Status code does not match'

@step('I can delete the card')
def step_impl(context):
    delete_status, _ = request_manager.delete_request('cards/' + context.card['id'])
    assert delete_status == 200, 'Card was not deleted'

@then('I receive a response with the "{item}" id')
def step_impl(context, item):
    item_id = getattr(context, item)['id']
    assert context.response['id'] == item_id, f'{item} id does not match'

@given('I created a new card')
def step_impl(context):
    _, card = request_manager.post_request('cards', payload={'name': 'New card', 'idList': "627ee9268cea2a5a877b8b40"})
    context.card = card

@then('the checklist is created on the card')
def step_impl(context):
    status_code, response = checklist_manager.get_checklist(context.response['id'])
    assert status_code == 200, 'Checklist was not created'
    assert response['idCard'] == context.card['id'], 'Checklist was not created on the card'

@then('the checklist is updated')
def step_impl(context):
    _, response = checklist_manager.get_checklist(context.response['id'])
    assert response['name'] == context.response['name'], 'Checklist was not updated'

@then('the checklist is deleted')
def step_impl(context):
    _, response = checklist_manager.get_checklists(context.card['id'])
    assert not any(checklist['id'] == context.checklist['id'] for checklist in response), 'Checklist was not deleted'

@step('the checklist has a completed item')
def step_impl(context):
    _, checkitem = checklist_manager.create_checkitem(context.checklist['id'], 'Completed item', checked=True)
    context.checkitem = checkitem

@then('I receive a list with at least one checklist item')
def step_impl(context):
    assert len(context.response) > 0, 'No checklitems were found'

@then('the checklist item is created on the checklist')
def step_impl(context):
    status_code, response = checklist_manager.get_checkitem(context.checklist['id'], context.response['id'])
    assert status_code == 200, 'Checklist item was not created'
    assert response['idChecklist'] == context.checklist['id'], 'Checklist item was not created on the checklist'

@then('the checklist item is updated')
def step_impl(context):
    _, response = checklist_manager.get_checkitem(context.checklist['id'], context.response['id'])
    assert response['name'] == context.response['name'], 'Checklist item was not updated'

@then('the checklist item is deleted')
def step_impl(context):
    _, response = checklist_manager.get_all_checkitems(context.checklist['id'])
    assert not any(checkitem['id'] == context.checkitem['id'] for checkitem in response), 'Checklist item was not deleted'