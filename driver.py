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
from llm import CohereAPI
from dotenv import load_dotenv
import os

filename = "results/network_outputs.txt"
API_KEY = os.getenv("COHERE_API_KEY")

def init_cohere(api_key):
    cohere_api = CohereAPI(api_key=api_key, model="command-r-plus-08-2024")
    return cohere_api


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
        # llm_thread = Thread

def populateRAG(cohere_api: CohereAPI):
    with open("results/network_outputs.txt", 'r') as f:
        network_outputs = f.read()
    with open("utils/network.txt", 'r') as f:
        vulnerable_requests_examples = f.read()
        
    cohere_api.set_documents([
                                {"title": "network_outputs", "snippet": network_outputs},
                                {"title": "vulnerable_requests_examples", "snippet": vulnerable_requests_examples},
                              ])
    

def llmParse(cohere_api: CohereAPI):
    populateRAG(cohere_api)
    prompt = f"Generate a list of vulnerabilities by assessing the list of network requests provided and comparing them with common vulnerabilities. RETURN A SHORT DESCRIPTION OF THE VULNERABILITY AND THE RESPECTIVE NETWORK REQUEST. LOOK THROUGH ALL OF THE REQUESTS, PARTICULARLY THOSE WITH PASSWORDS AND CARD NUMBERS. MAKE SURE TO IDENTIFY VULNERABLE DATA BY REFERING TO EXAMPLES LABELLED WITH Security Vulnerability:"
    response = cohere_api.send_prompt(prompt=prompt)

    with open("results/vulnerabilities", "w") as f:
        f.write(str(response))

cohere_api = init_cohere(API_KEY)
llmParse(cohere_api)

# url = getUrl()

# if (url != "Invalid link"):
#     sql_injection.sql_injection(url)
#     xss.xss(url)
#     brute_force.brute_force(url)
#     directory_discovery.directory_discovery(url)
#     listenToNetwork(filename)



    # sql_injection_thread = Thread(target=sql_injection.sql_injection, args=[url])
    # sql_injection_thread.start()

    # xss_thread = Thread(target=xss.xss, args=[url])
    # xss_thread.start()
    
    # brute_force_thread = Thread(target=brute_force.brute_force, args=[url])
    # brute_force_thread.start()

    # directory_discovery_thread = Thread(target=directory_discovery.directory_discovery, args=[url])
    # directory_discovery_thread.start()

    # listenToNetwork(filename)
    # thread = Thread(target=listenToNetwork, args=[filename])
    # thread.start()
