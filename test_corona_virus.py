#!/usr/bin/python3.8

import unittest
import warnings
from unittest.mock import patch
import corona.corona_virus as cv
import os



class TestCoronaVirus(unittest.TestCase):
    
    def test_create_file_path(self):
        file_path = cv.create_file_path()

        self.assertEqual(file_path, "/home/mostafa/ProjectPy/GitHub Clone/CoronaVirus/corona/coronavirus")

    def test_get_countries_info(self):
        #mocked for requests.get when request was fail and raise RuntimeError
        with self.assertRaises(RuntimeError):
            with patch("corona.corona_virus.requests.get") as mocked_get:
                mocked_get.return_value.status_code = 503

                _countries = cv.get_countries_info()
                mocked_get.assert_called_with("https://www.worldometers.info/coronavirus/")

        #mocked for requests.get when request was successful and BeautifulSoup parser
        with patch("corona.corona_virus.requests.get") as mocked_get:
            with patch("corona.corona_virus.BeautifulSoup") as mocked_bs:
                mocked_get.return_value.status_code = 200
                mocked_get.return_value.text = "Success"

                _countries = cv.get_countries_info()
                mocked_get.assert_called_with("https://www.worldometers.info/coronavirus/")
                mocked_bs.assert_called_with(mocked_get.return_value.text, "html.parser")
        
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            countries_info = cv.get_countries_info()

            for country_info in countries_info:
                self.assertEqual(len(country_info), 13)

            self.assertGreaterEqual(len(countries_info), 50)
            self.assertLessEqual(len(countries_info), 100)
    
    def test_write_in_csv(self):
        countries_info      = cv.get_countries_info()
        correct_info        = cv.info_correction(countries_info)
        sorted_informations = cv.sort_informations(correct_info)


        cv.write_in_csv(sorted_informations)
        cv.write_in_csv(sorted_informations, csv_file_path=cv.create_file_path)
        cv.write_in_csv(sorted_informations, csv_file_path=cv.create_file_path() + ".csv")
        cv.write_in_csv(sorted_informations, csv_file_path="/home/mostafa/corona.csv")

        with self.assertRaises(RuntimeError):
            cv.write_in_csv(sorted_informations, "/home/mostafa/corona.txt")
            cv.write_in_csv(sorted_informations, "/home/mostafa/corona.cs")
            cv.write_in_csv(sorted_informations, "/home/mostafa/corona.cvs")
            cv.write_in_csv(sorted_informations, "/home/mostafa/coronacsv")
            cv.write_in_csv(sorted_informations, "/home/mostafa/corona")
            cv.write_in_csv(sorted_informations, "/home/mostafa/")
            cv.write_in_csv(sorted_informations, "/home/mostafa/ProjectPy")
            cv.write_in_csv(sorted_informations, csv_file_path=cv.create_file_path())
        
        with self.assertRaises(TypeError):
            cv.write_in_csv(sorted_informations, True)
            cv.write_in_csv(sorted_informations, False)

            cv.write_in_csv(sorted_informations, 12)
            cv.write_in_csv(sorted_informations, 12.22)

            cv.write_in_csv(sorted_informations, dict())
            cv.write_in_csv(sorted_informations, {"a": 1, "b": 2, "c": 3})

            cv.write_in_csv(sorted_informations, list())
            cv.write_in_csv(sorted_informations, [1, 2, 3])

            cv.write_in_csv(sorted_informations, tuple())
            cv.write_in_csv(sorted_informations, (1, 2, 3))

if __name__ == "__main__":
    unittest.main()



