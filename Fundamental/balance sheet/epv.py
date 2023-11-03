# Earnings Power Value (EPV) Analysis
# ------------------------------------
# Overview:
# The Earnings Power Value (EPV) is a valuation technique that evaluates a company's ability to generate earnings, 
# independent of the current state of its finances. 
# Ideally, for a deep value investor, you'd want the EPV to be significantly higher than the current stock price, 
# suggesting the stock may be undervalued.
# 
# Formula:
# EPV = Adjusted Earnings / Cost of Capital

class Company:
    def __init__(self, name, adjusted_earnings, cost_of_capital):
        self.name = name
        self.adjusted_earnings = adjusted_earnings  # In $ million format: 1.00 means $1 million
        self.cost_of_capital = cost_of_capital  # As a percentage, e.g., 0.07 for 7%
        
        # Validate the data
        self._validate_data()

    def _validate_data(self):
        if self.adjusted_earnings <= 0:
            raise ValueError("Adjusted Earnings must be positive.")
        if not (0 < self.cost_of_capital < 1):
            raise ValueError("Cost of Capital should be between 0 and 1 (0% to 100%).")
    
    def compute_epv(self):
        return self.adjusted_earnings / self.cost_of_capital

    def display_epv(self):
        try:
            epv = self.compute_epv()
            print(f"Earnings Power Value (EPV) for {self.name}: ${epv:.2f} million")
            
            # Factors and Scenarios that Might Influence EPV
            print("\nFactors and Scenarios that Could Influence EPV:")
            print("1. Economic Conditions: A recession could lead to reduced earnings.")
            print("2. Competition: Increased competition could erode market share and earnings.")
            print("3. Technological Changes: Can either boost or hinder earnings depending on adaptability.")
            print("4. Regulatory Environment: Changes in regulation can significantly affect the cost structure.")
            print("5. Capital Allocation: Effective use of capital can significantly boost earnings.")
            
        except Exception as e:
            print(f"An error occurred while processing the data for {self.name}. Error: {str(e)}")

# Hardcoded values for two companies
company_A = Company("Company A", 10.00, 0.07)  # $10 million earnings and 7% cost of capital
company_B = Company("Company B", 25.00, 0.05)  # $25 million earnings and 5% cost of capital

# Display EPVs
company_A.display_epv()
print("--------------------")
company_B.display_epv()

# Comparing EPVs
if company_A.compute_epv() > company_B.compute_epv():
    print(f"\n{company_A.name} has a higher Earnings Power Value, indicating a potentially more attractive investment opportunity.")
elif company_A.compute_epv() < company_B.compute_epv():
    print(f"\n{company_B.name} has a higher Earnings Power Value, signaling a potentially better earnings generation capability.")
else:
    print(f"\nBoth {company_A.name} and {company_B.name} have the same Earnings Power Value, suggesting similar earnings capabilities.")
    