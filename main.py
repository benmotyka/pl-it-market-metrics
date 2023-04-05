"""
Main module.
"""

from domains.justjoinit import JustJoinIt
from domains.nofluffjobs import NoFluffJobs


def main():
    just_join_it = JustJoinIt()
    just_join_it.get_data()
    just_join_it.count_data()
    just_join_it.draw_plot()
    just_join_it.print_stats()

    no_fluff_jobs = NoFluffJobs()
    no_fluff_jobs.get_data()
    no_fluff_jobs.count_data()
    no_fluff_jobs.print_stats()


if __name__ == '__main__':
    main()
