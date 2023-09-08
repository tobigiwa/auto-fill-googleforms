from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

URL: str = "https://docs.google.com/forms/d/e/1FAIpQLSeG_hjjalfPzCFvS_pBT6FYnj5URYeMmCkIooOq0DbXA6LDXg/viewform"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)
c = driver.find_elements(By.CSS_SELECTOR, ".geS5n")[2]
for options in c.find_elements(By.CSS_SELECTOR, ".nWQGrd.zwllIb"):
    print("each text is-----", options.text)


print("length of this option is---",
      len(c.find_elements(By.CSS_SELECTOR, ".nWQGrd.zwllIb")))
time.sleep(5)
driver.quit()
