let Vehicle = class Vehicle {
  constructor(co2Emissions, fuelType, dateOfFirstRegistration, listPrice) {
    this.co2Emissions = co2Emissions;
    this.fuelType = fuelType;
    this.dateOfFirstRegistration = dateOfFirstRegistration;
    this.listPrice = listPrice;
  }

}

module.exports = { Vehicle: Vehicle }