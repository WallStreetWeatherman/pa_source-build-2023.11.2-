# ESG Water Usage Calculator
# --------------------------------
# Overview:
# Environmental, Social, and Governance (ESG) metrics assess a company's behavior in environmental sustainability.
# Water Usage is a critical ESG metric that quantifies the amount of water a company consumes during its operations.
# This helps in assessing the company's water sustainability practices.
#
# Desired Value:
# A lower Water Usage value is more desirable, indicating efficient and sustainable water consumption.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual water usage data should be input.

class WaterUsageCalculator:
    def __init__(self, water_sources, usage_data):
        """
        Args:
        water_sources (list): List of water sources being used, e.g., 'groundwater', 'river', 'recycled', etc.
        usage_data (dict): Dictionary with water sources as keys and water consumed as values (in liters).
        """
        self.water_sources = water_sources
        self.usage_data = usage_data

    def calculate_total_usage(self):
        """Calculate total water usage."""
        total_usage = sum(self.usage_data.values())
        # Convert total usage so that 1 million liters becomes 1.00, 10 million liters becomes 10.00, etc.
        return total_usage / 1000000

    def display_usage(self):
        """Display the calculated Water Usage."""
        total_usage = self.calculate_total_usage()
        print(f"Total Water Usage: {total_usage:.2f} (in Million Liters)")

# Hard-coded values for demonstration:
water_sources = ['groundwater', 'river', 'recycled']

usage_data = {
    'groundwater': 600000,  # Liters
    'river': 300000,       # Liters
    'recycled': 100000     # Liters
}

calculator = WaterUsageCalculator(water_sources, usage_data)
calculator.display_usage()
