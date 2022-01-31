import datetime
import unittest

from dummy_tax_calculator import DummyTaxCalculator
from vehicle import Vehicle


class TaxCalculatorAfterFirstYearTest(unittest.TestCase):
    def setUp(self):
        self.tax_calculator = DummyTaxCalculator()
        self.FIRST_OF_APRIL_2017 = datetime.date(2017, 4, 1)

    def test_subsequent_years_tax_for(self):
        vehicle = Vehicle(206, "PETROL", self.FIRST_OF_APRIL_2017, 20000)
        self.assertEqual(140, self.tax_calculator.calculate_tax(vehicle))

    def test_subsequent_years_tax_for_electric(self):
        vehicle = Vehicle(206, "ELECTRIC", self.FIRST_OF_APRIL_2017, 20000)
        self.assertEqual(0, self.tax_calculator.calculate_tax(vehicle))

    def test_subsequent_years_tax_for_alternative_fuel(self):
        vehicle = Vehicle(206, "ALTERNATIVE_FUEL", self.FIRST_OF_APRIL_2017, 20000)
        self.assertEqual(130, self.tax_calculator.calculate_tax(vehicle))


if __name__ == '__main__':
    unittest.main()
