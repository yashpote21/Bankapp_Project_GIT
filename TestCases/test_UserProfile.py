import time

import allure
import pytest


from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from PageObjects.Login_PageObjects import Login_Class
from PageObjects.SignUp_PageObjects import SignUp_Class
from Utilities.ReadProperties import ReadConfigFile
from Utilities.logger import Log_Class


class Test_UserProfile_Class:

    # Username for login
    Username = ReadConfigFile.GetUsername()
    # Password for login
    Password = ReadConfigFile.GetPassword()

    log = Log_Class.loggen()

    # Test case to validate URL. Which says we are landed on correct page or not.

    @allure.title("Check URL")
    # @pytest.mark.Sanity
    def test_BankApp_URL_001(self, setup):
        self.log.info("test_BankApp_URL_001 is started")
        # calling setup method for Opening browser and launching URL.

        self.log.info("Opening browser")
        self.log.info("Launching URL")
        self.driver = setup
        # Validating pase title is matched or not.
        self.log.info("Validating launching correct page or not")
        if self.driver.title == "Bank Application":
            self.log.info("Launching on correct page")
            self.log.info("Capturing test_BankApp_URL_001_Pass screenshot")
            # Capturing Screenshot
            allure.attach(self.driver.get_screenshot_as_png(), name="test_BankApp_URL_001_Pass", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\test_BankApp_URL_001_Pass.png")
            self.log.info("test_BankApp_URL_001 is Passed")
            assert True
        else:
            self.log.info("Launching on different page")
            self.log.info("Capturing test_BankApp_URL_001_Fail screenshot")
            # Capturing Screenshot
            allure.attach(self.driver.get_screenshot_as_png(), name="test_BankApp_URL_001_Fail", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\test_BankApp_URL_001_Fail.png")
            self.log.info("test_BankApp_URL_001 is Failed\n")
            assert False
        self.log.info("test_BankApp_URL_001 is Completed\n")


    # This Test Case is for Sign Up.
    @allure.title("This is a signup test case")
    # @pytest.mark.Sanity
    def test_Signup_002(self, setup):
        self.log.info("test_Signup_002 is started")
        # calling setup method for Opening browser and launching URL.

        self.log.info("Opening browser")
        self.log.info("Launching URL")
        self.driver = setup
        # Calling method from PageObjects
        self.cu = SignUp_Class(self.driver)

        self.log.info("Click on SignUp link")
        # Click on SignUp link.
        self.cu.Click_SignUp_Link()

        # Entering random Username
        username = generate_random_username()
        self.cu.Enter_Username(username)
        self.log.info(f"Enter Username:- {username}")

        # Entering Password:- MyPass@101
        self.cu.Enter_Password('MyPass@101')
        self.log.info("Enter Password:- MyPass@101")

        # Entering random Email
        self.cu.Enter_Email(f"{username}@gmail.com")
        self.log.info(f"Enter Email:- {username}@gmail.com")

        # Entering random Phone number
        self.cu.Enter_Phone(generate_random_phone())
        self.log.info(f"Enter Phone Number:- {generate_random_phone()}")

        self.log.info("Click on Create User button")
        # Click on Create User Button.
        self.cu.Click_CreateUser_Button()


        time.sleep(2)
        self.log.info("Validating User Created or not")
        # Validating User Creation
        if self.cu.Validate_UserCreation() == 'User created successfully':
            # self.driver.save_screenshot("./Screenshots/test_Signup_002_Pass.png")

            self.log.info("User created successfully")
            self.log.info("Capturing test_Signup_002_Pass screenshot")

            allure.attach(self.driver.get_screenshot_as_png(), name="test_Signup_002_Pass",
                          attachment_type=AttachmentType.PNG)
            # Capturing Full Page Screenshot
            width = 1920
            height = self.driver.execute_script(
                "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight)")
            self.driver.set_window_size(width, height)
            page_body = self.driver.find_element(By.TAG_NAME, "body")
            page_body.screenshot(".\\Screenshots\\test_Signup_002_Pass.png")
            # self.driver.save_screenshot(".\\Screenshots\\test_Signup_002_Pass.png")
            self.log.info("test_Signup_002 is Passed")
            assert True
        else:
            # self.driver.save_screenshot("./Screenshots/test_Signup_002_Fail.png")

            self.log.info("User not created")
            self.log.info("Capturing test_Signup_002_Fail screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Signup_002_Fail",
                          attachment_type=AttachmentType.PNG)

            # Capturing Full Page Screenshot
            width = 1920
            height = self.driver.execute_script(
                "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight)")
            self.driver.set_window_size(width, height)
            page_body = self.driver.find_element(By.TAG_NAME, "body")
            page_body.screenshot(".\\Screenshots\\test_Signup_002_Fail.png")
            self.log.info("test_Signup_002 is Failed\n")
            assert False
        self.log.info("test_Signup_002 is completed\n")


    @allure.title("This is a Login test case")
    # @pytest.mark.Sanity
    def test_UserLogin_003(self, setup):
        self.log.info("test_UserLogin_003 is started")

        self.log.info("Opening browser")
        self.log.info("Launching URL")
        # calling setup method for Opening browser and launching URL.
        self.driver = setup

        # Calling method from PageObjects
        self.lp = Login_Class(self.driver)

        self.log.info("Click on Log In link")
        # Click on Login link.
        self.lp.Click_Login_Link()

        # Entering Username:- YashTech
        self.lp.Enter_Username(self.Username)
        self.log.info(f"Entering Username:- {self.Username}")

        # Entering Password:- YashTech@101
        self.lp.Enter_Password(self.Password)
        self.log.info(f"Entering Password:- {self.Password}")

        self.log.info("Click on Log In button")
        # Click on Login button.
        self.lp.Click_Login_Button()

        self.log.info("Validating User Logged In or not")
        # Validating User Logged in or not.
        if self.lp.Validate_UserLogin() == 'Dashboard':
            self.log.info("User LoggedIn")
            self.log.info("Capturing test_UserLogin_003_Pass screenshot")
            # Capturing Screenshot
            allure.attach(self.driver.get_screenshot_as_png(), name="test_UserLogin_003_Pass",
                          attachment_type=AttachmentType.PNG)

            self.driver.save_screenshot(".\\Screenshots\\test_UserLogin_003_Pass.png")
            self.log.info("test_UserLogin_003 is Passed")
            assert True
        else:
            self.log.info("User not LoggedIn")
            self.log.info("Capturing test_UserLogin_003_Fail screenshot")

            allure.attach(self.driver.get_screenshot_as_png(), name="test_UserLogin_003_Fail",
                          attachment_type=AttachmentType.PNG)
            # Capturing Screenshot
            self.driver.save_screenshot(".\\Screenshots\\test_UserLogin_003_Fail.png")
            self.log.info("test_UserLogin_003 is Failed\n")
            assert False
        self.log.info("test_UserLogin_003 is completed\n")



import random
import string

# It generater the Random Username for SignUp page.
def generate_random_username(length = 4):
    username = 'User' + ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return username

"""
# It generater the Random Password for SignUp page.
def generate_random_password(end = '@101'):
    return generate_random_username() + end
"""


# It generater the Random Email for SignUp page.
def generate_random_email(domain='gmail.com'):
    email = generate_random_username() + '@' + domain
    return email


# It generater the Random Phone Number for SignUp page.
def generate_random_phone():
    return ''.join(random.choices(string.digits, k=10))
