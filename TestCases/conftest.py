import pytest
from selenium import webdriver

# Creating for running the Test Cases in Headless Mode.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


# Creating for adding the option in command while running the test cases.
def pytest_addoption(parser):
    parser.addoption("--browser")



# Creating fixture for executing this 'setup' method before running each test case.
@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")

    # if "--browser chrome" then executes this
    if browser == 'chrome':
        driver = webdriver.Chrome()
    # if "--browser edge" then executes this
    elif browser == 'edge':
        driver = webdriver.Edge()
    # if "--browser firefox" then executes this
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    # if "--browser safari" then executes this
    elif browser == 'safari':
        driver = webdriver.Safari()
    # if not any of this then executes this
    else:
        driver = webdriver.Chrome(options = chrome_options)
    # Maximizing window
    driver.maximize_window()
    # Launching URL
    driver.get("https://apps.credence.in/")
    # Giving Inplicit wait of 5 seconds.
    driver.implicitly_wait(5)
    yield driver
    driver.quit()




def pytest_metadata(metadata):
    # To Add
    metadata["Class"] = "Credence"
    metadata["Batch"] = "CT#15"
    metadata["URL"] = "https://automation.credence.in"
    metadata["Build"] = "04"
    metadata["Tested By"] = "Sr. Software Test Engineer: Yash Pote"
    # To Remove
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Python", None)
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)


"""@pytest.fixture()
def setup():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://apps.credence.in/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()"""


@pytest.fixture(params=[
    ('Admin', 'pass'),
    ('Yashp', 'pass'),
    ('Tushar', 'pass'),
    ('Barclays', 'pass'),
    ('Ddmmoo', 'fail'),
    ('Ramdev', 'fail'),
    ('Raghu', 'fail')
])

def get_DataFor_SearchUser(request):
    return request.param