#!/usr/bin/python3.8


import matplotlib.pyplot as plt
import csv

def get_total_data(csv_file_address):
    with open(csv_file_address, "r") as csv_file:
        total_death_data = {}
        total_case_data = {}
        countries = list(csv.reader(csv_file))[1:6]  # 0 item are our colums

        for country_data in countries:
            country_name = country_data[0]

            country_total_case  = int(country_data[1])
            country_total_death = int(country_data[3])

            total_case_data[country_name]  = country_total_case
            total_death_data[country_name] = country_total_death

    return total_case_data, total_death_data



def plot_data(total_case, tota_death, save_svg_img=True):

    countries_name = list(total_case.keys())
    number_of_cases = list(total_case.values())
    number_of_deaths = list(tota_death.values())

    fig, axs = plt.subplots(1, 2, figsize=(15, 15))

    axs[0].bar(countries_name, number_of_cases, color="orange")
    axs[1].bar(countries_name, number_of_deaths, color="orange")
    axs[0].set_title("TOTAL CASES", color="green")
    axs[1].set_title("TOTAL DEATHS", color="green")

    fig.suptitle("CORONA PLOTS FOR THE TOP OF FIVE COUNTRIES IN THE WORLD", color="red")

    if save_svg_img:
        plt.savefig('coronavirus.svg')
        print("Done, Your svg plot saved in current location.")
    else:
        plt.show()








