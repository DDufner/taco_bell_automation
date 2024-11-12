from PageObjects.MainPage import MainPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By  
import time

class Test_001_Main_Page_General:
    search_term = "taco"
    email_address = "domdautomation@gmail.com"
    search_icon_xpath = MainPage.search_icon_xpath
    dropdown_search_result = "//*[contains(text(),'Soft Taco')]"
    search_results_dropdown = "//div[@class='styles_results_LTiZ7']"
    target_url = "https://www.tacobell.com/"

    def test_click_on_menu(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(MainPage.main_page_url)
        self.mainPage = MainPage(self.driver)
        self.mainPage.acceptPrivacyPolicy()
        self.mainPage.clickMenuTab()
        if self.driver.current_url == "https://www.tacobell.com/food":
            assert True
        else:
            assert False
        self.driver.quit()
   
    def test_search_for_item(self,driver_setup):
        self.driver = driver_setup
        self.driver.get(MainPage.main_page_url)
        self.mainPage = MainPage(self.driver)
        self.mainPage.searchForItem(self.search_term)
        time.sleep(3)
        self.mainPage.assertElementIsPresent(self.mainPage.search_results_dropdown)
        self.driver.quit()

    def test_confirm_homepage_name(self, driver_setup): 
        self.driver = driver_setup
        self.driver.get(MainPage.main_page_url)
        actual_url = self.driver.title
        if actual_url == "Taco Bell® | Live Más":
            assert True
        else: 
            assert False
        self.driver.quit()

    def test_accept_privacy_policy(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(MainPage.main_page_url)
        self.mainPage = MainPage(self.driver)
        self.mainPage.acceptPrivacyPolicy()
        try:
            self.driver.find_element(By.XPATH, value=self.mainPage.privacy_policy_accept_xpath)
        except NoSuchElementException:
            assert False
        assert True
        self.driver.quit()