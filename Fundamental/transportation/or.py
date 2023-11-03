# Operating Ratio Calculator for Railway Industry
# --------------------------------------------------------------
# Overview:
# The operating ratio is a metric that measures the operational efficiency of a company.
# It represents the operating expenses as a percentage of revenue. For the railway industry,
# a lower operating ratio indicates that the company is operating more efficiently.
#
# Desired Value:
# Lower operating ratios are generally better, indicating more efficient operations. 
# However, extremely low values might be an indicator of underinvestment in essential areas.
# It's a balance that railway companies need to strike.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual revenue and operating expense data should be inputted.

class OperatingRatioCalculator:
    def __init__(self, revenue, operating_expenses):
        # Convert revenue and operating expenses from millions representation to actual values
        # For instance, 1.00 means 1 million dollars
        self.revenue = revenue * 10**6
        self.operating_expenses = operating_expenses * 10**6

    def calculate_ratio(self):
        """Calculate and return the Operating Ratio."""
        if self.revenue == 0:
            return 0.0  # Return 0 if revenue is 0 to avoid division by zero
        return (self.operating_expenses / self.revenue) * 100

    def display_ratio(self):
        """Display the calculated Operating Ratio."""
        ratio = self.calculate_ratio()
        print(f"Operating Ratio: {ratio:.2f}%")

# Hard-coded values
sample_revenue = 10.00  # Example: Revenue generated is $10 million
sample_operating_expenses = 7.50  # Example: Operating expenses are $7.5 million

ratio_calculator = OperatingRatioCalculator(sample_revenue, sample_operating_expenses)
ratio_calculator.display_ratio()
