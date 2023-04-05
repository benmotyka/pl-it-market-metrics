from collections import Counter
import requests
import matplotlib.pyplot as plt


class JustJoinIt:
    _url = "https://justjoin.it/api/offers"
    data = None
    overall_positions = 0
    city_counts = Counter()
    seniority_counts = Counter()
    skill_counts = Counter()
    remote_counts = 0

    def get_data(self):
        """
        JustJoinIt has a very simple API that returns ALL of the offers, no need for pagination/filtering/authentication
        """
        response = requests.get(self._url, timeout=10)
        response.raise_for_status()
        self.data = response.json()

    def count_data(self):
        for record in self.data:
            self.city_counts[record['city']] += 1
            self.seniority_counts[record['experience_level']] += 1
            self.skill_counts[record['marker_icon']] += 1
        self.remote_counts = sum(1 for record in self.data if record['remote'])
        self.overall_positions = len(self.data)

    def draw_plot(self):
        min_job_offers_threshold = 10

        # Filter the Counter object to only include values greater than job_offers_threshold
        city_counts = {key: value for key,
                       value in self.city_counts.items() if value > min_job_offers_threshold}

        # Sort the dictionary by values in descending order
        sorted_data = sorted(city_counts.items(),
                             key=lambda x: x[1], reverse=True)

        _, ax = plt.subplots()
        ax.bar([x[0] for x in sorted_data], [x[1] for x in sorted_data])
        ax.set_xlabel('City')
        ax.set_ylabel('Number of job offers')
        ax.set_title('Job offers by city')
        for i, v in enumerate([x[1] for x in sorted_data]):
            ax.text(i, v, str(v), ha='center', va='bottom')
        plt.xticks(rotation=90)
        plt.show()

    def print_stats(self):
        print(f"There are {self.overall_positions} overall positions.")
        print(f"There are {self.remote_counts} remote records.")
        for level, count in self.seniority_counts.items():
            print(f"Seniority: there are {count} records for {level}.")
        for skill, count in self.skill_counts.items():
            print(f"Skills: there are {count} records for {skill}.")
        for city, count in self.city_counts.items():
            print(f"Localization: there are {count} records for {city}.")
