const { TaxCalculator } = require('../tax-calculator');

/**
* @deprecated
*/
let DummyTaxCalculator = class DummyTaxCalculator extends TaxCalculator {
  constructor() {
    super();
  }
  calculateTax(vehicle) {
    return -1;
  }
}

module.exports = {
  DummyTaxCalculator: DummyTaxCalculator
}