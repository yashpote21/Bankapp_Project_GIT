from selenium.webdriver.common.by import By


class Search_User_Class:

    UserManagement_btn_XPATH = "//a[normalize-space()='User Management']"
    Text_Username_XPATH = "//input[@id='username']"
    Link_Dashboard_XPATH = "//a[normalize-space()='Dashboard']"
    SearchUser_btn_XPATH = "//button[normalize-space()='Search User']"
    Validate_SearchUser_XPATH = "//h2[normalize-space()='Edit User']"


    def __init__(self, driver):
        self.driver = driver
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def Click_UserManagement_Btn(self):
        self.driver.find_element(By.XPATH, self.UserManagement_btn_XPATH).click()

    def Enter_Username(self, username):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.Text_Username_XPATH).send_keys(username)

    def Click_Dashboard(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.Link_Dashboard_XPATH).click()

    def Click_SearchUser_Btn(self):
        self.driver.find_element(By.XPATH, self.SearchUser_btn_XPATH).click()

    def Validate_SearchUser(self):
        try:
            success_msg = self.driver.find_element(By.XPATH, self.Validate_SearchUser_XPATH).text
            return success_msg
        except:
            pass
