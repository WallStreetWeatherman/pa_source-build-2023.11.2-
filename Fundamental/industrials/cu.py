# Capacity Utilization
# --------------------
# Overview:
# Capacity Utilization is a metric used primarily in manufacturing that quantifies 
# the extent to which a manufacturer employs its resources, such as machinery and 
# personnel, versus its full potential. It is expressed as a percentage.
#
# The formula for Capacity Utilization:
#   Capacity Utilization (%) = (Actual Output / Maximum Possible Output) * 100
#
# Desired Value:
# A higher percentage indicates more efficient use of resources. However, if the 
# capacity utilization is consistently too high, it may indicate the need for expansion 
# or concern about overuse of resources. In contrast, very low capacity utilization 
# can indicate inefficiency or underused resources.
#
# Industry standards vary, so it's essential to compare within similar industries.

def calculate_capacity_utilization(actual_output, maximum_possible_output):
    """Calculate the Capacity Utilization percentage."""
    return (actual_output / maximum_possible_output) * 100

# Hard-coded values (These are sample values and should be replaced with real-world data)
actual_output = 8.0         # Actual output of $8,000,000, represented as 8.0
maximum_possible_output = 10.0 # Maximum possible output of $10,000,000, represented as 10.0

# Calculating Capacity Utilization from the sample values
capacity_utilization_percentage = calculate_capacity_utilization(actual_output, maximum_possible_output)

print(f"Actual Output: ${actual_output:.2f} million")
print(f"Maximum Possible Output: ${maximum_possible_output:.2f} million")
print(f"Capacity Utilization: {capacity_utilization_percentage:.2f}%")
