def calculate_SGI(this_year_sales, last_year_sales):
    """
    Calculate Sales Growth Index (SGI).
    
    Parameters:
        this_year_sales (float): This year's sales or net revenue.
        last_year_sales (float): Last year's sales or net revenue.
        
    Returns:
        float: Sales Growth Index (SGI).
    """
    
    if last_year_sales == 0:  # To prevent division by zero
        print("Error: Last year's sales are zero. Cannot calculate SGI.")
        return None
    
    SGI = this_year_sales / last_year_sales
    
    return SGI

# Example usage:
this_year_sales = 23_149_000_000  # Replace with actual figure
last_year_sales = 19_732_000_000  # Replace with actual figure

SGI = calculate_SGI(this_year_sales, last_year_sales)

if SGI is not None:
    print(f"The Sales Growth Index (SGI) is: {SGI}")
