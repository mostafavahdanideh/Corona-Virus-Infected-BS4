#!/usr/bin/python3.8


import matplotlib.pyplot as plt
import csv


def get_total_data(csv_file_address):
    with open(f"{csv_file_address}.csv", "r") as csv_file:
        total_death_data = {}
        total_case_data = {}
        countries = list(csv.reader(csv_file))[1:6]  # 0 item are our colums

        for country_data in countries:
            country_name = country_data[0]

            country_total_case = int(country_data[1])
            country_total_death = int(country_data[3])

            total_case_data[country_name] = country_total_case
            total_death_data[country_name] = country_total_death

    return total_case_data, total_death_data


def plot_data(total_case, tota_death, save_svg_img_in_path=None):

    countries_name = list(total_case.keys())
    number_of_cases = list(total_case.values())
    number_of_deaths = list(tota_death.values())

    fig, axs = plt.subplots(1, 2, figsize=(12, 12))

    axs[0].bar(countries_name, number_of_cases, color="orange")
    axs[1].bar(countries_name, number_of_deaths, color="orange")
    axs[0].set_title("TOTAL CASES", color="green")
    axs[1].set_title("TOTAL DEATHS", color="green")

    fig.suptitle(
        "CORONA PLOTS FOR THE TOP OF FIVE COUNTRIES IN THE WORLD", color="red")

    if isinstance(save_svg_img_in_path, str):
        if ".svg" not in save_svg_img_in_path:
            save_svg_img_in_path += '.svg'

        plt.savefig(save_svg_img_in_path)

    elif save_svg_img_in_path == None:
        plt.show()

    else:
        raise TypeError(
            "save_svg_img_in_path param must be None for just show plot or path for save plot")

