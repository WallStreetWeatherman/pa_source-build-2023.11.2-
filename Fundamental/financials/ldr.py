# Loan-to-Deposit Ratio (LDR)
# ---------------------------
# Overview:
# LDR measures the comparison between a bank's total loans and its total deposits.
# It's a common metric to assess a bank's liquidity. If the ratio is too high, it may 
# indicate that the bank might not have enough liquidity to cover any unforeseen fund requirements.
# If too low, the bank may not be earning as much as they could be on their loans.
#
# Desired Value:
# An optimal LDR varies, but a ratio of around 80-90% is considered ideal by many. This suggests 
# that the bank has lent out most of its deposits, but still retains some liquidity. It's essential 
# to compare LDR values across the industry to get a relative understanding of a bank's performance.

def calculate_ldr(total_loans, total_deposits):
    """Calculate the Loan-to-Deposit Ratio (LDR)."""
    return total_loans / total_deposits

# Hard-coded values (These are just sample values and should be replaced with real-world data)
sample_total_loans = 80.0    # Total loans of $80,000,000, represented as 80.0
sample_total_deposits = 100.0 # Total deposits of $100,000,000, represented as 100.0

# Calculating LDR from the sample values
sample_ldr = calculate_ldr(sample_total_loans, sample_total_deposits)

print(f"Total Loans is: ${sample_total_loans:.2f} million")
print(f"Total Deposits is: ${sample_total_deposits:.2f} million")
print(f"Loan-to-Deposit Ratio (LDR) is: {sample_ldr*100:.2f}%")