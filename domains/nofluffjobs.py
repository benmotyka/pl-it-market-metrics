"""
Scrapper for justjoinit.
"""

from collections import Counter
import requests
import matplotlib.pyplot as plt


class NoFluffJobs:
    """
    Class for scrapping data from NoFluffJobs.
    """
    _url = "https://nofluffjobs.com/api/search/posting"
    data = None
    overall_positions = 0
    city_counts = Counter()
    seniority_counts = Counter()
    skill_counts = Counter()
    remote_counts = 0

    def get_data(self):
        """
        Returns data from website
        """
        payload = {'rawSearch': ''}
        params = {
            "page": "1",
            "salaryCurrency": "PLN",
            "salaryPeriod": "month",
            "region": "pl",
        }
        response = requests.post(
            self._url, timeout=15, json=payload, params=params)
        response.raise_for_status()
        self.data = response.json()

    def count_data(self):
        """
        Counts the data
        """
        self.overall_positions = self.data['totalCount']
        for record in self.data['postings']:
            if ('technology' in record):
                self.skill_counts[record['technology']] += 1
            if ('seniority' in record):
                for seniority_item in record['seniority']:
                    self.seniority_counts[seniority_item] += 1
        self.remote_counts = sum(
            1 for record in self.data['postings'] if record['location']['fullyRemote'])

    def print_stats(self):
        """
        Prints the stats.
        """
        print(f"There are {self.overall_positions} overall positions.")
        print(f"There are {self.remote_counts} remote records.")
        for skill, count in self.skill_counts.items():
            print(f"Skills: there are {count} records for {skill}.")
        for seniority, count in self.seniority_counts.items():
            print(f"Seniority: there are {count} records for {seniority}.")
