import datetime
import unittest

from dummy_tax_calculator import DummyTaxCalculator
from vehicle import Vehicle


class TaxCalculatorAlternativeFuelTest(unittest.TestCase):
    def setUp(self):
        self.tax_calculator = DummyTaxCalculator()
        self.FIRST_OF_APRIL_2017 = datetime.datetime.date(2019, 1, 1)

    def test_first_years_tax_for_alternative_fuel_0_grams_co2(self):
        vehicle = Vehicle(0, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(0, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_alternative_fuel_1_to_50_grams_co2(self):
        vehicle = Vehicle(50, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(0, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_alternative_fuel_51_to_75_grams_co2(self):
        vehicle = Vehicle(75, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(15, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_alternative_fuel_76_to_90_grams_co2(self):
        vehicle = Vehicle(90, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(95, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_alternative_fuel_91_to_100_grams_co2(self):
        vehicle = Vehicle(100, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(115, self.tax_calculator.calculate_tax(vehicle))


    def test_first_years_tax_for_alternative_fuel_101_to_110_grams_co2(self):
        vehicle = Vehicle(110, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(135, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_alternative_fuel_111_to_130_grams_co2(self):
        vehicle = Vehicle(130, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(155, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_alternative_fuel_131_to_150_grams_co2(self):
        vehicle = Vehicle(150, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(195, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_alternative_fuel_151_to_170_grams_co2(self):
        vehicle = Vehicle(170, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(505, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_alternative_fuel_171_to_190_grams_co2(self):
        vehicle = Vehicle(190, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(820, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_alternative_fuel_191_to_225_grams_co2(self):
        vehicle = Vehicle(225, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(1230, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_alternative_fuel_226_to_255_grams_co2(self):
        vehicle = Vehicle(255, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(1750, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_alternative_fuel_over_225_grams_co2(self):
        vehicle = Vehicle(256, "ALTERNATIVE_FUEL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(2060, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_electric(self):
        vehicle = Vehicle(0, "ELECTRIC", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(0, self.tax_calculator.calculate_tax(vehicle))


if __name__ == '__main__':
    unittest.main()


