from behave import *

use_step_matcher("parse")


@when("I assign AFE new")
def step_impl(context):
    context.browser.visit(context.get_url('/AFE/'))
    context.browser.visit(context.get_url('/AFE/new/test-txf15k/'))
    form = context.browser.find_by_tag('form').first
    form.find_by_value('Assignar').first.click()
    assert context.browser.is_text_present("Assignació Satisfactória")
    assert context.browser.is_text_present("alta")
    assert context.browser.is_text_present("CW")


@then("I'm viewing the new assigned in the workload of copywriter")
def step_impl(context):
    context.browser.visit(context.get_url('/Redactor_cap/carrega_de_treball/'))
    assert context.browser.is_text_present("alta")
    assert context.browser.is_text_present("CW")
    assert context.browser.is_text_present("Test")
