# Cost per Ounce/Ton Calculator for Mining Industry
# -------------------------------------------------
# Overview:
# This script calculates the cost to produce one unit (ounce or ton) of a mineral.
# It helps mining companies determine the efficiency and effectiveness of their extraction processes.
#
# Desired Value:
# Lower values are desired as they indicate a more efficient and cost-effective extraction process. 
# However, it's also important to compare this cost with the current market price of the mineral to ensure profitability.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual production costs and extraction quantities should be inputted.

class CostPerUnitCalculator:
    def __init__(self, total_production_cost, total_extraction_volume, unit='ton'):
        # Convert values from millions representation to actual values
        self.total_production_cost = total_production_cost * 10**6  # total cost in dollars
        self.total_extraction_volume = total_extraction_volume * 10**6  # in ounces or tons based on unit
        self.unit = unit

    def calculate_cost_per_unit(self):
        """Calculate and return the cost per unit (ounce/ton)."""
        return self.total_production_cost / self.total_extraction_volume

    def display_cost_per_unit(self):
        """Display the calculated cost per unit."""
        cost_per_unit = self.calculate_cost_per_unit()
        print(f"Cost per {self.unit.capitalize()}: ${cost_per_unit:.2f}")

# Hard-coded values
sample_total_production_cost = 10.00  # Example: Total cost to produce the mineral is $10 million
sample_total_extraction_volume = 2.00  # Example: Company extracted 2 million tons of the mineral
unit_type = 'ton'  # This can be changed to 'ounce' if needed

cost_calculator = CostPerUnitCalculator(sample_total_production_cost, sample_total_extraction_volume, unit_type)
cost_calculator.display_cost_per_unit()
