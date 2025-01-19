from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import requests
from selenium.webdriver.chrome.options import Options

def directory_discovery(base_url):

    api_url = "http://127.0.0.1:3001/api/tests/4"

    headers = {
        "Content-Type": "application/json"
    }

    requests.patch(api_url, json={"status": "In Progress"}, headers=headers)

    with open('utils/common.txt', 'r') as file:
        file_paths = [line.strip() for line in file.readlines()]

    chrome_options = Options()
    chrome_options.add_argument("--auto-open-devtools-for-tabs")  

    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    
    driver = webdriver.Chrome(options=chrome_options)

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

    requests.patch(api_url, json={"status": "Complete"}, headers=headers)
    requests.patch(api_url, json={"raw_data" : results}, headers=headers)


#directory_discovery("http://localhost:3000")