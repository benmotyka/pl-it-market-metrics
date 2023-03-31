"""
This is scrapper for justjoinit.
"""

from collections import Counter
import requests
# from bs4 import BeautifulSoup

response = requests.get("https://justjoin.it/api/offers/", timeout=10)
response.raise_for_status()

data = response.json()

overall_positions = len(data)

city_counts = Counter()
seniority_counts = Counter()
kind_counts = Counter()

for record in data:
    city_counts[record['city']] += 1
    seniority_counts[record['experience_level']] += 1
    kind_counts[record['marker_icon']] += 1

remote_counts = sum(1 for record in data if record['remote'])

for city, count in city_counts.items():
    print(f"Localization: there are {count} records for {city}.")

for level, count in seniority_counts.items():
    print(f"Seniority: there are {count} records for {level}.")

for kind, count in kind_counts.items():
    print(f"Kind: there are {count} records for {kind}.")

print(f"There are {remote_counts} remote records.")

print(city_counts)
print(dict(city_counts))
