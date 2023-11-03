# EBT Including Unusual Items Calculation
# ---------------------------------------
# Overview:
# EBT Including Unusual Items accounts for a company's profit before taxes 
# with the addition of non-recurring or unusual items. It gives a comprehensive 
# view of a company's earnings during periods when these one-off events occurred.
#
# Desired Value:
# Generally, a higher EBT suggests better profitability, but the inclusion of 
# unusual items can distort the underlying operating performance. It's crucial 
# to understand the nature of the unusual items and their impact on reported 
# earnings when analyzing this metric.
#
# Note: This script uses hard-coded values. For real-world application, data should be adjusted accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Hard-coded values
revenues = convert_to_actual_value(250.00)           # Example: $250 million
cost_of_goods_sold = convert_to_actual_value(80.00)   # Example: $80 million
operating_expenses = convert_to_actual_value(60.00)   # Example: $60 million
interest_expense = convert_to_actual_value(10.00)     # Example: $10 million
unusual_items = convert_to_actual_value(-15.00)       # Example: -$15 million (e.g., loss from asset sale)

# Calculate EBT Including Unusual Items
ebt_incl_unusual = revenues - cost_of_goods_sold - operating_expenses - interest_expense + unusual_items

# Output the result
print("EBT (Earnings Before Taxes) Including Unusual Items Calculation:\n")
print(f"EBT Including Unusual Items: ${ebt_incl_unusual/1000000:,.2f} million")

# Analysis based on EBT value including unusual items
if ebt_incl_unusual > 0:
    print("\nThe company has a positive EBT even after accounting for unusual items, indicating overall profitability.")
    print("\nPotential positive influencing factors include:")
    print("- Robust sales and revenue streams.")
    print("- Efficient cost management strategies.")
    print("- Positive effects of certain unusual items, like gains from asset sales or lawsuit settlements.")
else:
    print("\nThe company has a negative or zero EBT after accounting for unusual items, suggesting challenges in profitability.")
    print("\nPotential challenging influencing factors include:")
    print("- Declining revenues or increased competition.")
    print("- Rising operational costs or unexpected expenses.")
    print("- Significant negative unusual items, such as large fines, asset write-downs, or substantial lawsuit settlements.")
    