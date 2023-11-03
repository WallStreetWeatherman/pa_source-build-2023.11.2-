# Comparable Companies Analysis (CCA) Calculator
# ----------------------------------------------
# Overview:
# Comparable Companies Analysis (CCA) is a method used to value a company by comparing its valuation 
# ratios to those of its peers in the same industry or sector. Common multiples used include P/E, P/B, 
# and EV/EBITDA.
# 
# Desired Value:
# The "desired" value depends on the purpose of the analysis. If you're looking for undervalued stocks, 
# you might seek companies with lower multiples compared to peers. Conversely, higher multiples might 
# indicate overvaluation or higher growth expectations.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values from multiple companies should be input.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for a hypothetical company 'Company A' and its peers
company_a = {
    'name': 'Company A',
    'price': 50.00,  # Stock price
    'earnings': convert_to_actual_value(5.00),  # Earnings
    'book_value': convert_to_actual_value(10.00),  # Book Value
    'ev': convert_to_actual_value(100.00),  # Enterprise Value
    'ebitda': convert_to_actual_value(20.00)  # EBITDA
}

peer_1 = {
    'name': 'Peer 1',
    'price': 45.00,
    'earnings': convert_to_actual_value(4.50),
    'book_value': convert_to_actual_value(9.00),
    'ev': convert_to_actual_value(90.00),
    'ebitda': convert_to_actual_value(18.00)
}

peer_2 = {
    'name': 'Peer 2',
    'price': 55.00,
    'earnings': convert_to_actual_value(6.00),
    'book_value': convert_to_actual_value(12.00),
    'ev': convert_to_actual_value(110.00),
    'ebitda': convert_to_actual_value(24.00)
}

companies = [company_a, peer_1, peer_2]

for company in companies:
    company['pe_ratio'] = company['price'] / (company['earnings'] / convert_to_actual_value(1.00))
    company['pb_ratio'] = company['price'] / (company['book_value'] / convert_to_actual_value(1.00))
    company['ev_to_ebitda'] = company['ev'] / company['ebitda']

# Output the results
print("Comparable Companies Analysis (CCA):\n")
print("{:<12} {:<10} {:<10} {:<15}".format('Company', 'P/E', 'P/B', 'EV/EBITDA'))
for company in companies:
    print("{:<12} {:<10.2f} {:<10.2f} {:<15.2f}".format(company['name'], company['pe_ratio'], company['pb_ratio'], company['ev_to_ebitda']))
