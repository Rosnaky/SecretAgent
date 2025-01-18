from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import requests
import time

with open('common.txt', 'r') as file:
    file_paths = [line.strip() for line in file.readlines()]

driver = webdriver.Firefox()

base_url = 'http://localhost:3000'

results = []

print("Starting testing...")
for path in file_paths:
    try:
        url = f"{base_url}/{path}"
        print(f"Testing {url}...")
        
        driver.get(url)
        time.sleep(1)

        response = requests.get(url)

        if response.status_code != 404 and url == driver.current_url:  
            results.append(path)
    
    except WebDriverException as e:
        print(f"Error accessing {url}: {e}")

driver.quit()

with open('results.txt', 'w') as result_file:
    if len(results) > 0:
        result_file.write("Potential vulnerabilities\n:")
        for path in results:
            result_file.write(f"{path}\n")

print("Testing completed. Results saved to 'results.txt'.")
