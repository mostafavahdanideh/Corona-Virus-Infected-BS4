#!/usr/bin/python3.8


import corona_virus as cv
from corona_plot import get_total_data, plot_data


def run_script():
    try:
        corona_info = cv.get_countries_info()
        correct_info = cv.info_correction(corona_info)
        sort_info = cv.sort_informations(correct_info)

        cv.write_in_csv(sort_info)

        total_case, total_death = get_total_data(cv.create_file_path())

        plot_data(total_case, total_death, cv.create_file_path() + ".svg")

    except Exception as error:
        print("this error for {} and message is {}".format(error.__class__, error))


if __name__ == "__main__":
    run_script()
