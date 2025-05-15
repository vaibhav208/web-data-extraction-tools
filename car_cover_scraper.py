from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time

# Set up headless Chrome browser
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

url = 'https://www.olx.in/items/q-car-cover'
driver.get(url)
time.sleep(5)  # wait for page to fully load

items = []
ads = driver.find_elements("css selector", "li.EIR5N")

for ad in ads:
    try:
        title = ad.find_element("css selector", "span._2tW1I").text
        price = ad.find_element("css selector", "span._89yzn").text
        link = ad.find_element("css selector", "a").get_attribute("href")
        items.append({
            "title": title,
            "price": price,
            "link": link
        })
    except:
        continue

driver.quit()

with open("car_covers.json", "w") as f:
    json.dump(items, f, indent=2)

print("Saved car cover listings to car_covers.json")
