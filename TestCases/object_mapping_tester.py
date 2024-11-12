from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
import time
from selenium.webdriver.common.action_chains import ActionChains

#Chome option
#service = Service(executable_path='/Users/dominickdufner/Coding/chromedriver')
#chrome_options = Options()
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=service)
#action=ActionChains(driver)

#Firefox option
service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action=ActionChains(driver)

driver.get("https://www.tacobell.com/")
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollTo(0, -100);")
#driver.find_element(By.XPATH, "//*[@aria-labelledby='title-icon-search desc-icon-search']").click()
#driver.find_element(By.XPATH, "//div[@class='styles_input-control__2Hp8U']//input[@type='text']").send_keys("taco")
time.sleep(10)

print("test completed!")
driver.quit()