import allure
import pytest

from PageObjects.Login_PageObjects import Login_Class
from PageObjects.SearchUser_Page import Search_User_Class
from Utilities.ReadProperties import ReadConfigFile
from Utilities.logger import Log_Class


class Test_SearchUser_Class:

    username = ReadConfigFile.GetUsername()
    password = ReadConfigFile.GetPassword()
    Username = ReadConfigFile.getUsername_for_SearchUser()

    log = Log_Class.loggen()


    # @pytest.mark.SearchUser
    @allure.title("This is a Search User test case")
    def test_SearchUser_004(self, setup):
        self.log.info("test_SearchUser_004 is started")
        self.log.info("Opening browser")
        self.log.info("Launching URL")
        self.driver = setup
        self.lp = Login_Class(self.driver)
        self.lp.Click_Login_Link()
        self.log.info("Click on login link")
        self.lp.Enter_Username(self.username)
        self.log.info(f"Entering Username:- {self.username}")
        self.lp.Enter_Password(self.password)
        self.log.info(f"Entering Password:- {self.password}")
        self.lp.Click_Login_Button()
        self.log.info("Click on login button")
        self.log.info("Validating User Logged In or not")
        if self.lp.Validate_UserLogin() == 'Dashboard':
            self.log.info("User LoggedIn")
            # self.log.info("Capturing screenshot")
            # Capturing Screenshot
            # self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_004_Pass.png")
            # self.log.info("test_SearchUser_004 is Passed")
            assert True
        else:
            self.log.info("User not LoggedIn")
            self.log.info("Capturing screenshot")
            # Capturing Screenshot
            self.driver.save_screenshot(".\\Screenshots\\test_UserLogin_003_Fail.png")
            self.log.info("test_SearchUser_004 is Failed\n")
            assert False

        self.su = Search_User_Class(self.driver)
        self.su.Click_UserManagement_Btn()
        self.log.info("Click on User Management button")
        self.su.Enter_Username(self.Username)
        self.log.info(f"Entering Username:- {self.Username}")
        self.su.Click_SearchUser_Btn()
        self.log.info("CLick on Search User button")
        self.log.info("Validate User found or not")
        if self.su.Validate_SearchUser() == "Edit User":
            self.log.info("User found")
            self.log.info("Capturing screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_004_Pass.png")
            self.log.info("test_SearchUser_004 is Passed")
            assert True
        else:
            self.log.info("User not found")
            self.log.info("Capturing screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_004_Fail.png")
            self.log.info("test_SearchUser_004 is Failed\n")
            assert False
        self.log.info("test_SearchUser_004 is Completed\n")