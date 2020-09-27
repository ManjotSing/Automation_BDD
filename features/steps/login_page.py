from locators.locators import LoginLocators
from features.steps.base_page import BasePage
from behave import *

@then('enter username {username}')
def enter_user_name(context,username):
    context.driver.find_element_by_id(LoginLocators.username_id).clear()
    context.driver.find_element_by_id(LoginLocators.username_id).send_keys(username);

@then('enter password {password}')
def enter_user_password(context, password):
    context.driver.find_element_by_id(LoginLocators.password_id).clear()
    context.driver.find_element_by_id(LoginLocators.password_id).send_keys(password);

@then('press login')
def login(context):
    context.driver.find_element_by_id(LoginLocators.login_button).click();