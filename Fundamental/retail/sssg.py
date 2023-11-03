# Same-Store Sales Growth
# -----------------------
# Overview:
# Same-Store Sales Growth, also known as comparable or "comp" sales, is a metric used primarily 
# by retailers to measure the performance of their existing stores over a specified period, 
# excluding the impact of recently opened or closed stores. It provides insight into the 
# organic growth of a business.
#
# The formula for Same-Store Sales Growth:
#   (Current Period Sales - Previous Period Sales) / Previous Period Sales * 100
#
# Desired Value:
# Positive Same-Store Sales Growth indicates an increase in sales, which is generally favorable 
# for a retailer. However, consistent negative growth may indicate underlying problems. 
# It's crucial to understand the reasons behind the growth or decline.

def calculate_same_store_sales_growth(current_period_sales, previous_period_sales):
    """Calculate the Same-Store Sales Growth in percentage."""
    return ((current_period_sales - previous_period_sales) / previous_period_sales) * 100

# Hard-coded values (These are sample values and should be replaced with real-world data)
previous_sales = 50.0  # Previous period sales of $50,000,000, represented as 50.0
current_sales = 55.0   # Current period sales of $55,000,000, represented as 55.0

# Calculating Same-Store Sales Growth from the sample values
growth_percentage = calculate_same_store_sales_growth(current_sales, previous_sales)

print(f"Previous Period Sales: ${previous_sales:.2f} million")
print(f"Current Period Sales: ${current_sales:.2f} million")
print(f"Same-Store Sales Growth: {growth_percentage:.2f}%")
