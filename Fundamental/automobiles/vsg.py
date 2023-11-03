# Vehicle Sales Growth Calculator
# -------------------------------
# Overview:
# This script calculates the growth rate of vehicle unit sales on a year-over-year basis.
# Growth in sales can be a sign of increasing demand or successful marketing, whereas a 
# decrease might indicate market saturation, increased competition, or other challenges.
#
# Desired Value:
# Generally, a higher year-over-year growth rate is desired as it indicates increased sales and 
# potentially expanding market share. However, extremely high growth can be unsustainable 
# and may signal a future downturn.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual vehicle sales data for the respective years should be inputted.

class VehicleSalesGrowthCalculator:
    def __init__(self, last_year_sales, current_year_sales):
        # Convert sales from millions representation to actual values
        # For instance, 1.00 means 1 million vehicles or 1,000,000 vehicles
        self.last_year_sales = last_year_sales * 10**6
        self.current_year_sales = current_year_sales * 10**6

    def calculate_sales_growth(self):
        """Calculate and return the year-over-year growth rate of vehicle sales."""
        growth = ((self.current_year_sales - self.last_year_sales) / self.last_year_sales) * 100 if self.last_year_sales != 0 else 0
        return growth

    def display_sales_growth(self):
        """Display the year-over-year growth rate of vehicle sales."""
        growth_rate = self.calculate_sales_growth()
        print(f"Year-over-Year Vehicle Sales Growth Rate is: {growth_rate:.2f}%")

# Hard-coded values
sample_last_year_sales = 1.50  # Example: 1.5 million vehicles sold last year
sample_current_year_sales = 1.80  # Example: 1.8 million vehicles sold this year

sales_growth_calculator = VehicleSalesGrowthCalculator(sample_last_year_sales, sample_current_year_sales)
sales_growth_calculator.display_sales_growth()