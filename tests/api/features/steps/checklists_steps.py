from behave import given, when, then, step
from main.trello.api.checklists_manager import ChecklistsManager

checklist_manager = ChecklistsManager()

@step('I created a checklist on the card')
def step_impl(context):
    _, checklist = checklist_manager.create_checklist(context.card['id'], 'New checklist')
    context.checklist = checklist

@step('I created a completed item on the checklist')
def step_impl(context):
    _, checkitem = checklist_manager.create_checkitem(context.checklist['id'], 'Completed item', checked=True)
    context.checkitem = checkitem

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