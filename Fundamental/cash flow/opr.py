# Operating Performance Ratio Calculator
# --------------------------------------
# Overview:
# The Operating Performance Ratio (OPR) gauges a company's ability to convert 
# its sales into cash. A higher ratio indicates that the company is efficient 
# at translating its sales into actual cash flow, which can be used for 
# reinvestment, debt servicing, or returned to shareholders.
#
# Formula:
# Operating Performance Ratio = Operating Cash Flow / Sales Revenue
#
# Desired Value:
# A higher ratio is preferable as it means the firm is more efficient in 
# turning its sales into cash. Conversely, a lower ratio may indicate inefficiencies 
# in the company's operations or its collection practices.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Operating Cash Flow (in million dollars format for simplicity)
operating_cash_flow_in_millions = 1583.00 # Cash from Operations in Tikr
operating_cash_flow = convert_to_actual_value(operating_cash_flow_in_millions)

# Sales Revenue (in million dollars format for simplicity)
sales_revenue_in_millions = 23606.00  # Revenues in Tikr
sales_revenue = convert_to_actual_value(sales_revenue_in_millions)

# Calculate Operating Performance Ratio for the company
opr_company = operating_cash_flow / sales_revenue

# Hard-coded values for the industry average
industry_average_operating_cash_flow_in_millions = 1600.00  
industry_average_operating_cash_flow = convert_to_actual_value(industry_average_operating_cash_flow_in_millions)

industry_average_sales_revenue_in_millions = 24000.00  
industry_average_sales_revenue = convert_to_actual_value(industry_average_sales_revenue_in_millions)

# Calculate OPR for the industry
opr_industry = industry_average_operating_cash_flow / industry_average_sales_revenue

# Output the results
print(f"Company's Operating Performance Ratio: {opr_company:.2f}")
print(f"Industry Average Operating Performance Ratio: {opr_industry:.2f}\n")

print("Analyzing the components and possible influencing factors:")

print(f"Operating Cash Flow: ${operating_cash_flow_in_millions:.2f} million")
if operating_cash_flow > 0:
    print("- A positive operating cash flow suggests the company effectively manages its working capital, possibly having efficient collections, judicious inventory management, and controlled operating expenses.")
else:
    print("- A negative or low operating cash flow might hint at issues like delayed collections, high inventory levels, or substantial operating costs.")

print(f"Sales Revenue: ${sales_revenue_in_millions:.2f} million")
print("- The magnitude and volatility in sales revenue can arise from various sources: market demand fluctuations, pricing adjustments, promotional activities, or seasonal sales variations.")

print("\nGeneral Observations:")
if opr_company > 0.5:
    print("For the company, a considerable part of sales turns into cash. This might reflect effective operations, efficient credit policies, or favorable terms with suppliers. It positions the company well for growth and meeting financial obligations.")
elif opr_company > 0.2:
    print("For the company, around a fifth to half of its sales become cash. It signifies a balance between revenues and costs but there could be potential areas to optimize cash flow, such as revisiting credit policies or inventory management.")
else:
    print("For the company, less than a fifth of its sales become cash. This might indicate challenges in cash flow management, such as slow receivable collections, significant discounts, or high operating costs.")

if opr_company > opr_industry:
    print("The company's OPR exceeds the industry average, which could signal a competitive edge in its operations. Factors like efficient collection practices, low return rates, or streamlined supply chain management might be contributing.")
elif opr_company < opr_industry:
    print("The company's OPR trails the industry average. It would be wise to examine potential bottlenecks in operations, review credit terms, and perhaps benchmark against industry leaders to identify areas of enhancement.")
else:
    print("The company's OPR aligns with the industry benchmark, showcasing its operations as standard compared to its peers.")
