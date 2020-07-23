
class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.profile_menu_xpath = "(//button[@type='button'])[26]"
        self.logout_button_xpath = "//a[contains(text(),'Logout')]"

    def open_profile_menu(self):
        self.driver.find_element_by_xpath(self.profile_menu_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()
