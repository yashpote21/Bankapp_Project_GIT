import time

import pytest

from PageObjects.Login_PageObjects import Login_Class
from PageObjects.SearchUser_Page import Search_User_Class
from Utilities.ReadProperties import ReadConfigFile
from Utilities.logger import Log_Class


class Test_SearchUser_param_Class:

    username = ReadConfigFile.GetUsername()
    password = ReadConfigFile.GetPassword()

    log = Log_Class.loggen()


    @pytest.mark.skip(reason = "No way of currently test this...")
    def test_SearchUser_param_005(self, setup, get_DataFor_SearchUser):
        self.log.info("test_SearchUser_005 is started")
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
            # self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_005_Pass.png")
            # self.log.info("test_SearchUser_004 is Passed")
            assert True
        else:
            self.log.info("User not LoggedIn")
            self.log.info("Capturing screenshot")
            # Capturing Screenshot
            self.driver.save_screenshot(".\\Screenshots\\test_UserLogin_005_Fail.png")
            self.log.info("test_SearchUser_005 is Failed\n")
            assert False

        self.su = Search_User_Class(self.driver)
        self.su.Click_UserManagement_Btn()
        self.log.info("Click on User Management button")

        Search_User = get_DataFor_SearchUser[0]
        Expected_Result = get_DataFor_SearchUser[1]

        self.su.Enter_Username(Search_User)
        self.log.info(f"Entering Username:- {Search_User}")
        self.su.Click_SearchUser_Btn()
        self.log.info("Click on Search User button")
        self.log.info("Validate User found or not")
        time.sleep(3)

        Status_List_Params = []

        if self.su.Validate_SearchUser() == "Edit User" and Expected_Result == 'pass':
            self.log.info("User found")
            self.log.info("Capturing screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_005_Pass.png")
            self.log.info("test_SearchUser_005 is Passed")
            Status_List_Params.append('pass')
            assert True
        elif self.su.Validate_SearchUser() == "Edit User" and Expected_Result == 'fail':
            self.log.info("User not found")
            self.log.info("Capturing screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_005_Fail.png")
            self.log.info("test_SearchUser_005 is Failed\n")
            Status_List_Params.append('fail')
            assert False
        elif self.su.Validate_SearchUser() != "Edit User" and Expected_Result == 'pass':
            self.log.info("User not found")
            self.log.info("Capturing screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_005_Fail.png")
            self.log.info("test_SearchUser_005 is Failed\n")
            Status_List_Params.append('fail')
            assert False
        elif self.su.Validate_SearchUser() != "Edit User" and Expected_Result == 'fail':
            self.log.info("User not found")
            self.log.info("Capturing screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_SearchUser_005_Pass.png")
            self.log.info("test_SearchUser_005 is Passed")
            Status_List_Params.append('pass')
            assert True
        self.log.info(f"Number of 'pass' test cases in params--> {str(Status_List_Params.count('pass'))}")
        self.log.info(f"Number of 'fail' test cases in params--> {str(Status_List_Params.count('fail'))}")
        self.log.info("test_SearchUser_005 is Completed\n")