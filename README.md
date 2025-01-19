# CyberAgent

## Installation

Selenium installation:
```
pip install selenium
pip install selenium-wire
```

## Motivation

CyberAgent aims to create an AI-powered cybersecurity developer tool to identify security vulnerabilities. Developers can enter the url a web-app repository, prompting the app to provide information about potential vulnerabilities and security recommendations.

## Description

Our project combines simple web attacks such as SQL injections, network request interceptions, and brute force attacks with a Cohere large language model to scan through a web repository and inform the developer of vulnerabilities. Raw security data is sent to the Cohere LLM, which returns a readable analysis of threats and recommendations that are sent to the frontend and displayed to the user.

The backend server was implemented using Python and Flask, and Selenium was used to scrape repository data. The frontend web interface was created using React and JavaScript.

## Challenges

Significant challenges were learning how to integrate the large language model into our project by optimizing the model for our specific uses and communicating with the LLM API.

## What we accomplished

We successfully scanned and caught several vulnerabilities from the OWASP Juice Shop, an insecure web app created for testing cybersecurity hacks. We were also able to successfully obtain output from a Cohere LLM to display on our user interface.