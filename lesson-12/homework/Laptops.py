import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.demoblaze.com/")
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Laptops"))).click()
time.sleep(2)

laptops = []

while True:
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "col-lg-4.col-md-6.mb-4")))
    items = driver.find_elements(By.CLASS_NAME, "col-lg-4.col-md-6.mb-4")

    for item in items:
        name = item.find_element(By.CLASS_NAME, "card-title").text
        price = item.find_element(By.CLASS_NAME, "price-container").text.replace("Price: $", "").strip()
        description = item.find_element(By.CLASS_NAME, "card-text").text

        laptops.append({
            "name": name,
            "price": price,
            "description": description
        })


    try:
        next_button = wait.until(EC.element_to_be_clickable((By.ID, "next2")))
        next_button.click()
        time.sleep(2)
    except:
        break  
with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops, f, ensure_ascii=False, indent=4)

print(f"{len(laptops)} ta laptop ma'lumoti 'laptops.json' fayliga saqlandi.")
driver.quit()
