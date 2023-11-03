# Cap Rate (Capitalization Rate)
# ------------------------------
# Overview:
# The Cap Rate, often used in real estate investment analysis, measures the rate of return 
# on a real estate investment property based on the expected income the property will generate.
# It's calculated by dividing the Net Operating Income (NOI) by the current market value of the property.
#
# Desired Value:
# A higher Cap Rate suggests a better potential return on investment, but it might also indicate 
# higher risk. It's important to compare Cap Rates within similar real estate markets and 
# consider other factors like property condition, location, and growth potential.

def calculate_cap_rate(net_operating_income, property_value):
    """Calculate the Cap Rate for a real estate property."""
    return net_operating_income / property_value

# Hard-coded values (These are sample values and should be replaced with real-world data)
sample_net_operating_income = 7.5  # Net Operating Income of $7,500,000, represented as 7.5
sample_property_value = 75.0      # Property value of $75,000,000, represented as 75.0

# Calculating Cap Rate from the sample values
sample_cap_rate = calculate_cap_rate(sample_net_operating_income, sample_property_value)

print(f"Net Operating Income is: ${sample_net_operating_income:.2f} million")
print(f"Property Value is: ${sample_property_value:.2f} million")
print(f"Cap Rate is: {sample_cap_rate*100:.2f}%")
