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
