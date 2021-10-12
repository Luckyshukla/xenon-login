from behave import *
from selenium import webdriver
import time


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="/home/xs151-lucshu/Downloads/chromedriver_linux64/chromedriver")


@when('I open xenon login dashboard')
def step_impl(context):
    context.driver.get("https://xs-onboarding.neuralcompany.work/onboarding/login")


@when('Enter user name "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id("email").send_keys(user)
    context.driver.find_element_by_id("password").send_keys(pwd)


@when('click on login button')
def step_impl(context):
    context.driver.find_element_by_id("send-invite").click()
    time.sleep(3)


@then('User must successfully login to dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Training Module')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Training Module":
        context.driver.close()
        assert True, "Test Passed"
