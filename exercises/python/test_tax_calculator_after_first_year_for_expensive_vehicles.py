import datetime
import unittest
from dummy_tax_calculator import  DummyTaxCalculator
from vehicle import Vehicle


class TaxCalculatorAfterFirstYearForExpensiveVehiclesTest(unittest.TestCase):
	def setUp(self):
		self.tax_calculator = DummyTaxCalculator()
		self.FIRST_OF_APRIL_2017 = datetime.date(2017, 4, 1)

	def test_subsequent_years_tax_for_petrol_if_over_40k(self):
		vehicle = Vehicle(206, "PETROL", self.FIRST_OF_APRIL_2017, 50000)
		self.assertEqual(450, self.tax_calculator.calculate_tax(vehicle))

	def test_subsequent_years_tax_for_electric_if_over_40k(self):
		vehicle = Vehicle(206, 'ELECTRIC', self.FIRST_OF_APRIL_2017, 50000)
		self.assertEqual(310, self.tax_calculator.calculate_tax(vehicle))

	def test_subsequent_years_tax_for_alternative_fuel_if_over_40k(self):
		vehicle = Vehicle(206, "ALTERNATIVE FUEL", self.FIRST_OF_APRIL_2017, 50000)
		self.assertEqual(440, self.tax_calculator.calculate_tax(vehicle))


if __name__ == '__main__':
    unittest.main()