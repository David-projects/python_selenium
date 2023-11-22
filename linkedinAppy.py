from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3766601994&keywords=Python%20developer&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true")

signinButton = driver.find_element(By.XPATH, value="/html/body/div[3]/header/nav/div/a[2]")

signinButton.click()

time.sleep(2)

username = driver.find_element(By.ID, value="username")
username.send_keys("XXXXXXX@gmail.com")

password = driver.find_element(By.ID, value="password")
password.send_keys("XXXXXXXXX")

signinButton = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
signinButton.click()

time.sleep(10)
saveButton = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button')
saveButton.click()