# Replacement Cost Method Valuation
# ------------------------------------------------
# Overview:
# The Replacement Cost Method estimates the cost to replace an existing business.
# If it's cheaper to buy the existing company than to build its equivalent from scratch, 
# the company might be undervalued.
#
# Desired Value:
# For investors, a lower replacement cost compared to the market value suggests that 
# the company might be undervalued. Conversely, a higher replacement cost suggests 
# potential overvaluation.
#
# Note: This script uses hard-coded values. For real-world application, input data 
# should be sourced from detailed cost estimation and market data.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def replacement_cost_valuation(existing_company_value, replacement_costs):
    """Evaluates company value based on replacement costs."""
    total_replacement_cost = sum(replacement_costs)
    return existing_company_value, total_replacement_cost

# Hard-coded values for demonstration
existing_company_value = convert_to_actual_value(10.00)  # Current market value of the company, e.g., $10 million

# Costs to replace various segments of the business (e.g., physical assets, R&D, customer base)
replacement_costs = [
    convert_to_actual_value(6.00),  # Cost to replace physical assets
    convert_to_actual_value(3.00),  # Cost to recreate R&D
    convert_to_actual_value(2.50)   # Cost to acquire a similar customer base
]

existing_value, total_replacement_cost = replacement_cost_valuation(existing_company_value, replacement_costs)

# Output the result
print("Replacement Cost Method Valuation:\n")
print("Existing Company Market Value: ${:,.2f}".format(existing_value))
print("Total Replacement Cost: ${:,.2f}".format(total_replacement_cost))

if existing_value <= total_replacement_cost:
    print("The existing company appears to be undervalued based on the Replacement Cost Method.")
else:
    print("The existing company appears to be overvalued based on the Replacement Cost Method.")

