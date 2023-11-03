def calculate_net_profit(revenue, cogs, operating_expenses, interest_expense, taxes):
    """
    Calculate Net Profit based on various expenses and revenue.
    
    Parameters:
        revenue (float): Total revenue.
        cogs (float): Cost of Goods Sold.
        operating_expenses (float): Operating Expenses.
        interest_expense (float): Interest Expense.
        taxes (float): Taxes.
        
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
    net_profit = earnings_before_tax - taxes
    
    return net_profit

# Add Variables Here:
revenue = 710_720_000 
cogs = 140_350_000  
operating_expenses = 620_140_000 
interest_expense = 0
taxes = 100_000  

net_profit = calculate_net_profit(revenue, cogs, operating_expenses, interest_expense, taxes)

print(f"Net Profit (or Net Income): ${net_profit}")