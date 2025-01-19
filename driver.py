'''
Order of tasks
1) Look at network requests
2) Look at code
3) Sql injection
4) Unrestricted domain 
5) Execute brute-force login
'''

from threading import Thread
import time
import scraper
import sys

filename = "network_outputs.txt"

def init_selenium(url):
    scraper.setUpDriver()
    scraper.listenToPage(url)

def getUrl() -> str:
    if (len(sys.argv) > 1):
        return sys.argv[1]
    else:
        return "Invalid link"
    
def listenToNetwork(fname):
    while True:
        s = time.time()

        if time.time()-s < 7:
            time.sleep(0.2)

        scraper.printNetworkLogs(fname)
        

url = getUrl()

if (url != "Invalid link"):
    init_selenium(url)
    listenToNetwork(filename)
    # thread = Thread(listenToNetwork, args=[filename])
    # thread.start()
