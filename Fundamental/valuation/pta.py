# Precedent Transaction Analysis (PTA) Calculator
# ------------------------------------------------
# Overview:
# Precedent Transaction Analysis (PTA) is a valuation method in which past M&A transaction multiples are
# used to value a company. By analyzing what acquirers have historically paid for similar companies,
# one can derive an implied valuation range for the company in question.
#
# Desired Value:
# Typically, higher values indicate that companies in the sector have been valued highly in past transactions.
# However, every deal has its unique circumstances, so context is crucial.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual deal values and financial metrics from multiple past transactions should be input.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for past M&A transactions in the sector
transaction_1 = {
    'name': 'Transaction 1',
    'transaction_value': convert_to_actual_value(100.00),  # Transaction Value
    'ebitda': convert_to_actual_value(10.00)  # EBITDA of acquired company
}

transaction_2 = {
    'name': 'Transaction 2',
    'transaction_value': convert_to_actual_value(200.00),
    'ebitda': convert_to_actual_value(20.00)
}

transactions = [transaction_1, transaction_2]

for transaction in transactions:
    transaction['ev_to_ebitda'] = transaction['transaction_value'] / transaction['ebitda']

# Output the results
print("Precedent Transaction Analysis (PTA):\n")
print("{:<15} {:<15}".format('Transaction', 'EV/EBITDA'))
for transaction in transactions:
    print("{:<15} {:<15.2f}".format(transaction['name'], transaction['ev_to_ebitda']))

# Assuming you want to gauge an appropriate valuation for a company with $15 million EBITDA
target_ebitda = convert_to_actual_value(15.00)
average_ev_to_ebitda = sum([transaction['ev_to_ebitda'] for transaction in transactions]) / len(transactions)
implied_value = average_ev_to_ebitda * target_ebitda

print("\nImplied valuation for a company with $15M EBITDA based on historical transactions: ${:,.2f}".format(implied_value / 1000000))

