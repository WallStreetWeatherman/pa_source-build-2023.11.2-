# Gross Rent Multiplier (GRM)
# ---------------------------
# Overview:
# The Gross Rent Multiplier (GRM) is a valuation metric commonly used in real estate to assess
# the ratio between the property's price and its gross rental income. It offers a quick way
# to compare the relative value of properties.
# GRM is calculated by dividing the property's price by its gross annual rental income.
#
# Desired Value:
# A lower GRM can indicate a more favorable investment opportunity, as the property may be 
# undervalued compared to its rental income. Conversely, a higher GRM might suggest that 
# the property is overpriced. However, GRM should be used in conjunction with other metrics 
# and local market data to provide a comprehensive view.

def calculate_grm(property_price, gross_annual_rental_income):
    """Calculate the Gross Rent Multiplier."""
    return property_price / gross_annual_rental_income

# Hard-coded values (These are sample values and should be replaced with real-world data)
sample_property_price = 200.0  # Property price of $200,000,000, represented as 200.0
sample_gross_annual_rental_income = 20.0  # Gross annual rental income of $20,000,000, represented as 20.0

# Calculating GRM from the sample values
sample_grm = calculate_grm(sample_property_price, sample_gross_annual_rental_income)

print(f"Property Price is: ${sample_property_price:.2f} million")
print(f"Gross Annual Rental Income is: ${sample_gross_annual_rental_income:.2f} million")
print(f"Gross Rent Multiplier (GRM) is: {sample_grm:.2f}")
