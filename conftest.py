import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome(executable_path='C:/Tools/chromedriver.exe')
    request.cls.driver = driver
    driver.implicitly_wait(1)
    driver.maximize_window()
    yield
    driver.close()
    print("Browser closed")

@pytest.fixture(scope="class")
def driver_init2(request):
    driver = webdriver.Chrome(executable_path='C:/Tools/chromedriver.exe')
    request.cls.driver = driver
    driver.implicitly_wait(1)
    print("driver_init2")
    yield
    driver.close()
    print("Browser closed")
