# RevPAR (Revenue per Available Room) Tracker
# -------------------------------------------
# Overview:
# RevPAR is a critical metric in the hotel industry that provides insight into 
# a hotel's financial performance. By considering both occupancy rate and 
# the average daily room rate, RevPAR provides a comprehensive view of a hotel's 
# earning capability.
#
# Desired Value:
# A higher RevPAR is typically more desirable as it may indicate high occupancy, 
# a high average room rate, or both. By optimizing RevPAR, hotels can enhance 
# profitability and maintain competitive positioning.
# 
# Note: This script uses hard-coded values for demonstration. In real-world 
# applications, data from actual hotel bookings and pricing should be used.

class RevPARCalculator:
    def __init__(self, avg_daily_rate, occupancy_rate):
        self.avg_daily_rate = avg_daily_rate
        self.occupancy_rate = occupancy_rate

    def calculate_revpar(self):
        """Calculate RevPAR based on the given daily rate and occupancy rate."""
        return self.avg_daily_rate * self.occupancy_rate

    def display_revpar(self):
        """Display the calculated RevPAR value."""
        revpar = self.calculate_revpar()
        print(f"Revenue per Available Room (RevPAR): ${revpar:.2f} (per million dollars)")

# Hard-coded values
# Example: 
# avg_daily_rate = 2.00 represents an average daily room rate of $2 million.
# occupancy_rate = 0.80 represents an 80% occupancy rate.
avg_daily_rate = 2.00
occupancy_rate = 0.80

calculator = RevPARCalculator(avg_daily_rate, occupancy_rate)
calculator.display_revpar()
