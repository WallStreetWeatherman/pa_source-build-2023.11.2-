# Load Factor
# -----------
# Overview:
# The Load Factor measures the operational efficiency of energy companies by comparing 
# the actual energy output to the maximum possible output. It's used primarily by utility 
# companies to determine how efficiently they are producing energy relative to their capacity.
#
# Formula for Load Factor:
#   Load Factor = (Total Energy Produced in a Period) / (Maximum Possible Energy Production in that Period)
#
# Desired Value:
# A higher Load Factor is preferable, indicating efficient utilization of available resources. 
# However, a Load Factor of 100% could suggest that the company is running at full capacity, 
# which might not be sustainable over the long term. It's essential to assess the value 
# in context with industry averages and the company's historical data.

def calculate_load_factor(total_energy_produced, max_possible_energy_production):
    """Calculate the Load Factor."""
    return total_energy_produced / max_possible_energy_production

# Hard-coded values (expressed in terms of "million dollars" where 1 million is 1.00, 10 million is 10.00, etc.)
total_energy_produced = 50.00          # Example: 50 million units of energy produced
max_possible_energy_production = 70.00 # Example: maximum capacity of 70 million units

# Calculating Load Factor from the sample values
load_factor_percentage = calculate_load_factor(total_energy_produced, max_possible_energy_production) * 100

print(f"Total Energy Produced: {total_energy_produced} million units")
print(f"Maximum Possible Energy Production: {max_possible_energy_production} million units")
print(f"Load Factor: {load_factor_percentage:.2f}%")
