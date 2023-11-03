# Net Borrowing Calculator
# ------------------------
# Overview:
# This script calculates Net Borrowing based on new debt issued and debt repaid.
#
# Desired Value:
# A positive Net Borrowing indicates the company has taken on more debt than it has repaid, 
# which could be a signal for expansion or leveraging. A negative value indicates the company 
# has repaid more debt than it has taken on, which could be a sign of deleveraging.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# replace these values with actual financial data.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000  # Convert to actual dollar amounts

# Hard-coded values (in millions, e.g., 1.00 = $1 million)
new_debt_issued = 850.00  # New debt issued
debt_repaid = 1140.00  # Debt repaid

# Convert to actual values
new_debt_issued_actual = convert_to_actual_value(new_debt_issued)
debt_repaid_actual = convert_to_actual_value(debt_repaid)

# Calculate Net Borrowing
net_borrowing = new_debt_issued_actual - debt_repaid_actual
net_borrowing_in_millions = net_borrowing / 1000000  # Convert back to million-dollar format

# Output the result
print(f"Net Borrowing: ${net_borrowing_in_millions:.2f} million")

if net_borrowing_in_millions > 0:
    print("The company has taken on more debt than it has repaid. This could indicate:")
    print("- Plans for expansion, such as entering new markets or launching new products.")
    print("- Leveraging to take advantage of potential high-return investments.")
    print("- Refinancing older, higher-interest debts with newer, lower-interest ones.")
    print("- Managing working capital needs during periods of rapid growth.")
    print("- Response to a favorable debt market condition.")
    print("- Capital expenditures like acquiring assets or technology.")
elif net_borrowing_in_millions < 0:
    print("The company has repaid more debt than it has taken on. This could indicate:")
    print("- A strategy of deleveraging to strengthen the balance sheet.")
    print("- Generation of strong cash flows allowing the firm to reduce liabilities.")
    print("- A shift towards equity financing or internal funding.")
    print("- Company is in a mature or declining phase, thus reducing its operational scale.")
    print("- A risk-averse approach in uncertain market conditions.")
else:
    print("The company's new debt and repayments are balanced. This could indicate:")
    print("- Stable cash flows which align with their debt obligations.")
    print("- A strategic decision to maintain a certain debt level.")
    print("- Successful management of its financial liabilities and assets.")
