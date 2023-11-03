# Average Revenue Per User (ARPU) Calculator
# -------------------------------------------
# Overview:
# ARPU represents the amount of revenue each user (or unit) generates on average.
# It's commonly used in sectors like telecommunications, software-as-a-service (SaaS), 
# and other subscription-based services to gauge revenue streams.
#
# Desired Value:
# Generally, a higher ARPU is preferred as it indicates that each user is generating more revenue.
# However, ARPU should be looked at in context with acquisition costs, churn rates, and overall 
# customer lifetime value to get a comprehensive view of business health.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual revenue and user count data should be inputted.

class ARPU_Calculator:
    def __init__(self, total_revenue, total_users):
        # Note: Values are represented such that 1 million dollars would be 1.00, 10 million is 10.00, etc.
        self.total_revenue = total_revenue  # e.g., if revenue is 5 million, input as 5.00
        self.total_users = total_users

    def calculate_arpu(self):
        """Calculate and return the ARPU."""
        return self.total_revenue / self.total_users if self.total_users != 0 else 0

    def display_arpu(self):
        """Display the ARPU."""
        arpu = self.calculate_arpu()
        print(f"Average Revenue Per User (ARPU) is: ${arpu:.2f}")

# Hard-coded values (expressed in millions where 1 million dollars is 1.00, 10 million is 10.00, etc.)
sample_total_revenue = 10.00  # Example: $10 million in revenue
sample_total_users = 20000  # Example: 20,000 users

arpu_calculator = ARPU_Calculator(sample_total_revenue, sample_total_users)
arpu_calculator.display_arpu()