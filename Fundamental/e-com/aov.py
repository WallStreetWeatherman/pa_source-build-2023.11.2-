# Average Order Value (AOV) Calculator
# -----------------------------------
# Overview:
# Average Order Value (AOV) gives insights into the mean value of the orders placed 
# by customers over a given period. It is a significant metric for retail or e-commerce businesses.
#
# Formula: AOV = Total Revenue / Number of Orders
#
# Desired Value:
# A high AOV is generally more desirable, indicating that customers are spending more
# with each purchase. However, it's crucial to ensure strategies to increase AOV 
# don't negatively impact the frequency of purchases.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# it's essential to input actual sales data.

class AOVCalculator:
    def __init__(self, total_revenue, number_of_orders):
        # Convert the given revenue into the desired format (e.g., 1.00 for 1 million)
        self.total_revenue = total_revenue / 1000000
        self.number_of_orders = number_of_orders

    def calculate_aov(self):
        """Calculate Average Order Value."""
        return self.total_revenue / self.number_of_orders

    def display_aov(self):
        """Display the calculated AOV value."""
        aov = self.calculate_aov()
        print(f"Average Order Value (in millions): ${aov:.2f}")

# Hard-coded values for demonstration:
# Example: 
# total_revenue = 5000000 represents $5,000,000 in total revenue.
# number_of_orders = 1000 represents 1,000 total orders made.
total_revenue = 5000000
number_of_orders = 1000

calculator = AOVCalculator(total_revenue, number_of_orders)
calculator.display_aov()
