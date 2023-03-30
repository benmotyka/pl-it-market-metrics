"""
This is scrapper for justjoinit.
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/", timeout=5)
response.raise_for_status()

document = BeautifulSoup(response.content, 'html.parser')

print(document)
