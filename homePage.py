
class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.profile_menu_css = "span.userName"
        self.logout_button_xpath = "//a[5]"

    def open_profile_menu(self):
        self.driver.find_element_by_css_selector(self.profile_menu_css).click()


    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()

