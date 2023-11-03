# Content Production & Licensing Costs Tracker
# -------------------------------------------
# Overview:
# This script keeps a record of costs associated with producing original content 
# or licensing content from third parties. By tracking these costs, businesses can 
# assess the financial feasibility and impact of their content strategies.
#
# Desired Value:
# The desired value for content production and licensing costs varies. In general,
# a company should aim for a balanced approach, ensuring high-quality content 
# without overspending. A lower value indicates cost efficiency, but quality and 
# content variety should not be compromised.
# 
# Note: This script uses hard-coded values for demonstration. In real-world applications,
# actual cost data should be inputted.

class ContentCostTracker:
    def __init__(self, production_costs, licensing_costs):
        self.production_costs = production_costs
        self.licensing_costs = licensing_costs

    def display_costs_over_years(self):
        """Display costs for each year."""
        print("Content Production & Licensing Costs Summary:\n")
        for year, (prod_cost, lic_cost) in enumerate(zip(self.production_costs, self.licensing_costs), 1):
            total_cost = prod_cost + lic_cost
            print(f"Year {year}:")
            print(f"\tProduction Costs: ${prod_cost:.2f} million")
            print(f"\tLicensing Costs: ${lic_cost:.2f} million")
            print(f"\tTotal Costs: ${total_cost:.2f} million\n")

    def average_annual_cost(self):
        """Calculate the average annual cost over the years."""
        total_prod_cost = sum(self.production_costs)
        total_lic_cost = sum(self.licensing_costs)
        average_prod_cost = total_prod_cost / len(self.production_costs)
        average_lic_cost = total_lic_cost / len(self.licensing_costs)
        return average_prod_cost, average_lic_cost

# Hard-coded values
# Costs over 5 years in millions. Example: 5.00 means $5,000,000.
production_costs = [5.00, 5.50, 6.00, 6.50, 7.00]  # Represents production costs over 5 years.
licensing_costs = [3.00, 3.20, 3.50, 3.80, 4.00]   # Represents licensing costs over 5 years.

tracker = ContentCostTracker(production_costs, licensing_costs)
tracker.display_costs_over_years()

avg_prod_cost, avg_lic_cost = tracker.average_annual_cost()
print(f"Average Annual Production Cost: ${avg_prod_cost:.2f} million")
print(f"Average Annual Licensing Cost: ${avg_lic_cost:.2f} million")
