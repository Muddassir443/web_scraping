from selenium import webdriver
from selenium.webdriver.common.by import By
website="https://www.amazon.in/Comfortable-Intelligent-Brightness-Adjustments-Compatible/dp/B0CX4ZHR8S/ref=sr_1_3?nsdOptOutParam=true&sr=8-3"
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get(url=website)
price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
final_price = price.text
print(f"The Final price is :{final_price} ")