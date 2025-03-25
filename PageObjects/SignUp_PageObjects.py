from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


# Creating class for SignUp PageObjects and Methods.
class SignUp_Class:

    # Xpath of SignUp link.
    SignUp_Link_XPATH = "//a[normalize-space()='Sign Up']"
    # Xpath of Username.
    Text_Username_XPATH = "//input[@id='username']"
    # Xpath of Password.
    Text_Password_XPATH = "//input[@id='password']"
    # Xpath of Email.
    Text_Email_XPATH = "//input[@id='email']"
    # Xpath of Phone Number.
    Text_Phone_XPATH = "//input[@id='phone']"
    # Xpath of Create User button.
    Button_CreateUser_XPATH = "//button[@id='createUserButton']"
    # Xpath for Validating User created successfully.
    Success_Message_XPATH = "//div[@id='successMessage']"


    # Defining Constructor
    def __init__(self, driver):
        self.driver = driver

    # Method to Click on SignUp link.
    def Click_SignUp_Link(self):
        self.driver.find_element(By.XPATH, self.SignUp_Link_XPATH).click()

    # Method to Entering Username.
    def Enter_Username(self, username):
        self.driver.find_element(By.XPATH, self.Text_Username_XPATH).send_keys(username)

    # Method to Entering Password.
    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.Text_Password_XPATH).send_keys(password)

    # Method to Entering Email.
    def Enter_Email(self, email):
        self.driver.find_element(By.XPATH, self.Text_Email_XPATH).send_keys(email)

    # Method to Entering Phone Number.
    def Enter_Phone(self, phone):
        self.driver.find_element(By.XPATH, self.Text_Phone_XPATH).send_keys(phone)

    # Method to Click on Create User button.
    def Click_CreateUser_Button(self):
        self.driver.find_element(By.XPATH, self.Button_CreateUser_XPATH).click()

    # Method to Validating User created successfully or not.
    def Validate_UserCreation(self):
        try:
            success_msg = self.driver.find_element(By.XPATH, self.Success_Message_XPATH).text
            return success_msg  # User created successfully
        except:
            pass