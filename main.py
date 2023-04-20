from domains.justjoinit import JustJoinIt
from domains.nofluffjobs import NoFluffJobs
from models import session, ActivityModel


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

    activity = ActivityModel(domain="justjoinit")
    session.add(activity)
    session.commit()


if __name__ == '__main__':
    main()
