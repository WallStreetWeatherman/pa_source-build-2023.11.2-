# Weighted Average Basic Shares Outstanding Calculation
# -----------------------------------------------------
# Overview:
# This represents the average number of basic shares over a specified period, 
# taking into account any changes in the share count.
#
# Desired Value:
# Generally, for an investor, a decreasing number of shares is preferred as it means 
# there's less dilution of ownership. However, understanding the context for why 
# shares are increasing or decreasing is essential (e.g., stock buybacks, secondary offerings).
#
# Note: This script uses hard-coded values. For real-world application, data should be adjusted accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Example periods with hard-coded values (in months for this example, but could be quarters, etc.)
# Each tuple contains the period length and the average number of basic shares during that period
# For example, for 2 months there were an average of 5 million basic shares outstanding
periods = [
    (2, convert_to_actual_value(5.00)), 
    (4, convert_to_actual_value(5.25)),
    (3, convert_to_actual_value(5.40)),
    (3, convert_to_actual_value(5.20))
]

# Calculate the weighted average
total_period_length = sum(period[0] for period in periods)
weighted_average_basic_shares = sum(period[0] * period[1] for period in periods) / total_period_length

# Output the result
print("Weighted Average Basic Shares Outstanding Calculation:\n")
print("Weighted Average Basic Shares: {:,.2f}".format(weighted_average_basic_shares))

# Analyze the trend
beginning_period_shares = periods[0][1]
ending_period_shares = periods[-1][1]

if ending_period_shares < beginning_period_shares:
    print("\nThere's a decreasing trend in the Weighted Average Basic Shares Outstanding over the given periods.")
    print("\nPossible reasons for this decrease include:")
    print("- Company-initiated stock buybacks, which can indicate confidence in the company's future and return excess capital to shareholders.")
    print("- Mergers or acquisitions where the company's stock was used as a partial form of payment.")
    print("- Exercised stock options or other dilutive securities being offset by buybacks.")
    print("- Expiry of certain convertible bonds or securities without being converted to equity.")
    
elif ending_period_shares > beginning_period_shares:
    print("\nThere's an increasing trend in the Weighted Average Basic Shares Outstanding over the given periods.")
    print("\nPossible reasons for this increase are:")
    print("- The company might have issued additional shares to raise capital, which can dilute existing shareholders' ownership.")
    print("- Conversion of convertible bonds, warrants, or preferred stock into equity, increasing the number of shares.")
    print("- Employee stock option exercises, where employees convert their options into actual shares.")
    print("- Secondary offerings, where new shares are issued to the public.")
    
else:
    print("\nThe Weighted Average Basic Shares Outstanding has remained relatively constant over the given periods.")
    print("\nStable share counts can indicate a balanced approach to capital management where new issuances (if any) are offset by repurchases.")
    