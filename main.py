from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.co.uk/gp/product/B0017XHLCO/ref=ox_sc_act_title_1?smid=A37SR40BFQO66T&psc=1")
#
# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"The price is {price.text}.{cent.text}")

driver.get("https://www.python.org/")
events_website = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')
# event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
#
#
#
# events = []
# for time in event_times:
#     print(time.text)

events = []
for event in events_website:
    event_split = event.text.replace("\n", " ").split(" ")
    events.append({
        'time': event_split[0],
        'name': f"{event_split[1]} {event_split[2]}"
    })

print(events)

driver.quit()
