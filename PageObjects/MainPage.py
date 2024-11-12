from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action=ActionChains(driver)

class MainPage:
    #verified as working
    main_page_url = "https://www.tacobell.com/"
    tacoBell_icon_xpath = "//a[@class='styles_logo-ta-co__7nnAb']"
    menu_tab_xpath = "//div[@class='styles_full___yKBl styles_toolbar__NMMef']//a[contains(text(),'Menu')]"
    search_icon_xpath = "//*[@aria-labelledby='title-icon-search desc-icon-search']"
    search_field_xpath = "//div[@class='styles_input-control___Mwtd']//input[@type='text']"
    delivery_tab_xpath = "//a[@href='/delivery']"
    rewards_tab_xpath = "//a[@href='/rewards']"
    nutrition_tab_xpath = "//a[@href='/nutrition']"
    gift_cards_tab_xpath = "//a[@href='/gift-cards']"
    search_results_dropdown = "//div[@class='styles_results_LTiZ7']//a[@href='/search?text=taco']"
    soft_taco_result = "//*[contains(text(),'FAQS')]"
    privacy_policy_accept_xpath = "//button[contains(text(),'AGREE')]"
    privacy_button_xpath = "//button[@class='ot-floating-button__open']"
    privacy_summary_close_id = "close-pc-btn-handler"
    order_now_button_xpath = "//a[@class='styles_link-button__29UpC styles_bg-brand__2FGaD styles_primary-cta__TvcZc'][contains(text(),'Order Now')]"
    location_search_field_xpath = "//div[@class='styles_location-layout-desktop__333Zo']//input[@type='text']"
    location_search_xbutton_xpath = "//a//button[@class='styles_button__27tOv']"
    cart_icon_xpath ="//div[@class='styles_flex-section__2GgT-']//div[@class='full-toolbar_cart-container__3bia5']"

    #links at bottom
    info_links_nav_xpath = "//nav[@class='styles_footer-navigation__3sZCB styles_navi__1GbAA']"
    about_us_link_xpath = "//a[contains(text(),'About Us')]"
    contact_us_link_xpath = "//a[contains(text(),'Contact')]" 
    FAQS_link_xpath = "//a[contains(text(),'FAQS')]"

    def __init__(self, driver): #constructor that invokes objects for main page class.  
        self.driver=driver

    def acceptPrivacyPolicy(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, value=self.privacy_policy_accept_xpath).click()
      
    def setLocation(self, location):
        try:
            self.driver.find_element(By.XPATH, value=self.change_location_link_xpath).click()
        except:
            self.driver.find_element(By.XPATH, value=self.start_your_order_button_xpath).click()
            self.driver.find_element(By.XPATH, value=self.location_search_field_xpath).send_keys(location)
            self.driver.find_element(By.XPATH, value=self.location_search_xbutton_xpath).click()

    def selectItemForOrder(self, best_sellers_xpath, soft_taco_button_xpath):
        self.driver.find_element(By.XPATH, value=self.menu_tab_xpath).click()
        self.driver.find_element(By.XPATH, value= best_sellers_xpath).click()
        self.driver.find_element(By.XPATH, value= soft_taco_button_xpath).click()
    
    def searchForItem(self, searchTerm):
        self.driver.find_element(By.XPATH, value=self.search_icon_xpath).click()
        self.driver.find_element(By.XPATH, value=self.search_field_xpath).send_keys(searchTerm)

    def loginAccount(self, emailAddress):
        self.driver.find_element(By.XPATH, value=self.login_button_xpath).click()
        self.driver.find_element(By.XPATH, value=self.email_field_xpath).sendKeys(emailAddress)
        self.driver.find_element(By.XPATH, value=self.location_search_xbutton_xpath).click()
    
    def assertElementIsPresent(self, webelement):
        try:
            self.driver.find_element(By.XPATH, webelement)
        except NoSuchElementException:
            assert False
        assert True

    def clickMenuTab(self):
        self.driver.find_element(By.XPATH, value=self.menu_tab_xpath).click()

    def clickContactUsLink(self):
        self.driver.find_element(By.XPATH, value=self.contact_us_link_xpath).click()

    def clickItemByXpath(self, webelement):
        self.driver.find_element(By.XPATH, value=webelement).click()

    def confirmURL(self, target_URL):
        current_URL = self.driver.current_url
        if current_URL == target_URL:
            assert True
        else: 
            assert False