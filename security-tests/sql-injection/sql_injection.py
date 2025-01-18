from selenium import webdriver
import time

driver = webdriver.Firefox()

with open('sqli.txt', 'r') as file:
    statements = [line.strip() for line in file.readlines()]

base_url = 'http://localhost:3000/#/login'

results = []

driver.get(base_url)

time.sleep(1)

email_input = driver.find_element("xpath", '//input[@id="email"]')
password_input = driver.find_element("xpath", '//input[@id="password"]')
login_button = driver.find_element("xpath", '//button[@id="loginButton"]')

#for owasp
dismiss_button = driver.find_element("xpath", "//button[contains(@class, 'close-dialog')]")
if dismiss_button:
    dismiss_button.click()

password_input.send_keys("password")

print("Starting testing...")
for statement in statements:
    email_input.clear()
    email_input.send_keys(statement)

    login_button.click()

    if driver.current_url != base_url:
        results.append(statement)
        driver.get(base_url)

        email_input = driver.find_element("xpath", '//input[@id="email"]')
        password_input = driver.find_element("xpath", '//input[@id="password"]')
        login_button = driver.find_element("xpath", '//button[@id="loginButton"]')
        password_input.send_keys("password")

with open('results.txt', 'w') as result_file:
    if len(results) > 0:
        result_file.write("Potential vulnerabilities\n:")
        for statement in results:
            result_file.write(f"{statement}\n")

print("Testing completed. Results saved to 'results.txt'.")


        

