const { DummyTaxCalculator } = require('./dummy-tax-calculator');
const { Vehicle } = require('../vehicle');
const { FuelType } = require('../fuel-type');

describe.skip('Tax calculator on vehicles after the first year', () => {
  let taxCalculator = new DummyTaxCalculator();
  let FIRST_OF_APRIL_2017 = new Date(2017, 4, 1);

  it('subsequent years tax for petrol', () => {
    const vehicle = new Vehicle(206, FuelType.PETROL, FIRST_OF_APRIL_2017, 20000);
    expect(taxCalculator.calculateTax(vehicle)).toBe(140);
  })

  it('subsequent years tax for electric', () => {
    const vehicle = new Vehicle(206, FuelType.ELECTRIC, FIRST_OF_APRIL_2017, 20000);
    expect(taxCalculator.calculateTax(vehicle)).toBe(0);
  })

  it('subsequent years tax for alternative fuel', () => {
    const vehicle = new Vehicle(206, FuelType.ALTERNATIVE_FUEL, FIRST_OF_APRIL_2017, 20000);
    expect(taxCalculator.calculateTax(vehicle)).toBe(130);
  })
})
