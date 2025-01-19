from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import requests
import time

def directory_discovery(base_url):
    with open('utils/common.txt', 'r') as file:
        file_paths = [line.strip() for line in file.readlines()]

    driver = webdriver.Firefox()

    results = []

    for path in file_paths:
        try:
            url = f"{base_url}/{path}"
            
            driver.get(url)

            response = requests.get(url)

            if response.status_code != 404 and url == driver.current_url:  
                results.append(path)
        
        except WebDriverException as e:
            print(f"Error accessing {url}: {e}")

    driver.quit()

    with open('results/results_directory_discovery.txt', 'w') as result_file:
        if len(results) > 0:
            result_file.write("Exposed directories\n:")
            for path in results:
                result_file.write(f"{path}\n")


directory_discovery("http://localhost:3000")