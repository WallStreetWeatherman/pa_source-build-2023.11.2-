# Combined Ratio (for insurance)
# ------------------------------
# Overview:
# The combined ratio is a key metric for the insurance industry, giving insight into profitability.
# It measures the sum of loss and expense ratios. If it's over 100%, the insurance company 
# is paying out more than it earns from premiums, indicating a potential underwriting loss.
# However, insurance companies can still be profitable through investment income.
#
# Desired Value:
# A combined ratio of less than 100% is usually favorable, indicating an underwriting profit.
# If it exceeds 100%, the company may be incurring an underwriting loss. But, keep in mind, 
# investment income may offset this.

def calculate_combined_ratio(losses, expenses, earned_premiums):
    """Calculate the Combined Ratio for insurance."""
    loss_ratio = losses / earned_premiums
    expense_ratio = expenses / earned_premiums
    return loss_ratio + expense_ratio

# Hard-coded values (replace with real-world data)
sample_losses = 60.0          # Incurred losses of $60,000,000, represented as 60.0
sample_expenses = 30.0        # Incurred expenses of $30,000,000, represented as 30.0
sample_earned_premiums = 100.0 # Earned premiums of $100,000,000, represented as 100.0

# Calculating Combined Ratio from the sample values
sample_combined_ratio = calculate_combined_ratio(sample_losses, sample_expenses, sample_earned_premiums)

print(f"Losses are: ${sample_losses:.2f} million")
print(f"Expenses are: ${sample_expenses:.2f} million")
print(f"Earned Premiums are: ${sample_earned_premiums:.2f} million")
print(f"Combined Ratio is: {sample_combined_ratio*100:.2f}%")