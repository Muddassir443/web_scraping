from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://en.wikipedia.org/wiki/Main_Page"

option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)

web_driver = webdriver.Edge(options=option)
web_driver.get(url)

articles_in_english = web_driver.find_element(By.CSS_SELECTOR, value="#articlecount a").text

print(articles_in_english)

web_driver.quit()