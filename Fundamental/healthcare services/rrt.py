# Reimbursement Rates Tracker
# ---------------------------
# Overview:
# This script tracks the rates at which insurance providers compensate healthcare 
# service providers for their services. Monitoring these rates helps in gauging 
# the profitability and competitive position of the service provider.
#
# Desired Value:
# Higher reimbursement rates are typically preferred, signaling greater revenue 
# for services. However, excessively high rates might deter patients if they 
# result in higher out-of-pocket expenses. Providers should strive for rates 
# that reflect the quality and cost of care without being prohibitively expensive 
# for patients.
# 
# Note: This script uses hard-coded values for demonstration. In real-world 
# applications, data from actual contracts/agreements should be utilized.

class ReimbursementRatesTracker:
    def __init__(self, rates):
        self.rates = rates

    def calculate_average_rate(self):
        """Calculate the average reimbursement rate based on provided data."""
        total_rate = sum(self.rates)
        total_entries = len(self.rates)
        return total_rate / total_entries if total_entries else 0

    def display_average_rate(self):
        """Display the calculated average reimbursement rate."""
        average_rate = self.calculate_average_rate()
        print(f"Average Reimbursement Rate: ${average_rate:.2f} (per million dollars of service)")

# Hard-coded values
# Example: [1.50, 2.25, 1.75] represent reimbursement rates for three services
# ($1.5 million, $2.25 million, and $1.75 million respectively).
rates = [1.50, 2.25, 1.75]

tracker = ReimbursementRatesTracker(rates)
tracker.display_average_rate()
