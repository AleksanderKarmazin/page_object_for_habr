import time
from selenium import webdriver
import pytest
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from loginPage import LoginPage
from homePage import HomePage



@pytest.mark.usefixtures("driver_init")
class Test_Class_01():
    # ТС_01:Логин
    def test_TC_01(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")

        #Сценарий логина - Начало
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("123456")
        login.click_login()

        homepage = HomePage(driver)
        homepage.open_profile_menu()
        homepage.click_logout()
        time.sleep(3)






        # driver.find_element_by_xpath("//a[contains(text(),'Sign IN')]").click()
        # driver.find_element_by_id("signin-login").clear()
        # driver.find_element_by_id("signin-login").send_keys("testcaseqa5@gmail.com")
        # driver.find_element_by_id("signin-pass").clear()
        # driver.find_element_by_id("signin-pass").send_keys("123456")
        # driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        # Сценарий логина - Конец
        # time.sleep(5)
        #log_out
        # driver.find_element_by_xpath("(//button[@type='button'])[26]").click()
        # driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()

    # # ТС_02:Логин Blank user ID with blank password
    # def test_TC_02(self):
    #     driver = self.driver
    #     driver.get(URL)
    #     time.sleep(3)
    #     # Сценарий логина - Начало
    #     driver.find_element_by_xpath("//a[contains(text(),'Sign IN')]").click()
    #     driver.find_element_by_id("signin-login").clear()
    #     driver.find_element_by_id("signin-login").send_keys("testcaseqa5@gmail.com")
    #     driver.find_element_by_id("signin-pass").clear()
    #     driver.find_element_by_id("signin-pass").send_keys("123456")
    #     driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
    #     # Сценарий логина - Конец
    #     time.sleep(5)
    #     # log_out
    #     driver.find_element_by_xpath("(//button[@type='button'])[26]").click()
    #     driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
    #
    # # ТС_03:Логин Correct user ID with incorrect password
    # def test_TC_03(self):
    #     driver = self.driver
    #     driver.get(URL)
    #     time.sleep(3)
    #     # Сценарий логина - Начало
    #     driver.find_element_by_xpath("//a[contains(text(),'Sign IN')]").click()
    #     driver.find_element_by_id("signin-login").clear()
    #     driver.find_element_by_id("signin-login").send_keys("testcaseqa5@gmail.com")
    #     driver.find_element_by_id("signin-pass").clear()
    #     driver.find_element_by_id("signin-pass").send_keys("123456")
    #     driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
    #     # Сценарий логина - Конец
    #     time.sleep(5)
    #     # log_out
    #     driver.find_element_by_xpath("(//button[@type='button'])[26]").click()
    #     driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
    #
    # # ТС_04:Логин Incorrect user ID with correct password
    # def test_TC_04(self):
    #     driver = self.driver
    #     driver.get(URL)
    #     time.sleep(3)
    #     # Сценарий логина - Начало
    #     driver.find_element_by_xpath("//a[contains(text(),'Sign IN')]").click()
    #     driver.find_element_by_id("signin-login").clear()
    #     driver.find_element_by_id("signin-login").send_keys("testcaseqa5@gmail.com")
    #     driver.find_element_by_id("signin-pass").clear()
    #     driver.find_element_by_id("signin-pass").send_keys("123456")
    #     driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
    #     # Сценарий логина - Конец
    #     time.sleep(5)
    #     # log_out
    #     driver.find_element_by_xpath("(//button[@type='button'])[26]").click()
    #     driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
    #
    # # ТС_05:Логин Incorrect user ID with incorrect password
    # def test_TC_05(self):
    #     driver = self.driver
    #     driver.get(URL)
    #     time.sleep(3)
    #     # Сценарий логина - Начало
    #     driver.find_element_by_xpath("//a[contains(text(),'Sign IN')]").click()
    #     driver.find_element_by_id("signin-login").clear()
    #     driver.find_element_by_id("signin-login").send_keys("testcaseqa5@gmail.com")
    #     driver.find_element_by_id("signin-pass").clear()
    #     driver.find_element_by_id("signin-pass").send_keys("123456")
    #     driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
    #     # Сценарий логина - Конец
    #     time.sleep(5)
    #     # log_out
    #     driver.find_element_by_xpath("(//button[@type='button'])[26]").click()
    #     driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()



        # time.sleep(5)
        # try:
        #     driver.find_element_by_xpath("(//a[contains(@href,'#')])[4]").click()
        # except (ElementClickInterceptedException, NoSuchElementException):
        #     driver.execute_script("window.scrollTo(0, 1500);")  # Скрол
        #     time.sleep(5)
        #     driver.find_element_by_xpath("(//a[contains(@href,'#')])[4]").click()
        #     time.sleep(5)
        # time.sleep(5)

        # from selenium import webdriver
        # from selenium.webdriver.common.by import By
        # # from utilities.handy_wrappers import HandyWrappers
        # import time
        #
        # class GetText():
        #
        #     def test(self):
        #         baseUrl = "https://trunk.businesschain.io/portal"
        #         driver = webdriver.Firefox(executable_path='C:/Tools/geckodriver.exe')
        #         driver.maximize_window()
        #         driver.implicitly_wait(10)
        #         driver.get(baseUrl)
        #
        #         openTabElement = driver.find_element_by_link_text(u"Регистрация")
        #         elementText = openTabElement.text
        #         print("Text on element is: " + elementText)
        #         Text = "Регистрация"
        #         if elementText == Text:
        #             print('they are the same')
        #         else:
        #             print('ALIRT !!!!!!!!!!!!!!!')
        #
        # ff = GetText()
        # ff.test()

