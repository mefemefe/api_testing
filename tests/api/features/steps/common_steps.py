from behave import given, when, then, step
from main.utils.behave_helpers import replace_ids, fill_payload, validate_schema

@given('I created a new card')
def step_impl(context):
    _, context.card = context.request_manager.post_request('cards', payload={'name': 'Behave card', 'idList': context.list['id']})

@when('I send a "{method}" request to "{endpoint}"')
def step_impl(context, method, endpoint):
    endpoint = replace_ids(context, endpoint)
    context.payload = fill_payload(context, payload={})
    context.status_code, context.response = context.request_manager.do_request(method, endpoint, context.payload)

@then('I receive a list with at least "{quantity:d}" "{item}"')
def step_impl(context, quantity, item):
    assert len(context.response) >= quantity, f'No {item}s were found'

@then('I receive a response with the "{item}" id')
def step_impl(context, item):
    item_id = getattr(context, item)['id']
    assert context.response['id'] == item_id, f'{item} id does not match'

@step('the status code is "{status_code:d}"')
def step_impl(context, status_code):
    assert context.status_code == status_code, 'Status code does not match'

@then('I receive a response with the "{schema_name}" schema')
def step_impl(context, schema_name):
    validate_schema(context, schema_name)