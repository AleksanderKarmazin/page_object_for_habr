import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox(executable_path='C:/Tools/geckodriver.exe')
    yield driver
    driver.quit()
