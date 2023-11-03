# Customer Acquisition Cost (CAC)
# --------------------------------
# Overview:
# CAC measures the cost to acquire a customer. It's an essential metric, especially for businesses 
# with a strong online presence or those operating on a subscription-based model. CAC provides 
# insights into how much the company is spending to get a new customer, which can then be compared 
# to the lifetime value of the customer to assess the company's profitability.
#
# Desired Value:
# A lower CAC is generally favorable as it means the company spends less to acquire a new customer. 
# However, it's essential to consider the quality of the acquired customers and the value they bring 
# to the company. It's also crucial to compare CAC values across the industry to get a relative 
# understanding of a company's efficiency in acquiring customers.

def calculate_cac(marketing_spending, acquired_customers):
    """Calculate the Customer Acquisition Cost (CAC)."""
    cac = marketing_spending / acquired_customers
    return cac

# Hard-coded values (These are just sample values and should be replaced with real-world data)
sample_marketing_spending = 5.00  # $5 million spent on marketing, represented as 5.00
sample_acquired_customers = 2500  # 2,500 new customers acquired

cac_value = calculate_cac(sample_marketing_spending, sample_acquired_customers)

print(f"Customer Acquisition Cost (CAC) is: ${cac_value:.2f} per customer")
