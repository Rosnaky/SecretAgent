from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import time

def sql_injection(base_url):

    api_url = "http://127.0.0.1:3001/api/tests/1"

    headers = {
        "Content-Type": "application/json"
    }

    requests.patch(api_url, json={"status": "In Progress"}, headers=headers)
    
    # driver = webdriver.Firefox()
    chrome_options = Options()
    chrome_options.add_argument("--auto-open-devtools-for-tabs")  

    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    
    driver = webdriver.Chrome(options=chrome_options)

    with open('utils/sqli.txt', 'r') as file:
        statements = [line.strip() for line in file.readlines()]

    url = f'{base_url}/#/login'

    results = []

    driver.get(url)

    time.sleep(1)

    email_input = driver.find_element("xpath", '//input[@id="email"]')
    password_input = driver.find_element("xpath", '//input[@id="password"]')
    login_button = driver.find_element("xpath", '//button[@id="loginButton"]')

    #for owasp
    dismiss_button = driver.find_element("xpath", "//button[contains(@class, 'close-dialog')]")
    if dismiss_button:
        driver.execute_script("arguments[0].click();", dismiss_button)

    password_input.send_keys("password")

    for statement in statements:
        email_input.clear()
        email_input.send_keys(statement)

        login_button.click()

        time.sleep(0.2)

        if driver.current_url != url:
            results.append(statement)
            driver.get(url)

            time.sleep(0.5)

            email_input = driver.find_element("xpath", '//input[@id="email"]')
            password_input = driver.find_element("xpath", '//input[@id="password"]')
            login_button = driver.find_element("xpath", '//button[@id="loginButton"]')
            password_input.send_keys("password")

    with open('results/results_sql_injection.txt', 'w') as result_file:
        if len(results) > 0:
            result_file.write("Exposed directories\n:")
            for path in results:
                result_file.write(f"{path}\n")

    requests.patch(api_url, json={"status": "Complete"}, headers=headers)
    requests.patch(api_url, json={"raw_data" : results}, headers=headers)

    driver.quit()

# sql_injection("http://localhost:3000")



        

