# Cart Abandonment Rate Calculator
# --------------------------------
# Overview:
# Cart Abandonment Rate is a crucial metric in the e-commerce space. It represents the percentage
# of online shoppers who add items to their shopping cart but leave without completing the purchase.
#
# Formula: Cart Abandonment Rate = (Number of Abandoned Carts / Number of Initiated Carts) * 100
#
# Desired Value:
# A lower Cart Abandonment Rate is more desirable as it means more shoppers are completing their purchases.
# A high rate can indicate potential problems in the checkout process, pricing, or overall user experience.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual shopping cart data should be input.

class CartAbandonmentRateCalculator:
    def __init__(self, num_abandoned_carts, num_initiated_carts):
        self.num_abandoned_carts = num_abandoned_carts
        self.num_initiated_carts = num_initiated_carts

    def calculate_rate(self):
        """Calculate Cart Abandonment Rate."""
        return (self.num_abandoned_carts / self.num_initiated_carts) * 100

    def display_rate(self):
        """Display the calculated Cart Abandonment Rate."""
        rate = self.calculate_rate()
        print(f"Cart Abandonment Rate: {rate:.2f}%")

# Hard-coded values for demonstration:
# Example: 
# num_abandoned_carts = 600 represents 600 shoppers who abandoned their carts.
# num_initiated_carts = 1000 represents 1,000 shoppers who added items to their carts.
num_abandoned_carts = 600
num_initiated_carts = 1000

calculator = CartAbandonmentRateCalculator(num_abandoned_carts, num_initiated_carts)
calculator.display_rate()
