# LTV/CAC Ratio
# ---------------
# Overview:
# LTV/CAC ratio indicates the relationship between the lifetime value of a customer 
# and the cost to acquire that customer. A ratio greater than 1 indicates that a customer 
# is expected to generate more revenue than it costs to acquire them, signifying a 
# successful business model. Conversely, a ratio less than 1 can be a red flag.
#
# Desired Value:
# A higher LTV/CAC ratio is generally favorable, indicating a higher return on investment 
# in customer acquisition. Typically, a ratio of 3 or higher is considered good, but this 
# can vary by industry. Always consider the industry average and long-term sustainability 
# when analyzing this ratio.

def calculate_ltv_cac_ratio(ltv, cac):
    """Calculate the LTV/CAC ratio."""
    return ltv / cac

# Hard-coded values (These are just sample values and should be replaced with real-world data)
sample_ltv = 3.5  # Lifetime value of $3,500,000, represented as 3.5
sample_cac = 1.0  # Customer acquisition cost of $1,000,000, represented as 1.0

ltv_cac_ratio = calculate_ltv_cac_ratio(sample_ltv, sample_cac)

print(f"LTV/CAC Ratio is: {ltv_cac_ratio:.2f}")
