"""
Main module.
"""

from domains.justjoinit import JustJoinIt


def main():
    """
    Main function.
    """
    just_join_it = JustJoinIt()
    just_join_it.get_data()
    just_join_it.count_data()
    just_join_it.draw_plot()
    just_join_it.print_stats()


if __name__ == '__main__':
    main()
