def calculate_gross_margin(net_sales, cogs):
    """
    Calculate Gross Margin.
    
    Parameters:
        net_sales (float): Net Sales for the year.
        cogs (float): Cost of Goods Sold for the year.
        
    Returns:
        float: Gross Margin.
    """
    return (net_sales - cogs) / net_sales

def calculate_GMI(this_year_net_sales, this_year_cogs, last_year_net_sales, last_year_cogs):
    """
    Calculate Gross Margin Index (GMI).
    
    Parameters:
        this_year_net_sales (float): This year's Net Sales.
        this_year_cogs (float): This year's Cost of Goods Sold.
        last_year_net_sales (float): Last year's Net Sales.
        last_year_cogs (float): Last year's Cost of Goods Sold.
        
    Returns:
        float: Gross Margin Index (GMI).
    """
    
    this_year_gross_margin = calculate_gross_margin(this_year_net_sales, this_year_cogs)
    last_year_gross_margin = calculate_gross_margin(last_year_net_sales, last_year_cogs)
    
    if this_year_gross_margin == 0:  # To prevent division by zero
        print("Error: This year's Gross Margin is zero. Cannot calculate GMI.")
        return None
    
    return last_year_gross_margin / this_year_gross_margin

# Example usage:
this_year_net_sales = 23_149_000_000
this_year_cogs = 10_945_000_000
last_year_net_sales = 19_732_000_000
last_year_cogs = 11_550_000_000

GMI = calculate_GMI(this_year_net_sales, this_year_cogs, last_year_net_sales, last_year_cogs)

if GMI is not None:
    print(f"The Gross Margin Index (GMI) is: {GMI}")
