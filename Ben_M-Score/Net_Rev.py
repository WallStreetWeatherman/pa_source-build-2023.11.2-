def calculate_net_revenue(gross_sales, returns, allowances, discounts):
    """
    Calculate Net Revenue (Net Sales).
    
    Parameters:
        gross_sales (float): Total gross sales.
        returns (float): Total value of returned items.
        allowances (float): Total value of allowances.
        discounts (float): Total value of discounts.
        
    Returns:
        float: Net Revenue (Net Sales).
    """
    return gross_sales - (returns + allowances + discounts)

# Example usage:
gross_sales = 500000  # Total gross sales for the period
returns = 20000  # Total returns for the period
allowances = 5000  # Total allowances for the period
discounts = 10000  # Total discounts for the period

net_revenue = calculate_net_revenue(gross_sales, returns, allowances, discounts)

print(f"The Net Revenue (Net Sales) is: ${net_revenue}")
