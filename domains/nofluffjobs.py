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
            self._url, timeout=10, json=payload, params=params)
        response.raise_for_status()
        self.data = response.json()
        print(self.data)
