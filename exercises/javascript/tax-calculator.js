let TaxCalculator = class TaxCalculator {
  constructor(year) {
    if (year === undefined) {
      let date = new Date();
      this.year = date.getFullYear();
    } else {
      this.year = year;
    }
  }

  getYear() {
    return this.year;
  }

  calculateTax(vehicle) {
    const {co2Emissions, fuelType} = vehicle;
    let taxPrice;
    const petrolPrice = {
      0: 0,
      1: 10,
      51: 25,
      76: 105,
      91: 125,
      101: 145,
      111: 165,
      131: 205,
      151: 515,
      171: 830,
      191: 1240,
      226: 1760,
      256: 2070
    }

    const vehicleCo2= Object.keys(petrolPrice).find(element => co2Emissions >= element);
    taxPrice=petrolPrice[vehicleCo2];

    return taxPrice;
  }
}

module.exports = { TaxCalculator: TaxCalculator }