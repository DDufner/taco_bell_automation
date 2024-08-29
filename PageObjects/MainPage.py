from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path='/Users/dominickdufner/Coding/chromedriver')
chrome_options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)
action=ActionChains(driver)

class MainPage:
    #verified as working
    #main items and side bar
    tacoBell_icon_xpath = "//*[@class='styles_svg__1dXoB']"
    menu_tab_xpath = "//a[@href='/food']"
    search_field_xpath = "//div[@class='styles_full__3edrq styles_toolbar__2w15g']//input[@type='text']"
    locations_tab_xpath = "//a[@href='/locations']"
    delivery_tab_xpath = "//a[@href='/delivery']"
    rewards_tab_xpath = "//a[@href='/rewards']"
    nutrition_tab_xpath = "//a[@href='/nutrition']"
    gift_cards_tab_xpath = "//a[@href='/gift-cards']"
    rewards_icon_xpath = "//div[@class='styles_flex-section__2GgT-']//*[@class='full-toolbar_icon__3PBox']"
    privacy_policy_accept_xpath = "//button[contains(text(),'AGREE')]"
    privacy_button_xpath = "//button[@class='ot-floating-button__open']"
    privacy_summary_close_id = "close-pc-btn-handler"
    order_now_button_xpath = "//a[contains(text(),'Order Now')]"
    explore_menu_button_xpath = "//a[contains(text(),'Explore Menu')]"
    login_button_xpath = "//div[@class='styles_flex-section__2GgT-']//div[@class='styles_original__1jkQg']//div"
    start_your_order_button_xpath = "//a[contains(text(),'Start your order')]"
    location_search_field_xpath = "//div[@class='styles_location-layout-desktop__333Zo']//input[@type='text']"
    location_search_xbutton_xpath = "//a//button[@class='styles_button__27tOv']"
    cart_icon_xpath ="//div[@class='styles_flex-section__2GgT-']//div[@class='full-toolbar_cart-container__3bia5']"

    #links at bottom
    about_us_link_xpath = "//a[contains(text(),'About Us')]"
    continue_us_link_xpath = "//a[contains(text(),'Contact Us')]"
    FAQS_link_xpath = "//a[contains(text(),'FAQS')]"


    #needs to be confirmed
    email_field_xpath = "//input[@type='email']"
    cart_icon_xpath = "//div[@class='styles_flex-section__2GgT-']//div[@class='full-toolbar_cart-container__3bia5']"
    change_location_link_xpath = "//div[@class='styles_flex-section__2GgT-']//div//div[@class='styles_change-link__k7YyB'][contains(text(),'Change')]"
    
    def __init__(self, driver): #constructor that invokes objects for main page class.  
        self.driver=driver

    def acceptPrivacyPolicy(self):
        self.driver.find_element(By.XPATH, value=self.privacy_policy_accept_xpath).click()

#   setLocation function not working, 'change' link is bad        
    def setLocation(self,location):
        try:
            self.driver.find_element(By.XPATH, value=self.change_location_link_xpath).click()
        except:
            self.driver.find_element(By.XPATH, value=self.start_your_order_button_xpath).click()
            self.driver.find_element(By.XPATH, value=self.location_search_field_xpath).send_keys(location)
            self.driver.find_element(By.XPATH, value=self.location_search_xbutton_xpath).click()
    
    def searchForItem(self,searchTerm):
        self.driver.find_element(By.XPATH, value=self.search_field_xpath).send_keys(searchTerm)

    def loginAccount(self,emailAddress):
        self.driver.find_element(By.XPATH, value=self.login_button_xpath).click()
        self.driver.find_element(By.XPATH, value=self.email_field_xpath).sendKeys(emailAddress)
        self.driver.find_element(By.XPATH, value=self.location_search_xbutton_xpath).click()

    def clickMenuTab(self):
        self.driver.find_element(By.XPATH, value=self.menu_tab_xpath).click()

    def clickLocationsTab(self):
        self.driver.find_element(By.XPATH, value=self.locations_tab_xpath).click()

    def clickDeliveryTab(self):
        self.driver.find_element(By.XPATH, value=self.delivery_tab_xpath).click()
        
    def clickRewardsTab(self):
        self.driver.find_element(By.XPATH, value=self.rewards_tab_xpath).click() 

    def clickNutritionTab(self):
        self.driver.find_element(By.XPATH, value=self.nutrition_tab_xpath).click()

    def clickGiftCardsTab(self):
        self.driver.find_element(By.XPATH, value=self.gift_cards_tab_xpath).click()
    