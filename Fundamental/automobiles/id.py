# Automotive: Inventory Days Calculator
# -------------------------------------
# Overview:
# This script calculates the Inventory Days, which indicates how many days, on average, 
# it takes for an automotive company to sell its entire inventory. It's a measure of 
# inventory management and sales efficiency.
#
# Desired Value:
# A lower Inventory Days value is generally more desirable, as it suggests the company 
# can quickly turn over its inventory and may have strong sales. However, extremely low 
# numbers might indicate stockouts and potential sales loss. Conversely, higher values 
# may suggest slow-moving inventory or overstock, which can tie up capital and increase 
# carrying costs.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual financial data for the respective company should be inputted.

class InventoryDaysCalculator:
    def __init__(self, annual_cost_of_goods_sold, ending_inventory_value):
        # Convert financial values from millions representation to actual values
        # For instance, 1.00 means 1 million dollars or $1,000,000
        self.annual_cogs = annual_cost_of_goods_sold * 10**6
        self.ending_inventory_value = ending_inventory_value * 10**6

    def calculate_inventory_days(self):
        """Calculate and return the Inventory Days."""
        if self.annual_cogs == 0:
            return float('inf')  # Return infinity if COGS is 0 to avoid division by zero
        daily_cogs = self.annual_cogs / 365
        return self.ending_inventory_value / daily_cogs

    def display_inventory_days(self):
        """Display the calculated Inventory Days."""
        days = self.calculate_inventory_days()
        if days == float('inf'):
            print("Inventory Days: Infinity (Due to zero COGS)")
        else:
            print(f"Inventory Days: {days:.2f} days")

# Hard-coded values
sample_annual_cogs = 100.00  # Example: $100 million annual cost of goods sold
sample_ending_inventory_value = 10.00  # Example: $10 million ending inventory value

inventory_days_calculator = InventoryDaysCalculator(sample_annual_cogs, sample_ending_inventory_value)
inventory_days_calculator.display_inventory_days()
