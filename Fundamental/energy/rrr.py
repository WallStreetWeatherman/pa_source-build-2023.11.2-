# Reserve Replacement Ratio (RRR)
# -------------------------------
# Overview:
# The Reserve Replacement Ratio measures the amount of proved reserves added to a company's
# reserve base during the year, relative to the amount of oil and gas produced. It is a key 
# indicator of an oil & gas company's ability to maintain or grow its production levels.
#
# Formula:
#   RRR = (Net Increase in Proved Reserves during the Year) / (Oil & Gas Production for the Year)
#
# Desired Value:
# A RRR greater than 100% means the company is adding reserves at a faster rate than it is 
# producing, which is a positive sign for future production potential. Conversely, a RRR below 
# 100% can indicate the company is producing reserves faster than it is finding or acquiring 
# new ones, which could be a concern for long-term sustainability.

def compute_rrr(net_increase_reserves, annual_production):
    """Calculate the Reserve Replacement Ratio."""
    return net_increase_reserves / annual_production

# Hard-coded values (expressed in terms of "million barrels" where 1 million barrels is 1.00, 10 million barrels is 10.00, etc.)
net_increase_reserves = 15.00  # Net increase in proved reserves during the year (in million barrels)
annual_production = 10.00      # Total oil & gas production for the year (in million barrels)

# Calculating RRR from the sample values
rrr = compute_rrr(net_increase_reserves, annual_production)

print(f"Net Increase in Reserves: {net_increase_reserves} million barrels")
print(f"Annual Production: {annual_production} million barrels")
print(f"Reserve Replacement Ratio: {rrr*100:.2f}%")
