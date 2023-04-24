import os
import sys
from collections import Counter
import requests
import matplotlib.pyplot as plt
from models import session, ActivityModel, PositionModel, SeniorityModel, LocalizationModel, TechnologyModel
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class RocketJobs:
    _url = "https://api.rocketjobs.pl/v2/user-panel/offers"
    _name = "RocketJobs"
    data = None
    overall_positions = 0
    city_counts = Counter()
    seniority_counts = Counter()
    skill_counts = Counter()
    remote_counts = 0

    def get_data(self):
        print("Getting data from RocketJobs...")
        params = {
            "page": "1",
            "sortBy": "published",
            "orderBy": "DESC",
            "perPage": "100",
        }
        headers = {
            "authority": "api.rocketjobs.pl",
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "origin": "https://rocketjobs.pl",
            "referer": "https://rocketjobs.pl/",
        }
        response = requests.get(self._url, timeout=10,
                                params=params, headers=headers)
        response.raise_for_status()
        self.data = response.json()
        print(self.data)

    def count_data(self):
        print("Counting data from RocketJobs...")
        for record in self.postings:
            if ('technology' in record):
                self.skill_counts[record['technology']] += 1
            if ('seniority' in record):
                for seniority_item in record['seniority']:
                    self.seniority_counts[seniority_item] += 1
        self.remote_counts = sum(
            1 for record in self.postings if record['location']['fullyRemote'])

    def print_stats(self):
        print(f"There are {self.overall_positions} overall positions.")
        print(f"There are {self.remote_counts} remote records.")
        for skill, count in self.skill_counts.items():
            print(f"Skills: there are {count} records for {skill}.")
        for seniority, count in self.seniority_counts.items():
            print(f"Seniority: there are {count} records for {seniority}.")

    def save_data(self):
        print("Saving data from RocketJobs to database...")
        session.add(ActivityModel(domain=self._name))
        session.commit()
