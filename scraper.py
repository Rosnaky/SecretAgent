from multiprocessing import Process
from threading import Thread
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json

def setUpDriver():
    print("HU")
    chrome_driver_path = "chromedriver-win64\\chromedriver.exe"
    
    chrome_options = Options()
    chrome_options.add_argument("--auto-open-devtools-for-tabs")  

    # Enable performance logging
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    service = Service(chrome_driver_path)
    
    global driver
    driver = webdriver.Chrome(service=service, options=chrome_options)

def listenToPage(url):
    driver.get(url)

def process_browser_logs_for_network_events(logs):
    """
    Process performance logs and extract details about network requests, including POST and GET methods.
    """
    for entry in logs:
        log = json.loads(entry["message"])["message"]
        if "Network.requestWillBeSent" in log["method"]:
            request = log.get("params", {}).get("request", {})
            url = request.get("url", "N/A")
            method = request.get("method", "N/A")
            headers = request.get("headers", {})
            post_data = request.get("postData", "")

            yield {
                "url": url,
                "method": method,
                "headers": headers,
                "post_data": post_data,
            }

def closeConnection():
    driver.quit()

def printNetworkLogs(filename):
    try:
        with open(filename, 'w') as f:
            while True:
                logs = driver.get_log("performance")
                events = process_browser_logs_for_network_events(logs)
                for event in events:
                    try:
                        if ("N/A" == event["url"]):
                            continue

                        f.write(json.dumps(event, indent=4))
                        f.write("\n\n")
                    except Exception as e:
                        print(f"Error writing log: {e}")
    finally:
        # closeConnection()
        pass


# Set up the driver
# setUpDriver()

# # Open the page
# listenToPage(url="http://localhost:3000/")

# while True:
#     s = time.time()

#     if time.time()-s < 7:
#         time.sleep(0.2)

#     printNetworkLogs("./network_outputs.txt")