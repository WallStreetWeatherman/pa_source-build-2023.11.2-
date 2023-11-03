# Lifetime Value (LTV)
# ---------------------
# Overview:
# LTV calculates the predicted net profit associated with the entire future relationship 
# with a customer. It helps businesses understand the long-term value of a customer 
# and assess whether they are making a profit or loss in acquiring new customers when 
# compared with the Customer Acquisition Cost (CAC).
#
# Desired Value:
# A higher LTV is generally favorable as it indicates that the customer is expected 
# to bring in more profit over their entire relationship with the business. When used 
# in conjunction with CAC, an LTV that is substantially higher than CAC suggests the 
# business has a healthy profit margin on its customer acquisition strategy.

def calculate_ltv(average_purchase_value, purchase_frequency, customer_lifespan, gross_margin):
    """Calculate the Lifetime Value (LTV) of a customer."""
    ltv = average_purchase_value * purchase_frequency * customer_lifespan * gross_margin
    return ltv

# Hard-coded values (These are just sample values and should be replaced with real-world data)
sample_average_purchase_value = 0.1  # Average purchase value of $100,000, represented as 0.1
sample_purchase_frequency = 4       # Customers make an average of 4 purchases a year
sample_customer_lifespan = 5        # Average lifespan of a customer is 5 years
sample_gross_margin = 0.2           # Company retains 20% of the revenue after direct costs

ltv_value = calculate_ltv(sample_average_purchase_value, 
                          sample_purchase_frequency, 
                          sample_customer_lifespan, 
                          sample_gross_margin)

print(f"Predicted Lifetime Value (LTV) of a customer is: ${ltv_value:.2f}")
