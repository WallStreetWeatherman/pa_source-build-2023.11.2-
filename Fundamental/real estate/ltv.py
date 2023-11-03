# Loan-to-Value Ratio (LTV)
# -------------------------
# Overview:
# The Loan-to-Value (LTV) ratio is used predominantly in the context of property purchases.
# It calculates the percentage of the property's value that's being financed by a loan.
# LTV is calculated by dividing the loan amount by the property's appraised value.
#
# Desired Value:
# Lower LTV ratios suggest that the borrower has a more substantial stake in the property, 
# which generally means less risk for the lender. High LTV ratios might indicate higher risk 
# because they can lead to negative equity if property values decrease. Generally, lenders prefer 
# LTV ratios below 80% to avoid the necessity for mortgage insurance.

def calculate_ltv(loan_amount, property_value):
    """Calculate the Loan-to-Value ratio."""
    return loan_amount / property_value

# Hard-coded values (These are sample values and should be replaced with real-world data)
sample_loan_amount = 80.0  # Loan amount of $80,000,000, represented as 80.0
sample_property_value = 100.0  # Property value of $100,000,000, represented as 100.0

# Calculating LTV from the sample values
sample_ltv_ratio = calculate_ltv(sample_loan_amount, sample_property_value)

print(f"Loan Amount is: ${sample_loan_amount:.2f} million")
print(f"Property Value is: ${sample_property_value:.2f} million")
print(f"Loan-to-Value Ratio (LTV) is: {sample_ltv_ratio*100:.2f}%")
