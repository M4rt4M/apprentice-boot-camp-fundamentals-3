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
    let taxPrice;
    const {co2Emissions, fuelType} = vehicle;

    const taxPrices = {
      'Petrol' : {
        256: 2070,
        226: 1760,
        191: 1240,
        171: 830,
        151: 515,
        131: 205,
        111: 165,
        101: 145,
        91: 125,
        76: 105,
        51: 25,
        1: 10,
        0: 0
      },
      'Diesel' : {
        226: 2070,
        191: 1760,
        171: 1240,
        151: 830,
        131: 515,
        111: 205,
        101: 165,
        91: 145,
        76: 125,
        51: 105,
        1:25,
        0: 0
      }
    }
    
    const vehicleCo2 = Object.keys(taxPrices[fuelType])
            .sort((a,b) => b - a)
            .find(element => co2Emissions >= element);

    taxPrice = taxPrices[fuelType][vehicleCo2];

    return taxPrice;
    // throw new Error('You have to implement the method doSomething!');
  }
}

module.exports = { TaxCalculator: TaxCalculator }