from selenium.webdriver.common.by import By
from features.steps.base_page import BasePage
from locators.locators import HomeLocators
from locators.locators import LeaveLocators
from behave import *;

@then ('open leaves tab')
def click_apply_leave(context):
    BasePage.hover(HomeLocators.leave_hover)
    context.driver.find_element(By.XPATH, LeaveLocators.menu_leave_tab).click();

@then ('select leave type as {leavetype}')
def select_leave_type(context,leavetype):
    context.driver.find_element(By.XPATH, LeaveLocators.select_leave_type).click();
    if leavetype=='Vacation US':
        context.driver.find_element(By.XPATH, LeaveLocators.leave_type_vacation).click();
    elif leavetype=='FMLA US':
        context.driver.find_element(By.XPATH, LeaveLocators.leave_type_fmla).click();

@then ('apply leave from {fromdate}')
def leave_from_date(context,fromdate):
    context.driver.find_element(By.XPATH,LeaveLocators.leave_from_date).clear();
    context.driver.find_element(By.XPATH, LeaveLocators.leave_from_date).send_keys(fromdate);

@then ('apply leave to {todate}')
def leave_to_date(context,todate):
    context.driver.find_element(By.XPATH,LeaveLocators.leave_to_date).clear();
    context.driver.find_element(By.XPATH, LeaveLocators.leave_to_date).send_keys(todate);

@then ('apply leave')
def apply_leave(self):
    self.driver.find_element(By.ID,LeaveLocators.button_leave_apply).click();
    self.driver.implicitly_wait(30);
