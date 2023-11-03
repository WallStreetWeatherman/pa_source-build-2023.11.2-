def calculate_depreciation_rate(depreciation_expense, gross_ppe, accumulated_depreciation):
    """
    Calculate the Depreciation Rate.
    
    Parameters:
        depreciation_expense (float): Depreciation expense for the year.
        gross_ppe (float): Gross Property, Plant, and Equipment for the year.
        accumulated_depreciation (float): Accumulated Depreciation for the year.
        
    Returns:
        float: Depreciation Rate.
    """
    return depreciation_expense / (gross_ppe - accumulated_depreciation)


def calculate_DEPI(this_year_depreciation_expense, this_year_gross_ppe, this_year_accumulated_depreciation,
                   last_year_depreciation_expense, last_year_gross_ppe, last_year_accumulated_depreciation):
    """
    Calculate Depreciation Index (DEPI).
    
    Parameters:
        this_year_depreciation_expense (float): This year's Depreciation Expense.
        this_year_gross_ppe (float): This year's Gross Property, Plant, and Equipment.
        this_year_accumulated_depreciation (float): This year's Accumulated Depreciation.
        last_year_depreciation_expense (float): Last year's Depreciation Expense.
        last_year_gross_ppe (float): Last year's Gross Property, Plant, and Equipment.
        last_year_accumulated_depreciation (float): Last year's Accumulated Depreciation.
        
    Returns:
        float: Depreciation Index (DEPI).
    """
    
    this_year_rate = calculate_depreciation_rate(this_year_depreciation_expense, this_year_gross_ppe, this_year_accumulated_depreciation)
    last_year_rate = calculate_depreciation_rate(last_year_depreciation_expense, last_year_gross_ppe, last_year_accumulated_depreciation)
    
    if this_year_rate == 0:  # To prevent division by zero
        print("Error: This year's Depreciation Rate is zero. Cannot calculate DEPI.")
        return None
    
    return last_year_rate / this_year_rate

# Example usage:
this_year_depreciation_expense = 500_000  
this_year_gross_ppe = 5_000_000  
this_year_accumulated_depreciation = 2_000_000  

last_year_depreciation_expense = 400_000  
last_year_gross_ppe = 4_500_000  
last_year_accumulated_depreciation = 1_800_000  

DEPI = calculate_DEPI(this_year_depreciation_expense, this_year_gross_ppe, this_year_accumulated_depreciation,
                      last_year_depreciation_expense, last_year_gross_ppe, last_year_accumulated_depreciation)

if DEPI is not None:
    print(f"The Depreciation Index (DEPI) is: {DEPI}")