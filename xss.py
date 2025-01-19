from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def xss(base_url):
    driver = webdriver.Firefox()

    with open('utils/xss.txt', 'r') as file:
        statements = [line.strip() for line in file.readlines()]

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

        time.sleep(0.05)

        try:
            alert = driver.switch_to.alert
            alert.accept()
            results.append(statement)
        except:
            pass
            
        driver.get(base_url)
        search_input = driver.find_element("xpath", '//input[@type="search" or @type="text"]')

    with open('results/results_xss.txt', 'w') as result_file:
        if len(results) > 0:
            result_file.write("Successful XSS Attacks\n:")
            for statement in results:
                result_file.write(f"{statement}\n")

xss("http://localhost:3000")