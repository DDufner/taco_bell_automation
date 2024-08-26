from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
import time
#firefox
#service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
#firefox_options = Options()
#options = webdriver.FirefoxOptions()
#driver = webdriver.Firefox(service=service)

#chrome
service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')
chrome_options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("https://www.tacobell.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//button[contains(text(),'AGREE')]").click()
driver.find_element(By.XPATH,"//a[@href='/food']").click()
driver.find_element(By.XPATH,"//a[@aria-label='Navigate to Best Sellers category']").click()
driver.find_element(By.XPATH,"//button[@class='styles_button__FFI6b styles_button__1NHMg styles_bg-secondary__F6yGd styles_add-to-cart__2GF8N styles_add-to-cart-button__3sEhU']").click()
driver.find_element(By.XPATH,"//button[@class='styles_button__FFI6b styles_close__WEbpZ']//*[@aria-labelledby='title-icon-close desc-icon-close']").click()
print("fries added to order")

driver.find_element(By.XPATH,"//a[@aria-label='Crunchy Taco']//img[@class='styles_image__3bMG2 styles_product-image__p-OZn']").click()
driver.find_element(By.XPATH,"//img[@alt='Fresco']").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Add to Order')]").click()
driver.find_element(By.XPATH,"//button[@class='styles_button__FFI6b styles_close__WEbpZ']//*[@aria-labelledby='title-icon-close desc-icon-close']").click()
print("taco added to order")

driver.find_element(By.XPATH,"//a[@href='/food']").click()
driver.find_element(By.XPATH,"//a[@aria-label='Navigate to Best Sellers category']").click()
driver.find_element(By.XPATH,"//span[contains(text(),'Drinks')]").click()
driver.find_element(By.XPATH,"//img[@alt='Vanilla Creme Limonada Freeze']").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Add to Order')]").click()
print("drink added to order")

time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='styles_flex-section__2GgT-']//div[@class='full-toolbar_cart-container__3bia5']//article[@class='styles_mini-cart___AA8J styles_show-mini-cart__3bLsn']//footer//a[@class='styles_link-button__29UpC styles_bg-brand__2FGaD styles_mini-cart-cta__1kigf'][contains(text(),'View Bag & Checkout')]").click()
#driver.find_element(By.XPATH,"//button[@class='styles_button__FFI6b styles_close__WEbpZ']//*[@aria-labelledby='title-icon-close desc-icon-close']").click()
#driver.find_element(By.XPATH, "//*[@class='full-toolbar_icon__3PBox']").click()
time.sleep(25)
print("test completed")