# Churn Rate Calculator
# ------------------------------
# Overview:
# Churn Rate indicates the percentage of subscribers or customers who stop using 
# a product or service during a given time period. It's often used by subscription-based 
# services like telecommunications, SaaS, and other online platforms to gauge customer retention.
#
# Desired Value:
# Generally, a lower churn rate is better, as it means fewer customers are leaving the service.
# A higher churn rate might indicate customer dissatisfaction, higher competition, 
# or other issues affecting retention.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual subscriber data and churn data should be inputted.

class ChurnRateCalculator:
    def __init__(self, start_subscribers, churned_subscribers):
        # Note: Values are represented in terms of actual count (e.g., 10,000 subscribers is 10000)
        self.start_subscribers = start_subscribers
        self.churned_subscribers = churned_subscribers

    def calculate_churn_rate(self):
        """Calculate and return the churn rate percentage."""
        return (self.churned_subscribers / self.start_subscribers) * 100 if self.start_subscribers != 0 else 0

    def display_churn_rate(self):
        """Display the churn rate."""
        churn_rate = self.calculate_churn_rate()
        print(f"Churn Rate is: {churn_rate:.2f}%")

# Hard-coded values
sample_start_subscribers = 10000  # Example: Start with 10,000 subscribers
sample_churned_subscribers = 500  # Example: 500 subscribers left the service

churn_calculator = ChurnRateCalculator(sample_start_subscribers, sample_churned_subscribers)
churn_calculator.display_churn_rate()