# Ore Reserve & Mineral Resource Estimates Calculator for Mining Industry
# ----------------------------------------------------------------------
# Overview:
# This script calculates the estimated value of a mining company's ore reserves and mineral resources.
# It provides insight into the potential value of the minerals the company has access to extract.
#
# Desired Value:
# Higher values indicate a more significant potential for revenue generation from ore extraction and processing.
# However, it's essential to also consider extraction costs, market prices for the minerals, and other factors.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual mineral resource data and current market prices should be inputted.

class OreReserveEstimator:
    def __init__(self, ore_volume, avg_mineral_content, mineral_market_price):
        # Convert values from millions representation to actual values
        self.ore_volume = ore_volume * 10**6  # in tons
        self.avg_mineral_content = avg_mineral_content  # percentage (0-100)
        self.mineral_market_price = mineral_market_price * 10**6  # price per ton

    def calculate_estimated_value(self):
        """Calculate and return the estimated value of the ore reserves."""
        extractable_mineral_volume = self.ore_volume * (self.avg_mineral_content / 100)
        return extractable_mineral_volume * self.mineral_market_price

    def display_estimated_value(self):
        """Display the calculated value of the ore reserves."""
        estimated_value = self.calculate_estimated_value()
        print(f"Estimated Value of Ore Reserves: ${estimated_value:.2f}")

# Hard-coded values
sample_ore_volume = 5.00  # Example: Company has access to 5 million tons of ore
sample_avg_mineral_content = 10  # Example: The ore contains 10% of the desired mineral
sample_mineral_market_price = 0.5  # Example: The mineral sells for $0.5 million per ton

ore_estimator = OreReserveEstimator(sample_ore_volume, sample_avg_mineral_content, sample_mineral_market_price)
ore_estimator.display_estimated_value()
