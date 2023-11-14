from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

url = "https://www.psychometry.co.il"

driver.get(url)

input('Press Enter when you are ready!')

html_content = driver.page_source

driver.quit()

with open("webpage.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML content saved to webpage.html")