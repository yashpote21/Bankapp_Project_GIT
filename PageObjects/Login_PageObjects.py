from selenium.webdriver.common.by import By

# Creating class for Login pageObjects and methods.
class Login_Class:

    # XPATH for Login link
    Login_Link_XPATH = "//a[normalize-space()='Login']"
    # XPATH for Username
    Text_Username_XPATH = "//input[@id='username']"
    # XPATH for Password
    Text_Password_XPATH = "//input[@id='password']"
    # XPATH for Login button
    Click_Login_Button_XPATH = "//button[@id='loginButton']"
    # XPATH for validate User Login
    Validate_Login_XPATH = "//h2[normalize-space()='Dashboard']"

    # Creating constructor
    def __init__(self, driver):
        self.driver = driver

    # Method to Click on Login link
    def Click_Login_Link(self):
        self.driver.find_element(By.XPATH, self.Login_Link_XPATH).click()

    # Method to Entering Username
    def Enter_Username(self, username):
        self.driver.find_element(By.XPATH, self.Text_Username_XPATH).send_keys(username)

    # Method to Entering Password
    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.Text_Password_XPATH).send_keys(password)

    # Method to CLick on Login button
    def Click_Login_Button(self):
        self.driver.find_element(By.XPATH, self.Click_Login_Button_XPATH).click()

    # Method to Validating User Login or not
    def Validate_UserLogin(self):
        try:
            success_msg = self.driver.find_element(By.XPATH, self.Validate_Login_XPATH).text
            return success_msg
        except:
            pass
