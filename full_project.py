from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

web_options = webdriver.EdgeOptions()
web_options.add_experimental_option("detach", True)

drivers = webdriver.Edge(options=web_options)
drivers.get("https://www.linkedin.com/jobs/")
drivers.implicitly_wait(5)

usr_name = drivers.find_element(By.ID, value="session_key")
usr_name.send_keys("shaikmudassir443@gmail.com")

pwd = drivers.find_element(By.ID, value="session_password")
pwd.send_keys("NOT_@_a_PASSWORD")

sign_in = drivers.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(15)

show_all_jobs = drivers.find_element(By.LINK_TEXT, value="Show all").click()

easy_apply = drivers.find_element(By.PARTIAL_LINK_TEXT, "Easy Apply").click()





