from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
import time
service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/chromedriver')
chrome_options = Options()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("https://www.tacobell.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//div[@class='styles_flex-section__2GgT-']//div[@class='styles_original__1jkQg']//div").click()

driver.find_element(By.XPATH,"//input[@placeholder='Email Address']").send_keys("domdautomation@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='styles_button__FFI6b styles_button__1NHMg styles_bg-brand__2FGaD styles_button__tzBfg']").click()

time.sleep(15)




