"""
This is scrapper for justjoinit.
"""

from collections import Counter
import requests
# from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

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

# Filter the Counter object to only include values greater than 10
filtered_counter = {key: value for key, value in city_counts.items() if value > 10}

# Sort the dictionary by values in descending order
sorted_data = sorted(filtered_counter.items(), key=lambda x: x[1], reverse=True)

# Extract the keys and values into separate lists
cities = [city for city, value in sorted_data]
counts = [value for city, value in sorted_data]

# Plot the values
fig, ax = plt.subplots()
ax.bar([x[0] for x in sorted_data], [x[1] for x in sorted_data])
ax.set_xlabel('City')
ax.set_ylabel('Number of job offers')
ax.set_title('Job offers by city')
plt.xticks(rotation=90)
plt.show()

for level, count in seniority_counts.items():
    print(f"Seniority: there are {count} records for {level}.")

for kind, count in kind_counts.items():
    print(f"Kind: there are {count} records for {kind}.")

print(f"There are {remote_counts} remote records.")

print(city_counts)
print(dict(city_counts))
