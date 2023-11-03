# Net Change in Working Capital Calculator
# ----------------------------------------
# Overview:
# This script calculates the net change in working capital for both a specific company 
# and the industry average. The net change in working capital is an essential measure 
# for understanding how much a company's short-term assets and liabilities have changed 
# over a period.
#
# Desired Value:
# A significant increase might indicate the company is not efficiently utilizing its 
# short-term assets or not effectively managing its short-term liabilities. Conversely, 
# a substantial decrease might indicate potential liquidity concerns. Comparing the 
# company's net change to the industry average can provide context.


def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company
start_current_assets_in_millions = 6758.00 # Total Current Assets in Tikr
end_current_assets_in_millions = 5853.00

start_current_liabilities_in_millions = 5416.00 # Total Current Liabilites in Tikr
end_current_liabilities_in_millions = 4861.00

# Hard-coded values for industry average 
industry_start_current_assets_in_millions = 9530.00 
industry_end_current_assets_in_millions = 2880.00

industry_start_current_liabilities_in_millions = 7650.00
industry_end_current_liabilities_in_millions = 1680.00

# Calculate net change in working capital for the company
company_net_change = (convert_to_actual_value(end_current_assets_in_millions) - convert_to_actual_value(start_current_assets_in_millions)) - \
                    (convert_to_actual_value(end_current_liabilities_in_millions) - convert_to_actual_value(start_current_liabilities_in_millions))

# Calculate net change in working capital for the industry
industry_net_change = (convert_to_actual_value(industry_end_current_assets_in_millions) - convert_to_actual_value(industry_start_current_assets_in_millions)) - \
                     (convert_to_actual_value(industry_end_current_liabilities_in_millions) - convert_to_actual_value(industry_start_current_liabilities_in_millions))

print(f"Company's Net Change in Working Capital: ${company_net_change:.2f}")
print(f"Industry Average Net Change in Working Capital: ${industry_net_change:.2f}\n")

if company_net_change > industry_net_change:
    print("The company's net change in working capital is greater than the industry average. This could indicate several scenarios:")
    print("- The company has made significant sales but hasn't collected from its customers yet (accounts receivable).")
    print("- The company has overstocked inventory, potentially indicating inefficiencies or anticipation of higher future sales.")
    print("- There might be a decrease in accounts payable, indicating the company paid off its short-term debts more quickly than usual.")
    print("- It could also suggest the company is not efficiently utilizing its short-term assets or not effectively managing its short-term liabilities.")
elif company_net_change < industry_net_change:
    print("The company's net change in working capital is less than the industry average. Potential implications include:")
    print("- The company might be experiencing liquidity issues, struggling to maintain enough short-term assets to cover short-term liabilities.")
    print("- There could be a substantial increase in short-term debts (accounts payable) without a corresponding increase in short-term assets.")
    print("- The company could be efficiently converting its inventory to sales and effectively managing its accounts payable and receivable.")
    print("- The company might be operating on a leaner model compared to industry peers.")
else:
    print("The company's net change in working capital aligns with the industry standard. This suggests that its working capital management practices are in line with industry norms, neither exceptionally efficient nor problematic.")
