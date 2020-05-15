#!/usr/bin/python3.8

import requests
import csv
from bs4 import BeautifulSoup

def get_countries_info():
    req = requests.get("https://www.worldometers.info/coronavirus/")

    if req.status_code == 200:
        countries_info = []

        bs = BeautifulSoup(req.text, "html.parser")
        table = bs.find_all(
            "table", attrs={"id": "main_table_countries_today"})
        tbody = table[0].find_all("tbody")
        trs = tbody[0].find_all("tr", attrs={"style": ""})

        for tr in trs[1:]:  # start with 1 item because firts item is for world info
            country = []
            tds = tr.find_all("td")

            for td in tds[1:]:  # start with 1 item because first item is for show rows
                text = td.text
                info = text.split("\n")[0]

                country.append(info)

            # this item will be remove because this is ALL tab in site's table and we don't need it
            country.pop(-1)
            countries_info.append(country)

        return countries_info

    else:
       raise RuntimeError("Your status code is %i" % (req.status_code))


def info_correction(countries_info):
    for country_info in countries_info:  # countries have list of country
        # country_info is a list and have info abaut county
        for idx, value in enumerate(country_info):
            if idx > 0:  # idx 0 is name of country
                if value == "":
                    country_info[idx] = "unknown"

                elif value[0] != "+":
                    try:
                        number = int(value)
                        country_info[idx] = number
                    except:
                        if "," in value:
                            if value[-1] == " ":
                                value = value.replace(" ", "")

                            number = int(value.replace(",", ""))
                            country_info[idx] = number

                        elif ("." in value) and (idx != 1):
                            number = int(value.replace(".", ""))
                            country_info[idx] = number
    return countries_info


def sort_informations(informations):
    # selection sort algorithm for information
    for i in range(len(informations)):
        minimum = i

        for j in range(i + 1, len(informations)):
            if int(informations[j][1]) > int(informations[minimum][1]):
                minimum = j

            informations[minimum], informations[i] = informations[i], informations[minimum]

    return informations


def write_in_csv(information, coloums, path):
    # save information in csv file each time run this script
    with open(f"{path}coronavirus.csv", "w") as corona_csv:
        information.insert(0, columns)

        csv_writer = csv.writer(corona_csv, delimiter=",")
        csv_writer.writerows(information)


# if you want the data to be save in csv file, first write the path of file in the path variable
# FOR EXAMPLE:
# path = "/home/believe/py/" or "D:\believe\py\"

file_path = "/home/mostafa/ProjectPy/Project/corona/"

columns = ["Countries", "Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered",
           "Active Cases", "Serious Critical", "Tot Cases", "Deaths", "Total Tests", "Tests", "Population"]

try:
    corona_info = get_countries_info()
    correct_info = info_correction(corona_info)
    sort_info = sort_informations(correct_info)

    write_in_csv(sort_info, columns, file_path)
except Exception as error:
    print(error)
