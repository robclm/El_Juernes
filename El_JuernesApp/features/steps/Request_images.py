from behave import *

use_step_matcher("parse")


@when("I request images")
def step_impl(context):
    context.browser.visit(context.get_url('/Redactor/assigned/test-txf15k/'))
    form = context.browser.find_by_tag('form').first
    form.find_by_value('Demanar Imatges').first.click()
    assert context.browser.is_text_present("La petició ha estat enviada correctament")


@then('I\'m viewing the "Ja s\'ha fet la petició Encara no s\'ha rebut cap imatge" mesage')
def step_impl(context):
    context.browser.visit(context.get_url('/Redactor/assigned/test-txf15k/'))
    assert context.browser.is_text_present("Ja s'ha fet la petició. Encara no s'ha rebut cap imatge.")


@given('I login as copywriter "{CW}" with password "{password}""')
def step_impl(context, CW, password):
    context.browser.visit(context.get_url('/accounts/login/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', CW)
    context.browser.fill('password', password)

    form.find_by_css('button.btn-post').first.click()
    assert context.browser.is_text_present(CW)
