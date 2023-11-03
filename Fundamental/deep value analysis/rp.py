# Replacement Value Analysis
# --------------------------
# Overview:
# Replacement value is a valuation method that calculates the cost to replace a company's 
# tangible assets. This can serve as a floor value for the company. If the company's 
# market capitalization is below the replacement value of its assets, the company might 
# be considered undervalued.
#
# Desired Value:
# A company's market capitalization should ideally be above its replacement value. 
# If it's below, it suggests potential undervaluation, signaling a potential buying 
# opportunity for value investors.

class Company:
    def __init__(self, name, market_cap):
        self.name = name
        self.market_cap = market_cap
        self.assets = []

    def add_asset(self, asset_name, replacement_cost):
        """Add a tangible asset and its replacement cost."""
        self.assets.append((asset_name, replacement_cost))

    def compute_replacement_value(self):
        """Calculate the total replacement value of all assets."""
        return sum(asset[1] for asset in self.assets)

    def display_analysis(self):
        replacement_value = self.compute_replacement_value()
        print(f"Replacement Value for {self.name}: ${replacement_value:.2f} million.")
        print(f"Market Capitalization of {self.name}: ${self.market_cap:.2f} million.")
        
        if self.market_cap < replacement_value:
            print(f"{self.name} appears to be undervalued based on replacement value analysis.")
        else:
            print(f"{self.name} is trading above its asset replacement value.")

# Hardcoded values for a hypothetical company
tech_inc = Company("TechInc", 180.00)  # e.g., $180 million market capitalization

# Add tangible assets and their replacement costs to TechInc
tech_inc.add_asset("Factory & Machinery", 100.00)  # e.g., $100 million replacement cost
tech_inc.add_asset("Real Estate", 90.00)           # e.g., $90 million replacement cost

# Display Replacement Value analysis for TechInc
tech_inc.display_analysis()
