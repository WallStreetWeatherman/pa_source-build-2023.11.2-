# Operating Cycle
# ---------------
# Overview:
# The Operating Cycle calculates the time taken for a business to go from purchasing 
# raw materials to receiving cash from its sales. It comprises two parts: the number 
# of days inventory is on hand (Days Inventory Outstanding - DIO) and the number 
# of days it takes to collect cash from credit sales (Days Sales Outstanding - DSO).
#
# Formula for Operating Cycle:
#   Operating Cycle = DIO + DSO
#
# Desired Value:
# A shorter operating cycle is preferable because it indicates the company can quickly 
# convert its products into cash. However, what is considered "short" varies by industry, 
# and it's critical to make comparative assessments within the same sector.

def calculate_operating_cycle(DIO, DSO):
    """Calculate the Operating Cycle in days."""
    return DIO + DSO

# Hard-coded values (These are sample values and should be replaced with real-world data)
DIO = 45.0         # Days Inventory Outstanding (represented as 45 days)
DSO = 30.0        # Days Sales Outstanding (represented as 30 days)

# Calculating Operating Cycle from the sample values
operating_cycle_days = calculate_operating_cycle(DIO, DSO)

print(f"Days Inventory Outstanding (DIO): {DIO} days")
print(f"Days Sales Outstanding (DSO): {DSO} days")
print(f"Operating Cycle: {operating_cycle_days} days")
