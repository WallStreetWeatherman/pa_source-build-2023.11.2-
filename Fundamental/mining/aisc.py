# All-In Sustaining Costs (AISC) Calculator for Gold Industry
# ----------------------------------------------------------
# Overview:
# This script calculates the All-In Sustaining Costs (AISC) which is a comprehensive measure of the 
# cost of producing gold. It takes into account not only the direct costs of mining but also sustaining 
# capital and General & Administrative (G&A) expenses.
#
# Desired Value:
# Ideally, companies want the AISC to be lower, which indicates efficient operations and better 
# potential for profitability, especially when compared to the current market price of gold. 
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual production costs and expenses should be inputted.

class AISCCalculator:
    def __init__(self, production_costs, sustaining_capital, ga_expenses):
        # Convert values from millions representation to actual values
        self.production_costs = production_costs * 10**6  # total production costs in dollars
        self.sustaining_capital = sustaining_capital * 10**6  # sustaining capital in dollars
        self.ga_expenses = ga_expenses * 10**6  # G&A expenses in dollars

    def calculate_aisc(self):
        """Calculate and return the All-In Sustaining Costs (AISC)."""
        total_costs = self.production_costs + self.sustaining_capital + self.ga_expenses
        return total_costs

    def display_aisc(self):
        """Display the calculated AISC."""
        aisc = self.calculate_aisc()
        print(f"All-In Sustaining Costs (AISC): ${aisc/10**6:.2f} million")

# Hard-coded values
sample_production_costs = 100.00  # Example: Total production costs are $100 million
sample_sustaining_capital = 5.00  # Example: Sustaining capital is $5 million
sample_ga_expenses = 2.00  # Example: G&A expenses are $2 million

aisc_calculator = AISCCalculator(sample_production_costs, sample_sustaining_capital, sample_ga_expenses)
aisc_calculator.display_aisc()
