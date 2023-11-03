# Replacement Cost Valuation
# --------------------------
# Overview:
# The Replacement Cost Valuation method is primarily used to value a company based on 
# the cost it would take to replace its assets. This is especially relevant for commodity 
# companies or companies where their primary value comes from their tangible assets.
#
# Formula:
#   Replacement Cost = Sum of all costs to replace tangible assets (land, machinery, inventory, etc.)
#
# Desired Value:
# A company's market value that is lower than its replacement cost might be undervalued, 
# suggesting a buying opportunity. Conversely, if the market value is significantly higher 
# than the replacement cost, it could indicate overvaluation, though other factors 
# (like brand, IP, etc.) might justify the premium.

def calculate_replacement_cost(land_cost, machinery_cost, inventory_cost, technology_cost, human_resources_cost):
    """Calculate the Replacement Cost."""
    return land_cost + machinery_cost + inventory_cost + technology_cost + human_resources_cost

# Hard-coded values (expressed in terms of "million dollars" where 1 million is 1.00, 10 million is 10.00, etc.)
land_cost = 10.00        # Cost to replace or acquire equivalent land
machinery_cost = 15.00   # Cost to replace machinery/equipment
inventory_cost = 5.00    # Cost to replace inventory
technology_cost = 8.00   # Cost to develop/acquire equivalent technology
human_resources_cost = 12.00 # Cost for human resources (training, hiring, etc.)

# Calculating Replacement Cost from the sample values
replacement_cost = calculate_replacement_cost(land_cost, machinery_cost, inventory_cost, technology_cost, human_resources_cost)

print(f"Land Replacement Cost: ${land_cost} million")
print(f"Machinery Replacement Cost: ${machinery_cost} million")
print(f"Inventory Replacement Cost: ${inventory_cost} million")
print(f"Technology Replacement Cost: ${technology_cost} million")
print(f"Human Resources Replacement Cost: ${human_resources_cost} million")
print(f"Total Replacement Cost: ${replacement_cost} million")
