#!/usr/bin/python3.8

import unittest
import warnings
import corona.corona_virus as cv
import corona.corona_plot as cp



class TestCoronaPlot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            corona_info  = cv.get_countries_info()
            correct_info = cv.info_correction(corona_info)

            cls.sort_info = cv.sort_informations(correct_info)
            cls.file_path = cv.create_file_path()

        cv.write_in_csv(cls.sort_info)
    
    def test_get_total_data(self):
        total_data = cp.get_total_data(self.file_path)

        self.assertIsInstance(total_data, tuple)
        self.assertIsInstance(total_data[0], dict)
        self.assertIsInstance(total_data[1], dict)
    
    def test_plot_data(self):
        total_case, total_death = cp.get_total_data(self.file_path)

        cp.plot_data(total_case, total_death)
        cp.plot_data(total_case, total_death, save_svg_img_in_path=self.file_path)
        cp.plot_data(total_case, total_death, save_svg_img_in_path=self.file_path + ".svg")

        with self.assertRaises(TypeError):
            cp.plot_data(total_case, total_death, save_svg_img_in_path=True)
            cp.plot_data(total_case, total_death, save_svg_img_in_path=False)

            cp.plot_data(total_case, total_death, save_svg_img_in_path=12)
            cp.plot_data(total_case, total_death, save_svg_img_in_path=12.21)

            cp.plot_data(total_case, total_death, save_svg_img_in_path=list())
            cp.plot_data(total_case, total_death, save_svg_img_in_path=[1, 2, 3])

            cp.plot_data(total_case, total_death, save_svg_img_in_path=dict())
            cp.plot_data(total_case, total_death, save_svg_img_in_path={"a": 1, "b": 2, "c": 3})

            cp.plot_data(total_case, total_death, save_svg_img_in_path=tuple())
            cp.plot_data(total_case, total_death, save_svg_img_in_path=(1, 2, 3))


if __name__ == "__main__":
    unittest.main()







