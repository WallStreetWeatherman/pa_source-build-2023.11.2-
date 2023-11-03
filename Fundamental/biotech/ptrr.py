# Price to Research Ratio (P/R Ratio)
# -----------------------------------
# Overview:
# The Price to Research Ratio (P/R Ratio) provides insight into how much investors 
# are willing to pay for every dollar the company spends on research and development (R&D). 
# It compares the market value (or market capitalization) of a company to its R&D expenditures.
#
# Desired Value:
# A lower P/R ratio might indicate that the company's stock is undervalued given its R&D efforts.
# A higher ratio can mean that the stock might be overvalued relative to its R&D spending.
#
# Note: This script calculates the P/R ratio based on the provided hard-coded values.

def price_to_research(market_cap, rd_expenditure):
    """Calculate the Price to Research Ratio."""
    if rd_expenditure == 0:
        raise ValueError("R&D Expenditure cannot be zero.")
    return market_cap / rd_expenditure

# Hard-coded values (expressed in millions where 1 million dollars is 1.00, 10 million is 10.00, etc.)
# Company's market capitalization (in million dollars)
market_cap = 100.00  

# Company's R&D expenditure (in million dollars)
rd_expenditure = 5.00  

# Calculating the Price to Research Ratio
try:
    pr_ratio = price_to_research(market_cap, rd_expenditure)
    print(f"Price to Research Ratio (P/R Ratio): {pr_ratio:.2f}")
except ValueError as e:
    print(e)

