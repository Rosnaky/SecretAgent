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
import brute_force
import sql_injection
import xss
import directory_discovery

filename = "network_outputs.txt"

def init_selenium(url):
    scraper.setUpDriver()
    scraper.listenToPage(url)
    # pass

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
    sql_injection_thread = Thread(target=sql_injection.sql_injection, args=[url])
    sql_injection_thread.start()

    # xss_thread = Thread(target=xss.xss, args=[url])
    # xss_thread.start()
    
    # brute_force_thread = Thread(target=brute_force.brute_force, args=[url])
    # brute_force_thread.start()

    directory_discovery_thread = Thread(target=directory_discovery.directory_discovery, args=[url])
    directory_discovery_thread.start()

    # listenToNetwork(filename)
    # thread = Thread(target=listenToNetwork, args=[filename])
    # thread.start()
