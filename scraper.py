import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json

def setUpDriver():
    # Path to ChromeDriver
    chrome_driver_path = "chromedriver-win64\\chromedriver.exe"
    # Set up WebDriver
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--auto-open-devtools-for-tabs")  # Open DevTools automatically
    # chrome_options.add_argument("--headless=new")  # Optional: Run in headless mode
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    service = Service(chrome_driver_path)
    global driver
    driver = webdriver.Chrome(service=service, options=chrome_options)

def listenToPage(url):
    # Open a webpage
    driver.get(url)

    # Perform actions or analysis
    print(driver.title)


def process_browser_logs_for_network_events(logs):
    """
    Return only logs which have a method that start with "Network.response", "Network.request", or "Network.webSocket"
    since we're interested in the network events specifically.
    """
    for entry in logs:
        log = json.loads(entry["message"])["message"]
        if (
                "Network.response" in log["method"]
                or "Network.request" in log["method"]
                or "Network.webSocket" in log["method"]
        ):
            print(log)
            yield log

def closeConnection():
    driver.quit()

setUpDriver()

listenToPage(
    url="https://stackoverflow.com/questions/31511265/can-i-use-selenium-webdriver-for-chrome-without-using-chromedriver-exe/31540059",
)
# time.sleep(10)
logs = driver.get_log("performance")
events = process_browser_logs_for_network_events(logs)
for e in events:
    print(e)

# closeConnection()