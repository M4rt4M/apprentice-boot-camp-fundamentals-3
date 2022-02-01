let TaxCalculator = class TaxCalculator {
  constructor(year, storyFour = false) {
    if (year === undefined) {
      let date = new Date();
      this.year = date.getFullYear();
    } else {
      this.year = year;
    }
    this.storyFour = storyFour;
  }

  getYear() {
    return this.year;
  }

  calculate2ndYear(vehicle) {
    const taxPricesfrom2ndYear = {
      'Petrol': 140,
      'Diesel': 140,
      'Electric': 0,
      'Alternative fuel': 130
    };
    if (this.storyFour) {
      const { fuelType } = vehicle; 
      let taxPrice;
      taxPrice = taxPricesfrom2ndYear[fuelType];
      return taxPrice;
    }
  }

  calculateTax(vehicle) {
    let taxPrice;
    const { co2Emissions, fuelType } = vehicle;

    const taxPrices = {
      'Petrol': {
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
        0: 0,
      },
      'Diesel': {
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
        1: 25,
        0: 0,
      },
      'Alternative fuel': {
        256: 2060,
        226: 1750,
        191: 1230,
        171: 820,
        151: 505,
        131: 195,
        111: 155,
        101: 135,
        91: 115,
        76: 95,
        51: 15,
        1: 0,
        0: 0,
      },
      'Electric': {
        0: 0,
      },
    };

    const vehicleCo2 = Object.keys(taxPrices[fuelType])
      .sort((a, b) => b - a)
      .find((element) => co2Emissions >= element);

    taxPrice = taxPrices[fuelType][vehicleCo2];

    return taxPrice;
    // throw new Error('You have to implement the method doSomething!');
  }
};

module.exports = { TaxCalculator: TaxCalculator }