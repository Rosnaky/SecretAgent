from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def xss(base_url):

    api_url = "http://127.0.0.1:3001/api/tests/2"

    headers = {
        "Content-Type": "application/json"
    }

    requests.patch(api_url, json={"status": "In Progress"}, headers=headers)

    # driver = webdriver.Firefox()
    
    chrome_options = Options()
    chrome_options.add_argument("--auto-open-devtools-for-tabs")  

    # Enable performance logging
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    
    driver = webdriver.Chrome(options=chrome_options)


    with open('utils/xss.txt', 'r') as file:
        statements = [line.strip() for line in file.readlines()]

    results = []

    driver.get(base_url)

    time.sleep(1)

    try:

        dismiss_button = driver.find_element("xpath", "//button[contains(@class, 'close-dialog')]")
        if dismiss_button:
            driver.execute_script("arguments[0].click();", dismiss_button)

        search_input = driver.find_element("xpath", '//input[@type="search" or @type="text"]')

        for statement in statements:
            driver.execute_script("""
                arguments[0].value = arguments[1];
                arguments[0].dispatchEvent(new Event('input'));
                arguments[0].dispatchEvent(new Event('change'));
            """, search_input, statement)

            driver.execute_script("""
                arguments[0].dispatchEvent(new KeyboardEvent('keydown', {'key': 'Enter'}));
                arguments[0].dispatchEvent(new KeyboardEvent('keyup', {'key': 'Enter'}));
            """, search_input)

            time.sleep(0.5)

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
        
        requests.patch(api_url, json={"status": "Complete"}, headers=headers)
        requests.patch(api_url, json={"raw_data" : results}, headers=headers)
    except Exception as e:
        with open('results/results_xss.txt', 'w') as result_file:
            result_file.write(f"{e}")
    
    driver.quit()

# xss("http://localhost:3000")