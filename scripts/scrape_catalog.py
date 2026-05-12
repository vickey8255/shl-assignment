from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

URL = "https://www.shl.com/solutions/products/product-catalog/"

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get(URL)

time.sleep(15)

tables = driver.find_elements(By.TAG_NAME, "tr")

assessments = []

for row in tables:

    cols = row.find_elements(By.TAG_NAME, "td")

    if len(cols) >= 1:

        try:
            name = cols[0].text.strip()

            if name and name != "Individual Test Solutions":

                assessments.append({
                    "name": name,
                    "url": URL,
                    "description": "",
                    "test_type": "Unknown"
                })

        except:
            pass

driver.quit()

unique = []
seen = set()

for item in assessments:

    if item["name"] not in seen:

        seen.add(item["name"])
        unique.append(item)

with open("app/catalog.json", "w", encoding="utf-8") as f:

    json.dump(unique, f, indent=2)

print(f"Saved {len(unique)} assessments")