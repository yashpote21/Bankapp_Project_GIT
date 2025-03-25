import time

import pytest

from PageObjects.Login_PageObjects import Login_Class
from PageObjects.SearchUser_Page import Search_User_Class
from Utilities import XLUtilities
from Utilities.ReadProperties import ReadConfigFile
from Utilities.logger import Log_Class

class Test_SearchUser_Excel_DDT_Class:

    username = ReadConfigFile.GetUsername()
    password = ReadConfigFile.GetPassword()
    Excel_File_Path = ".\\TestCases\\TestData\\Dest_Data_Excel_DDT.xlsx"

    log = Log_Class.loggen()

    @pytest.mark.skip(reason="No way of currently test this...")
    def test_SearchUser_Excel_DDT_006(self, setup):
        self.log.info("test_SearchUser_Excel_DDT_006 is started")
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
            assert True
        else:
            self.log.info("User not LoggedIn")
            self.log.info("test_SearchUser_Excel_DDT_006 is Failed\n")
            assert False

        self.su = Search_User_Class(self.driver)
        self.su.Click_UserManagement_Btn()
        self.log.info("Click on User Management button")

        self.row_count = XLUtilities.RowCount(self.Excel_File_Path, "SearchUser")
        # print("Row Count:--> "+ str(self.row_count))

        Status_List = []


        for r in range(2, self.row_count+1):
            self.Search_Username = XLUtilities.ReadData(self.Excel_File_Path, "SearchUser", r, 2)
            self.Expected_Result = XLUtilities.ReadData(self.Excel_File_Path, "SearchUser", r, 3)

            self.su.Enter_Username(self.Search_Username)
            self.log.info(f"Entering Username:- {self.Search_Username}")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            self.su.Click_SearchUser_Btn()
            self.log.info("CLick on Search User button")
            self.log.info("Validate User found or not")


            if self.su.Validate_SearchUser() == "Edit User" and self.Expected_Result == 'pass':
                User_Name = XLUtilities.WriteData(self.Excel_File_Path, "SearchUser", r, 4, 'pass')
                Status = XLUtilities.WriteData(self.Excel_File_Path, "SearchUser", r, 5, 'pass')

                self.log.info("User found")
                self.log.info("test_SearchUser_005 is Passed")
                Status_List.append('pass')
            elif self.su.Validate_SearchUser() == "Edit User" and self.Expected_Result == 'fail':
                User_Name = XLUtilities.WriteData(self.Excel_File_Path, "SearchUser", r, 4, 'pass')
                Status = XLUtilities.WriteData(self.Excel_File_Path, "SearchUser", r, 5, 'fail')

                self.log.info("User not found")
                self.log.info("test_SearchUser_005 is Failed\n")
                Status_List.append('fail')
            elif self.su.Validate_SearchUser() != "Edit User" and self.Expected_Result == 'pass':
                User_Name = XLUtilities.WriteData(self.Excel_File_Path, "SearchUser", r, 4, 'fail')
                Status = XLUtilities.WriteData(self.Excel_File_Path, "SearchUser", r, 5, 'fail')

                self.log.info("User not found")
                self.log.info("test_SearchUser_005 is Failed\n")
                Status_List.append('fail')
            elif self.su.Validate_SearchUser() != "Edit User" and self.Expected_Result == 'fail':
                User_Name = XLUtilities.WriteData(self.Excel_File_Path, "SearchUser", r, 4, 'fail')
                Status = XLUtilities.WriteData(self.Excel_File_Path, "SearchUser", r, 5, 'pass')
                self.log.info("User not found")
                self.log.info("test_SearchUser_005 is Passed")
                Status_List.append('pass')

            self.su.Click_Dashboard()
            self.su.Click_UserManagement_Btn()
            self.log.info("test_SearchUser_005 is Completed\n")
        self.log.info(f"Number of 'pass' test cases--> {str(Status_List.count('pass'))}")
        self.log.info(f"Number of 'pass' test cases--> {str(Status_List.count('fail'))}")
        print(Status_List)
        if 'fail' not in Status_List:
            assert True
        else:
            assert False