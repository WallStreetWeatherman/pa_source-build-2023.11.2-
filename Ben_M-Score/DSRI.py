def calculate_days_sales_in_receivables(accounts_receivable, net_sales):
    """
    Calculate Days Sales in Receivables (DSO).
    
    Parameters:
        accounts_receivable (float): Accounts Receivable for the year.
        net_sales (float): Net Sales for the year.
        
    Returns:
        float: Days Sales in Receivables.
    """
    return (accounts_receivable / net_sales) * 365


def calculate_DSRI(this_year_receivables, this_year_sales, last_year_receivables, last_year_sales):
    """
    Calculate Days Sales in Receivables Index (DSRI).
    
    Parameters:
        this_year_receivables (float): This year's Accounts Receivable.
        this_year_sales (float): This year's Net Sales.
        last_year_receivables (float): Last year's Accounts Receivable.
        last_year_sales (float): Last year's Net Sales.
        
    Returns:
        float: Days Sales in Receivables Index (DSRI).
    """
    
    this_year_dso = calculate_days_sales_in_receivables(this_year_receivables, this_year_sales)
    last_year_dso = calculate_days_sales_in_receivables(last_year_receivables, last_year_sales)
    
    if last_year_dso == 0:  # To prevent division by zero
        print("Error: Last year's Days Sales in Receivables is zero. Cannot calculate DSRI.")
        return None
    
    return this_year_dso / last_year_dso

# Example usage:
this_year_receivables = 4_312_000_000
this_year_sales = 23_149_000_000
last_year_receivables = 4_126_000_000
last_year_sales = 19_732_000_000

DSRI = calculate_DSRI(this_year_receivables, this_year_sales, last_year_receivables, last_year_sales)

if DSRI is not None:
    print(f"The Days Sales in Receivables Index (DSRI) is: {DSRI}")