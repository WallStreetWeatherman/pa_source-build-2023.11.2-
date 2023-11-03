# Monthly/Annual Recurring Revenue (MRR/ARR)
# ------------------------------------------
# Overview:
# MRR and ARR represent the predictable revenue streams from ongoing subscriptions. 
# This is essential for businesses with a subscription model as it provides insight 
# into the stability and predictability of revenue. Growing MRR and ARR values indicate 
# increasing subscription numbers or higher revenue per customer, suggesting business health.
#
# Desired Value:
# A consistently growing MRR/ARR is favorable as it signifies business growth and stability. 
# It's essential to monitor the growth rate and compare it with churn rate (rate at which 
# customers cancel their subscriptions) to get a comprehensive view of subscription business health.

def calculate_arr(mrr):
    """Calculate the Annual Recurring Revenue (ARR) based on Monthly Recurring Revenue (MRR)."""
    return mrr * 12

# Hard-coded values (These are just sample values and should be replaced with real-world data)
sample_mrr = 5.0  # Monthly recurring revenue of $5,000,000, represented as 5.0

# Calculating ARR from the sample MRR value
sample_arr = calculate_arr(sample_mrr)

print(f"Monthly Recurring Revenue (MRR) is: ${sample_mrr:.2f} million")
print(f"Annual Recurring Revenue (ARR) is: ${sample_arr:.2f} million")
