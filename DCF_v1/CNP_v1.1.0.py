def calculate_net_profit(revenue, cogs, operating_expenses, interest_expense, income_tax_expense):
    """
    Calculate Net Profit based on various expenses and revenue.
    
    Parameters:
        revenue (float): Total revenue.
        cogs (float): Cost of Goods Sold.
        operating_expenses (float): Operating Expenses.
        interest_expense (float): Interest Expense. Put '0' if none.
        income_tax_expense (float): Income Tax Expense.
        
    Returns:
        net_profit (float): Net Profit or Net Income.
    """
    # Gross Profit
    gross_profit = revenue - cogs
    
    # Operating Profit
    operating_profit = gross_profit - operating_expenses
    
    # Earnings Before Tax
    earnings_before_tax = operating_profit - interest_expense
    
    # Net Profit or Net Income
    net_profit = earnings_before_tax - income_tax_expense
    
    return net_profit

# Add Variables Here:
revenue = 710_720_000 
cogs = 140_350_000  
operating_expenses = 620_140_000 
interest_expense = 0
income_tax_expense = 240_000

net_profit = calculate_net_profit(revenue, cogs, operating_expenses, interest_expense, income_tax_expense)

print(f"Net Profit (or Net Income): ${net_profit}")