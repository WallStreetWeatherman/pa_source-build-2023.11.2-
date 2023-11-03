# Beneish M-Score Calculator
# ---------------------------
# Overview:
# The Beneish M-Score is a statistical model to detect earnings manipulation.
# Companies with a score greater than -2.22 are more likely to be manipulating their earnings.
#
# Formula:
# M = -4.84 + 0.92*DSRI + 0.528*GMI + 0.404*AQI + 0.892*SGI + 0.115*DEPI - 0.172*SGAI + 4.679*TATA - 0.327*LVGI
#
# Ratios:
# DSRI = Days Sales in Receivables Index
# GMI = Gross Margin Index
# AQI = Asset Quality Index
# SGI = Sales Growth Index
# DEPI = Depreciation Index
# SGAI = Sales General and Administrative Expenses Index
# TATA = Total Accruals to Total Assets
# LVGI = Leverage Index
#
# Desired Value:
# M > -2.22 indicates a higher likelihood of earnings manipulation.
# 
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# financial statement data should be input.

# Hard-coded values in millions as decimals
# These are hypothetical values and should be replaced with real financial data
DSRI = 1.03  # Example value
GMI = 1.15  # Example value
AQI = 1.02  # Example value
SGI = 1.1   # Example value
DEPI = 0.95 # Example value
SGAI = 1.05 # Example value
TATA = 0.06 # Example value
LVGI = 1.2  # Example value

# Calculating the Beneish M-Score
m_score = (-4.84 + 0.92*DSRI + 0.528*GMI + 0.404*AQI + 0.892*SGI + 0.115*DEPI - 0.172*SGAI + 4.679*TATA - 0.327*LVGI)

# Outputting the results
print(f"Beneish M-Score: {m_score:.2f}")
if m_score > -2.22:
    print("Warning: Higher likelihood of earnings manipulation.")
else:
    print("Normal: Lower likelihood of earnings manipulation.")
