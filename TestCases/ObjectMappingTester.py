from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')
chrome_options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)
action=ActionChains(driver)

driver.get("https://www.tacobell.com/")
driver.maximize_window()
time.sleep(3)
print(driver.title)
driver.find_element(By.XPATH,"//button[contains(text(),'AGREE')]").click()
time.sleep(10)
driver.find_element(By.XPATH,"//a[@href='/food']").click()
time.sleep(3)
print("test completed!")