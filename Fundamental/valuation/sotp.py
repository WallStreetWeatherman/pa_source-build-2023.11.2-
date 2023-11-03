# Sum of the Parts (SOTP) Valuation Calculator
# -------------------------------------------
# Overview:
# The Sum of the Parts (SOTP) valuation approach is used to determine the value of a 
# conglomerate company by breaking it down into its individual business units. Each 
# business unit is valued separately, and the aggregate of these valuations gives 
# the total value of the company.
#
# Desired Value:
# A higher aggregate value indicates that the conglomerate's combined business units 
# are potentially worth more than the market's current valuation of the entire company. 
# This can highlight undervalued companies where the combined value of the parts 
# is greater than the whole.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# financial data should be sourced from the company's financial statements or market data.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for hypothetical business units of a conglomerate company
business_unit_values = {
    "Tech Division": convert_to_actual_value(150.00),
    "Manufacturing Division": convert_to_actual_value(80.00),
    "Retail Division": convert_to_actual_value(50.00),
    "Real Estate Division": convert_to_actual_value(120.00)
}

def sotp_valuation(business_unit_values):
    total_value = sum(business_unit_values.values())
    return total_value

aggregate_value = sotp_valuation(business_unit_values)

# Output the result
print("Sum of the Parts (SOTP) Valuation Calculation:\n")
for division, value in business_unit_values.items():
    print("{}: ${:,.2f} million".format(division, value / 1000000))
print("\nAggregate Value of the Conglomerate: ${:,.2f} million".format(aggregate_value / 1000000))

