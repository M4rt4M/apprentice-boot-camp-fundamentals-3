using System;

namespace TaxCalculator.Tests
{
    [Obsolete("DO NOT MAKE ANY CHANGES TO THIS CLASS - IT IS JUST HERE TO KEEP THE TESTS HAPPY TO BEGIN WITH. DON'T BE LAZY - WRITE YOUR OWN NEW TAXCALCULATOR CLASS")]
    public sealed class DummyTaxCalculator : TaxCalculator
    {
        public override int CalculateTax(Vehicle vehicle)
        {
            return -1;
        }
    }
}
