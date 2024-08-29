from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='/Users/dominickdufner/Coding/chromedriver')
chrome_options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)
action=ActionChains(driver)

driver.get("https://www.tacobell.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, "//button[contains(text(),'AGREE')]").click()
print(driver.title)
time.sleep(3)
driver.find_element(By.XPATH,"//nav[@class='styles_footer-navigation__3sZCB styles_navi__1GbAA']//a[@data-id='safe-anchor-%2Fabout-us']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//nav[@class='styles_footer-navigation__3sZCB styles_navi__1GbAA']//a[contains(text(),'Contact Us')]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//nav[@class='styles_footer-navigation__3sZCB styles_navi__1GbAA']//a[contains(text(),'FAQS')]").click()
time.sleep(5)

print("test completed!")