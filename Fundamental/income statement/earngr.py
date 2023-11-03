# Earnings Growth Rate Calculator
# -------------------------------
# Overview:
# The Earnings Growth Rate measures the annual rate of growth of earnings from investments.
# It's a vital metric for investors as it provides insights into a company's profitability growth.
#
# Formula:
# Earnings Growth Rate = [(Earnings in Current Period - Earnings in Previous Period) / Earnings in Previous Period] x 100
#
# Desired Value:
# A high earnings growth rate indicates that the company's earnings are increasing, suggesting
# strong profitability and potential for future growth. However, a growth rate that's too high
# might not be sustainable. A low or negative growth rate might indicate challenges in the business.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Earnings in Previous Period (in million dollars format)
earnings_previous_period_in_millions = 5.00  # Example value representing earnings of $5,000,000 in the previous period
earnings_previous_period = convert_to_actual_value(earnings_previous_period_in_millions)

# Earnings in Current Period (in million dollars format)
earnings_current_period_in_millions = 6.50  # Example value representing earnings of $6,500,000 in the current period
earnings_current_period = convert_to_actual_value(earnings_current_period_in_millions)

# Calculate Earnings Growth Rate
if earnings_previous_period == 0:
    earnings_growth_rate = 0
else:
    earnings_growth_rate = ((earnings_current_period - earnings_previous_period) / earnings_previous_period) * 100

# Output the results
print("Factors Influencing Earnings Growth Rate:")
print("- **Revenue Growth:** A rising top line, i.e., sales or revenue, can lead to a corresponding growth in earnings if costs are managed effectively.")
print("- **Margin Expansion:** Improved operational efficiency or pricing power might lead to higher margins, thus positively impacting the earnings growth.")
print("- **Cost Management:** Companies that can control or reduce their operational and fixed costs can see enhanced earnings growth, even with stagnant revenues.")
print("- **Non-recurring Items:** One-off financial events such as the sale of an asset or a legal settlement can temporarily boost or reduce earnings.")
print("- **Taxation Factors:** Changes in tax rates or benefits from tax incentives can influence net earnings.")
print("- **Foreign Exchange Fluctuations:** For multinational companies, currency valuation changes can impact reported earnings.")
print("- **Strategic Investments:** Investments in research & development or market expansion might suppress short-term earnings but can set the stage for future growth.")
print("- **Economic Conditions:** Macro-economic conditions, including demand cycles, interest rates, and consumer sentiment, can influence industry profitability and company earnings.")
print("- **Competitive Landscape:** Shifts in market share, new entrants, or disruptive innovations might affect company earnings.")

print("\nEarnings Growth Rate Analysis:")
print(f"Earnings Growth Rate: {earnings_growth_rate:.2f}%")

if earnings_growth_rate > 20:
    print("The company's earnings are growing at a rapid pace, which may raise questions on sustainability in the long run.")
elif earnings_growth_rate > 0:
    print("The company's earnings are growing, signaling a positive profitability trend.")
elif earnings_growth_rate == 0:
    print("The company's earnings remain consistent, indicating no growth.")
else:
    print("The company's earnings are declining, which may indicate underlying challenges. It's crucial to understand the root causes.")
