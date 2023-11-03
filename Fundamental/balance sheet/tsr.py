# Total Shareholder Return (TSR) Calculator
# ----------------------------------------
# Overview:
# Total Shareholder Return (TSR) measures the total return on a company's stock, considering both 
# capital gains (or losses) and dividends received. It is a comprehensive measure of a stock's 
# performance from an investor's perspective.
#
# Formula:
# TSR = (Ending stock price + Dividends - Beginning stock price) / Beginning stock price
#
# Desired Value:
# A higher TSR indicates better returns for the shareholders.
# Negative TSR indicates the investor would have lost money during the period.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual stock price and dividend data should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)
# Replace these with actual stock and dividend data

# Stock prices at the beginning and end of a period
beginning_stock_price = 10.00  # Stock price at the start of the period
ending_stock_price = 12.00  # Stock price at the end of the period

# Dividends received during the period
dividends = 0.50  # Total dividends received during the period

# Calculate Total Shareholder Return (TSR)
tsr = ((ending_stock_price + dividends - beginning_stock_price) / beginning_stock_price) * 100

# Outputting the results
print(f"Total Shareholder Return (TSR) Analysis:\n")
print(f"Calculated TSR based on given assumptions: {tsr:.2f}%")

if tsr > 0:
    print("The investment has yielded a positive return. Factors influencing this might include:")
    print("- Strong company earnings or upbeat financial guidance.")
    print("- Positive industry trends or favorable market conditions.")
    print("- Announcements of dividends or stock buybacks.")
    print("- Strategic acquisitions or partnerships that add value to the company.")
elif tsr < 0:
    print("The investment has yielded a negative return. Potential reasons and areas of investigation include:")
    print("- Subpar quarterly earnings or lowered financial guidance.")
    print("- Negative industry trends or economic downturns.")
    print("- Regulatory hurdles or lawsuits affecting the company's performance.")
    print("- Loss of key contracts or clients.")
else:
    print("There's no change in the return from the investment. Possible reasons could be:")
    print("- A balanced mix of positive and negative news affecting the stock.")
    print("- Market volatility that had both upward and downward impacts.")
    print("- Company's performance is in line with market expectations.")
