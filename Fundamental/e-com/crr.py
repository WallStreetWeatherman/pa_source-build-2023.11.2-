# Customer Retention Rate Calculator
# ----------------------------------
# Overview:
# Customer Retention Rate (CRR) indicates the proportion of customers that a business
# manages to retain over a given period. It is a vital metric for understanding customer
# loyalty and the effectiveness of marketing and customer service efforts.
#
# Formula: CRR = [(E - N) / S] * 100
# Where:
# E = Number of customers at the end of a period
# N = Number of new customers acquired during the period
# S = Number of customers at the start of the period
#
# Desired Value:
# A high CRR is usually more desirable as it indicates strong customer loyalty and satisfaction.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# it's essential to use actual business data.

class CRRCalculator:
    def __init__(self, start_customers, end_customers, new_customers):
        self.start_customers = start_customers
        self.end_customers = end_customers
        self.new_customers = new_customers

    def calculate_crr(self):
        """Calculate Customer Retention Rate."""
        return ((self.end_customers - self.new_customers) / self.start_customers) * 100

    def display_crr(self):
        """Display the calculated CRR value."""
        crr = self.calculate_crr()
        print(f"Customer Retention Rate: {crr:.2f}%")

# Hard-coded values for demonstration:
# Example: 
# start_customers = 1000 represents 1,000 customers at the beginning of a period.
# end_customers = 900 represents 900 customers at the end of that period.
# new_customers = 50 represents 50 new customers acquired during the period.
start_customers = 1000
end_customers = 900
new_customers = 50

calculator = CRRCalculator(start_customers, end_customers, new_customers)
calculator.display_crr()
