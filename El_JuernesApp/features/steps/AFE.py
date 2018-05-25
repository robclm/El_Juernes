from behave import *

use_step_matcher("parse")


@given('I login a headcopywriter "{HW}" with password "{password}"')
def step_impl(context, HW, password):
    context.browser.visit(context.get_url('/accounts/login/'))
    form = context.browser.find_by_tag('form').first

    context.browser.fill('username', HW)
    context.browser.fill('password', password)

    form.find_by_css('button.btn-post').first.click()
    assert context.browser.is_text_present(HW)


@when("I visit the AFE news page")
def step_impl(context):
    context.browser.visit(context.get_url('/AFE/'))


@then('I\'m viewing the Afe News List')
def step_impl(context):
    assert context.browser.is_text_present("Afe News List")
