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

import requests
import scraper
import sys
import brute_force
import sql_injection
import xss
import directory_discovery
from llm import CohereAPI
from dotenv import load_dotenv
import os
from threading import Event

network_filename = "results/network_outputs.txt"
client_code_filename = "results/client_code.txt"
API_KEY = os.getenv("COHERE_API_KEY")
api_url = "http://127.0.0.1:3001/api/tests"

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
    
def listenToNetwork(network_fname, client_code_fname, url, cohere_api):
    open(network_fname, 'w').close()
    open(client_code_fname, 'w').close()
    while True:
        s = time.time()

        # if time.time()-s < 10:
        #     time.sleep(0.2)
        # Event().wait(7)
        time.sleep(2)

        with open(client_code_filename, "w", encoding="charmap", errors="replace") as f:
            f.write(str(scraper.getClientCode()))
        
        scraper.print_network_logs_and_client_code(network_fname, client_code_fname, url)

        llmParseNetworkRequests(cohere_api)

        findSolutions(cohere_api)

        # time.sleep(3)

        # llmParseClientCode(cohere_api)

        # llm_thread = Thread

def findSolutions(cohere_api: CohereAPI):
    with open("results/network_vulnerabilities.txt", 'r') as f1:
        c1 = f1.read()
    with open("results/results_brute_force.txt", 'r') as f2:
        c2 = f2.read()
    with open("results/results_directory_discovery.txt", 'r') as f3:
        c3 = f3.read()
    with open("results/results_sql_injection.txt", 'r') as f4:
        c4 = f4.read()
    with open("results/results_xss.txt", 'r') as f5:
        c5 = f5.read()

    cohere_api.set_documents([
                                {"title": "network_vulnerabilities", "snippet": c1},
                                {"title": "brute_force", "snippet": c2},
                                {"title": "directory_discovery", "snippet": c3},
                                {"title": "sql_injection", "snippet": c4},
                                {"title": "xss", "snippet": c5},
                                # {"title": "vulnerable_requests_examples", "snippet": vulnerable_requests_examples},
                              ])
    prompt = f'Provide a list of remedies for these vulnerabilities. KEEP IT SHORT AND CONCISE. IF YOU HAVE NO SUGGESTIONS SAY NO CURRENT RECOMMENDATIONS VULNERABILITIES FOR FIXES'
    response = cohere_api.send_prompt(prompt=prompt)

    # with open("results/remedies.txt", "w") as f:
    #     f.write(response)

    issues = ""
    files = ["results/network_vulnerabilities.txt", "results/results_brute_force.txt", "results/results_directory_discovery.txt", "results/results_sql_injection.txt", "results/results_xss.txt"]

    for fname in files:
        with open(fname, "r") as f:
            issues += f.read()

    headers = {
        "Content-Type": "application/json"
    }

    requests.patch(api_url, json={
        "recommendations": response,
        "issues": issues
    },
        headers=headers,
    )

def populateNetworkRAG(cohere_api: CohereAPI):
    with open("results/network_outputs.txt", 'r') as f:
        network_outputs = f.read()
    with open("utils/network.txt", 'r') as f:
        vulnerable_requests_examples = f.read()
        
    cohere_api.set_documents([
                                {"title": "network_outputs", "snippet": network_outputs},
                                # {"title": "vulnerable_requests_examples", "snippet": vulnerable_requests_examples},
                              ])
    

def llmParseNetworkRequests(cohere_api: CohereAPI):
    populateNetworkRAG(cohere_api)
    prompt = f"Generate a list of vulnerabilities by assessing the network requests. RETURN A SHORT DESCRIPTION OF THE VULNERABILITY AND THE RESPECTIVE NETWORK REQUEST IN ONE LINE. Example: Password Vulnerable: (username: dhisah, password: dskad)  Give a list of vulnerabilities. MAKE SURE TO IDENTIFY VULNERABLE DATA ESPECIALLY PASSWORDS AND CARDS. LOOK THROUGH ALL OF THE REQUESTS. IF YOU ENCOUNTER ONE, DO NOT FORGET IT. DO NOT OUTPUT ANYTHING OTHER THAN VULNERABILITIES"
    # return
    response = cohere_api.send_prompt(prompt=prompt)

    with open("results/network_vulnerabilities.txt", "w") as f:
        f.write(str(response))

    with open("results/client_code.txt", 'r') as f:
        client_code = f.read()
    with open("utils/client_code.txt", 'r') as f:
        vulnerable_client_code_examples = f.read()
        
    cohere_api.set_documents([
                                {"title": "client_code", "snippet": client_code},
                                # {"title": "vulnerable_client_code_examples", "snippet": vulnerable_client_code_examples},
                              ])

def llmParseClientCode(cohere_api: CohereAPI):
    populateClientCodeRAG(cohere_api)
    prompt = f"Generate a list of vulnerabilities by assessing the HTML code provided and comparing them with common vulnerabilities. RETURN A SHORT DESCRIPTION OF THE VULNERABILITY AND THE RESPECTIVE CODE LINE IN THE FOLLOWING FORMAT: <Short description> <code line>. LOOK THROUGH ALL CODE, PARTICULARLY THOSE WITH API_KEYS. MAKE SURE TO IDENTIFY VULNERABLE DATA BY REFERING TO EXAMPLES LABELLED WITH Security Vulnerability:"

    # return
    response = cohere_api.send_prompt(prompt=prompt)

    with open("results/code_vulnerabilities.txt", "w") as f:
        f.write(str(response))


# cohere_api = init_cohere(API_KEY)
# llmParse(cohere_api)

url = getUrl()
# url = "http://localhost:4000"

if (url != "Invalid link"):
    cohere_api = init_cohere(API_KEY)
    init_selenium(url)

    sql_injection.sql_injection(url)
    xss.xss(url)
    brute_force.brute_force(url)
    directory_discovery.directory_discovery(url)
    listenToNetwork(network_filename, client_code_filename, url, cohere_api)



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
