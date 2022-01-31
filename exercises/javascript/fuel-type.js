let FuelType = class FuelType {
  static get PETROL() {
    return 'Petrol';
  }

  static get DIESEL() {
    return 'Diesel';
  }

  static get ELECTRIC() {
    return 'Electric';
  }

  static get ALTERNATIVE_FUEL() {
    return 'Alternative fuel';
  }
}

module.exports = {
  FuelType: FuelType
}