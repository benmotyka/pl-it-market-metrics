from collections import Counter
import requests


class NoFluffJobs:
    _url = "https://nofluffjobs.com/api/search/posting"
    data = None
    postings = []
    overall_positions = 0
    seniority_counts = Counter()
    skill_counts = Counter()
    remote_counts = 0

    def get_data(self):
        """
        NoFluffJobs API is paginated, so we need to get positions from all of the pages
        """

        print("Getting data from NoFluffJobs...")

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
        result = response.json()

        pages = result['totalPages']
        self.postings.extend(result['postings'])
        self.overall_positions = result['totalCount']

        # Iterate over other pages
        for page in range(2, pages):
            params = {
                "page": str(page),
                "salaryCurrency": "PLN",
                "salaryPeriod": "month",
                "region": "pl",
            }
            print(f"Getting page {page} of {pages} for NoFluffJobs...")
            response = requests.post(
                self._url, timeout=15, json=payload, params=params)
            response.raise_for_status()
            result = response.json()
            self.postings.extend(result['postings'])

    def count_data(self):
        print("Counting data from NoFluffJobs...")
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
