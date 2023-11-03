# Yield per Acre Calculator for Agriculture
# -----------------------------------------
# Overview:
# This script calculates the Yield per Acre, which is a measure of how much of a specific crop 
# is harvested per unit of land (acre). It provides insights into the productivity of land and 
# can be useful in comparing the efficiency of different farming techniques or the fertility of different lands.
#
# Desired Value:
# For farmers and agricultural businesses, a higher Yield per Acre is often desirable as it indicates
# more efficient land use and potentially higher profitability. However, the optimal yield can vary 
# based on the specific crop and local conditions.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual harvest amounts and land sizes should be inputted.

class YieldCalculator:
    def __init__(self, total_harvest, total_acres):
        # Convert values from millions representation to actual values
        self.total_harvest = total_harvest * 10**6  # total amount of crop harvested (e.g., in bushels)
        self.total_acres = total_acres * 10**6  # total land size in acres

    def calculate_yield_per_acre(self):
        """Calculate and return the Yield per Acre."""
        yield_per_acre = self.total_harvest / self.total_acres
        return yield_per_acre

    def display_yield(self):
        """Display the calculated Yield per Acre."""
        ypa = self.calculate_yield_per_acre()
        print(f"Yield per Acre: {ypa:.2f} bushels/acre")  # Adjust the unit "bushels" as needed

# Hard-coded values
sample_total_harvest = 2.00  # Example: Total harvested amount is 2 million bushels
sample_total_acres = 1.00  # Example: Total land size is 1 million acres

yield_calculator = YieldCalculator(sample_total_harvest, sample_total_acres)
yield_calculator.display_yield()
