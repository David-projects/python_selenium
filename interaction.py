from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)



# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# website_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
#
# print(website_count.text)
# # website_count.click()
#
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# driver.get("http://secure-retreat-92358.herokuapp.com/")
# name = driver.find_element(By.NAME, value="fName")
# name.send_keys("Hello")
#
# name_last = driver.find_element(By.NAME, value="lName")
# name_last.send_keys("bye")
#
# email = driver.find_element(By.NAME, value="email")
# email.send_keys("email@gmail.com")
#
# button = driver.find_element(By.CSS_SELECTOR, value="form button")
# button.click()

driver.get("https://orteil.dashnet.org/experiments/cookie/")
button = driver.find_element(By.ID, value="cookie")

items = driver.find_elements(By.CSS_SELECTOR, value="#store div")

items_id = [item.get_attribute("id") for item in items]

print(items)

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes
run_game = True
while run_game:
    button.click()

    if time.time() > timeout:
        prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = items_id[n]

        # Get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
#driver.quit()