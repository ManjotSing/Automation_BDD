from selenium.webdriver.common.by import By
from locators.locators import LeaveLocators
from behave import *

@then('open my leaves tab')
def open_myleaves(context):
    context.driver.find_element(By.XPATH, LeaveLocators.menu_my_leaves).click();

@then('search leave from {from_date}')
def from_date(context,from_date):
    context.driver.find_element(By.ID,LeaveLocators.search_from_date).send_keys(from_date);

@then('search leave to {to_date}')
def to_date(context,to_date):
    context.driver.find_element(By.ID,LeaveLocators.search_to_date).send_keys(to_date);

@then('search')
def search(context):
    context.driver.find_element(By.CLASS_NAME,LeaveLocators.button_search_class).click();