# Private Market Value (PMV) Analysis
# -----------------------------------
# Overview:
# PMV estimates what a company might be worth if it were acquired in a private transaction.
# This is often calculated by looking at the valuations of recent acquisitions of similar companies 
# in the same industry and applying relevant multipliers.
#
# Desired Value:
# The value itself is subjective. A higher PMV might indicate that the company is undervalued in the public market.
# Investors would typically want this number to be higher than the company's current market cap, indicating potential undervaluation.

class Company:
    def __init__(self, name, financial_metric):
        self.name = name
        self.financial_metric = financial_metric  # This could be EBITDA, sales, net income, etc.

    def estimate_pmv(self, comparable_acquisitions):
        """
        Estimate the PMV based on comparable acquisitions.
        
        Parameters:
        - comparable_acquisitions: List of tuples where each tuple contains
          (name of acquired company, financial metric of acquired company, acquisition price)
        """
        multipliers = [acquisition[2] / acquisition[1] for acquisition in comparable_acquisitions]
        average_multiplier = sum(multipliers) / len(multipliers)
        
        return self.financial_metric * average_multiplier

# Example: Let's say the financial metric we're using is EBITDA

# Hardcoded values for our target company's EBITDA
target_company = Company("TargetCo", 10)  # $10 million EBITDA

# Hardcoded values for comparable acquisitions:
# Each tuple consists of (acquired company's name, EBITDA of acquired company, acquisition price)
comparable_acquisitions = [
    ("CompanyA", 8, 90),   # Acquired for $90 million with EBITDA of $8 million
    ("CompanyB", 12, 130), # Acquired for $130 million with EBITDA of $12 million
    ("CompanyC", 9, 100)   # Acquired for $100 million with EBITDA of $9 million
]

estimated_pmv = target_company.estimate_pmv(comparable_acquisitions)
print(f"The estimated Private Market Value (PMV) for {target_company.name} is ${estimated_pmv:.2f} million.")
