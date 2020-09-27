from behave import *
from selenium import webdriver
from config.factory_manager import FactoryManager

@given('launch browser')
def launch_browser(context):
    context.driver=FactoryManager.createDriver("Chrome");


@when('open orange hrm homepage')
def open_home_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/");


@then('verify the logo')
def verify_logo(context):
    status=context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed();
    assert status is True


@then('close browser')
def close_browser(context):
    context.driver.close();

