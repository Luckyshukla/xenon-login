from behave import *
from selenium import webdriver
import time


@given('launch Chrome browser')
def launch_browser(self):
    self.driver = webdriver.Chrome(executable_path="/home/xs151-lucshu/Downloads/chromedriver_linux64/chromedriver")


@when('open xenon login dashboard')
def dashboard(self):
    self.driver.get("https://xs-onboarding.neuralcompany.work/onboarding/login")


@when('click on forget button')
def forget_click(self):
    self.driver.find_element_by_class_name("auth-page-link").click()
    time.sleep(3)


@When('Enter the username')
def userId(self):
    self.driver.find_element_by_id("email").send_keys("km.saloni+1@xenonstack.com")
    time.sleep(2)


@When('Hit the submit button')
def submit(self):
    self.driver.find_element_by_id("send-invite").click()
    time.sleep(2)


@Then('User must Retract the password')
def retract_password(self):
    try:
        text = self.driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/main[1]/div[1]/section[1]/div[1]/form[1]/div[3]/p[1]")
    except:
        self.driver.close()
        assert False, "Test Failed"
    if text == "Email sent successfully. Please check your email.":
        self.driver.close()
        assert True, "Email sent successfully. Please check your email."
