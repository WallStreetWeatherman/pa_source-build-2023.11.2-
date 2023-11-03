# Subscriber Growth Rate Tracker for Subscription-Based Services
# --------------------------------------------------------------
# Overview:
# This script monitors and analyzes the growth rate of subscribers over time.
# Subscriber growth rate provides insights into the attractiveness of the service 
# and indicates potential future revenues.
#
# Desired Value:
# For subscription-based services, a high positive growth rate is generally desirable 
# as it suggests more users are adopting the service, which in turn leads to higher revenues.
# A decreasing or negative growth rate might indicate customer dissatisfaction or 
# increased competition.
#
# Note: This script uses hard-coded values for demonstration. In real-world applications,
# actual subscriber data should be inputted.

class SubscriberGrowthRateTracker:
    def __init__(self, subscriber_data):
        self.subscriber_data = subscriber_data

    def calculate_growth_rate(self, old, new):
        """Calculate growth rate."""
        return ((new - old) / old) * 100

    def display_growth_rate(self):
        """Display growth rate for each period."""
        previous_subscribers = self.subscriber_data[0]
        print(f"Initial Subscribers: {previous_subscribers * 1_000_000:.0f}\n")
        print("Subscriber Growth Rate Summary:")

        for i, current_subscribers in enumerate(self.subscriber_data[1:], 1):
            growth_rate = self.calculate_growth_rate(previous_subscribers, current_subscribers)
            print(f"Year {i}: {growth_rate:.2f}%")
            previous_subscribers = current_subscribers

# Hard-coded values
# Subscriber data over years in millions. Example: 1.50 means 1,500,000 subscribers.
subscriber_data = [1.50, 1.80, 2.10, 2.50, 2.85]  # Represents subscribers over 5 years.

tracker = SubscriberGrowthRateTracker(subscriber_data)
tracker.display_growth_rate()
