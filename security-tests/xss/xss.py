from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

with open('xss.txt', 'r') as file:
    statements = [line.strip() for line in file.readlines()]

base_url = 'http://localhost:3000/'

results = []

driver.get(base_url)

time.sleep(1)

dismiss_button = driver.find_element("xpath", "//button[contains(@class, 'close-dialog')]")
if dismiss_button:
    dismiss_button.click()

search_input = driver.find_element("xpath", '//input[@type="search" or @type="text"]')

for statement in statements:
    search_input.send_keys(statement)
    search_input.send_keys(Keys.ENTER)

    time.sleep(1)

    try:
        alert = driver.switch_to.alert
        alert.accept()
        results.append(statement)
    except:
        pass
        
    driver.get(base_url)
    search_input = driver.find_element("xpath", '//input[@type="search" or @type="text"]')

with open('results.txt', 'w') as result_file:
    if len(results) > 0:
        result_file.write("Potential vulnerabilities\n:")
        for statement in results:
            result_file.write(f"{statement}\n")

print("Testing completed. Results saved to 'results.txt'.")