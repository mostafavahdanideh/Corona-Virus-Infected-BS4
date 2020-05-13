#!/usr/bin/python3.8


import requests
from bs4 import BeautifulSoup
import csv

#if you want the data to be save in csv file, first write the path of file in the path variable
#FOR EXAMPLE:
#path = "/home/believe/py/" or "D:\believe\py\"

file_path = "/home/mostafa/ProjectPy/Project/corona/"

columns = ["Countries", "Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered",
           "Active Cases", "Serious Critical", "Tot Cases", "Deaths", "Total Tests", "Tests"]


try:
    req = requests.get("https://www.worldometers.info/coronavirus/")

    if req.status_code == 200:
        countries_info = []
        bs = BeautifulSoup(req.text, "html.parser")
        table = bs.find_all(
            "table", attrs={"id": "main_table_countries_today"})
        tbody = table[0].find_all("tbody")
        trs = tbody[0].find_all("tr", attrs={"style": ""})

        for tr in trs:
            country = []
            tds = tr.find_all("td")

            for td in tds:
                text = td.text
                info = text.split("\n")[0]
                country.append(info)

            # this item will be remove becuase this is ALL tab in site's table and we don't need it
            country.pop(-1)
            countries_info.append(country)

        for country_info in countries_info:
            for idx, value in enumerate(country_info[1:]):
                real_idx = idx + 1

                if value == "":
                    country_info[real_idx] = "unknown"

                elif (value != "") and (value[0] != "+"):
                    if "," in value:
                        number = int(value.replace(",", ""))
                        country_info[real_idx] = number
                    elif "." in value:
                        number = int(value.replace(".", ""))
                        country_info[real_idx] = number

        # selection sort algorithm for countries
        for i in range(len(countries_info)):
            minimum = i

            for j in range(i + 1, len(countries_info)):
                if int(countries_info[j][1]) > int(countries_info[minimum][1]):
                    minimum = j

            countries_info[minimum], countries_info[i] = countries_info[i], countries_info[minimum]

        # save information in csv file each time run this script
        with open(f"{file_path}coronavirus.csv", "w") as corona_csv:
            countries_info.insert(0, columns)
            csv_writer = csv.writer(corona_csv, delimiter=",")
            csv_writer.writerows(countries_info)

        #at the end we have dataset of corona in the world :))))))))
    else:
        print(req.status_code)

except Exception as error:
    print(error)
