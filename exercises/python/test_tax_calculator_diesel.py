import datetime
import unittest

from dummy_tax_calculator import DummyTaxCalculator
from vehicle import Vehicle


class TaxCalculatorDieselFuelTest(unittest.TestCase):
    def setUp(self):
        self.tax_calculator = DummyTaxCalculator()
        self.FIRST_OF_JAN_2019 = datetime.datetime.date(2019, 1, 1)

    def test_first_years_tax_for__diesel_0_grams_co2(self):
        vehicle = Vehicle(0, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(0, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for__diesel_1_to_50_grams_co2(self):
        vehicle = Vehicle(50, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(25, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for__diesel_51_to_75_grams_co2(self):
        vehicle = Vehicle(75, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(105, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for__diesel_76_to_90_grams_co2(self):
        vehicle = Vehicle(90, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(125, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for__diesel_91_to_100_grams_co2(self):
        vehicle = Vehicle(100, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(145, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for__diesel_101_to_110_grams_co2(self):
        vehicle = Vehicle(110, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(165, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for__diesel_111_to_130_grams_co2(self):
        vehicle = Vehicle(130, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(205, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for__diesel_131_to_150_grams_co2(self):
        vehicle = Vehicle(150, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(515, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for__diesel_151_to_170_grams_co2(self):
        vehicle = Vehicle(170, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(830, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for__diesel_171_to_190_grams_co2(self):
        vehicle = Vehicle(1240, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(820, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for__diesel_191_to_225_grams_co2(self):
        vehicle = Vehicle(225, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(1760, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for__diesel_226_to_255_grams_co2(self):
        vehicle = Vehicle(255, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(2070, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for__diesel_over_225_grams_co2(self):
        vehicle = Vehicle(256, "DIESEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(2070, self.tax_calculator.calculate_tax(vehicle))



if __name__ == '__main__':
    unittest.main()


