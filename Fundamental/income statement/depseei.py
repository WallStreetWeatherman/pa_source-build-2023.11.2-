# Diluted EPS Excluding Extraordinary Items Calculation
# -----------------------------------------------------
# Overview:
# Diluted EPS Excluding Extraordinary Items offers a clearer picture of a company's profitability 
# by considering only core operations and excluding one-time, non-recurring items.
# It takes into account potential shares that could come into existence, like from stock options.
#
# Desired Value:
# A higher Diluted EPS Excl. Extra Items is preferable, as it indicates greater profitability 
# and more earnings available for shareholders. Conversely, a declining EPS might signify potential problems.
#
# Note: This script uses hard-coded values. For real-world application, data should be adjusted accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Hard-coded values for demonstration:
net_income = convert_to_actual_value(20.00)  # Net income of the company
extraordinary_items = convert_to_actual_value(5.00)  # Extraordinary items value
diluted_shares_outstanding = convert_to_actual_value(10.00)  # Diluted number of shares outstanding

# Diluted EPS calculation excluding extraordinary items
diluted_eps_excl_extra_items = (net_income - extraordinary_items) / diluted_shares_outstanding

# Output the result
print("Factors Influencing Diluted EPS Excluding Extraordinary Items:")
print("- **Stock-based Compensation:** As more stock options or other equity-based compensation get exercised, it increases the diluted share count, which could depress the EPS.")
print("- **Mergers and Acquisitions:** Accretive acquisitions can enhance EPS, while dilutive acquisitions might reduce it. The manner in which the transaction is financed (stock vs. cash) also impacts dilution.")
print("- **Debt Conversions:** Convertible debt, when converted into stock, increases the number of outstanding shares, leading to potential EPS dilution.")
print("- **Business Segmentation:** The performance of various business segments can influence overall profitability, impacting the EPS.")
print("- **Operational Efficiency:** Efficiency in operations can lead to increased profits, positively affecting the EPS.")
print("- **Change in Tax Rates:** Changes in corporate tax rates, either due to policy changes or operational shifts, can influence net income.")
print("- **Foreign Exchange Movements:** For companies with global operations, FX movements can significantly impact profitability.")
print("- **Write-downs/Impairments:** Significant write-downs or asset impairments, even if non-recurring, can depress net income and thus, the EPS.")

print("\nAnalysis of Diluted EPS Excluding Extraordinary Items:")
print("Diluted EPS Excl. Extra Items: ${:,.2f} per share".format(diluted_eps_excl_extra_items))
if diluted_eps_excl_extra_items > 0:
    print("A positive Diluted EPS indicates profitability on a per-share basis after considering potential dilution and excluding non-core activities.")
else:
    print("A negative Diluted EPS suggests challenges in maintaining profitability on a per-share basis after considering potential dilution and excluding non-core activities.")
