# webscraping

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import requests

url = 'https://infopark.in/companies/company/thrissur'
response = requests.get(url,verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

h3_tags = soup.find_all('h3')
for tag in h3_tags:
    print(tag.text)


# email scrapping

import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://infopark.in/companies/company/thrissur"
r = requests.get(url, verify=False)
soup = BeautifulSoup(r.content, 'html.parser')

# Find email addresses using a regular expression
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Find all text on the page
all_text = soup.get_text()


email_addresses = re.findall(email_pattern, all_text)


for email in email_addresses:
    print(email)

p_tags = soup.find_all('p')
for tag in p_tags:
    print(tag.text)



