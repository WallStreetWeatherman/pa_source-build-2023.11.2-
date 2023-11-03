# M&A Comps (Mergers and Acquisitions Comparables)
#
# Overview:
# M&A Comps analysis evaluates a company based on recent mergers and acquisitions 
# within an industry to determine the average going rate for similar companies. 
# This helps to identify whether a company might be undervalued or overvalued 
# compared to its peers that were recently acquired.
#
# Desired Value:
# If the target company's value is considerably lower than the average M&A 
# comp value, it might be undervalued. Conversely, if it's significantly higher, 
# it could be overvalued.

def ma_comps(target_company_value, recent_ma_values, industry_average):
    """
    Determine the position of the target company based on recent M&A values and industry average.
    
    Parameters:
    - target_company_value: Value of the target company
    - recent_ma_values: List of recent M&A transaction values in the industry.
    - industry_average: The industry average company value
    
    Returns:
    - A string indicating the position of the target company compared to the average M&A value.
    """
    average_ma_value = sum(recent_ma_values) / len(recent_ma_values)
    
    valuation_status = ''
    
    if target_company_value < industry_average * 0.9:  # 10% threshold for undervaluation
        valuation_status = "The target company appears to be undervalued compared to the industry average."
    elif target_company_value > industry_average * 1.1:  # 10% threshold for overvaluation
        valuation_status = "The target company appears to be overvalued compared to the industry average."
    else:
        valuation_status = "The target company appears to be fairly valued."
    
    return average_ma_value, valuation_status

# Hardcoded values
target_company_value = 12.00
recent_ma_values = [10.00, 11.50, 13.00, 9.50, 12.50]
industry_average = sum(recent_ma_values) / len(recent_ma_values)

average_ma_value, result = ma_comps(target_company_value, recent_ma_values, industry_average)

# Output the results
print(f"Target Company Value: ${target_company_value:.2f} million")
print(f"Average M&A Comparable Value: ${average_ma_value:.2f} million")
print(f"Industry Average Value: ${industry_average:.2f} million")
print(result)

# Interpretation
if target_company_value < industry_average * 0.9:
    print("\nFactors possibly contributing to the undervaluation include:")
    print("- Subpar company performance compared to recently acquired peers.")
    print("- Lack of visibility or recognition in the market.")
    print("- Operational or financial challenges facing the company.")
    print("- Market conditions or external factors that have impacted the company more than its peers.")
elif target_company_value > industry_average * 1.1:
    print("\nFactors possibly contributing to the overvaluation include:")
    print("- Superior performance and growth prospects compared to peers.")
    print("- Strong brand recognition or proprietary technology.")
    print("- Beneficial market positioning or competitive advantages.")
    print("- Recent positive news or events boosting the company's value.")
else:
    print("\nThe target company's valuation aligns with the industry average, indicating a comparable market position to its recently acquired peers.")
    