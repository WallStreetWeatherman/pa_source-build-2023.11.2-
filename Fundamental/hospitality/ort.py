# Occupancy Rate Tracker
# -----------------------
# Overview:
# Occupancy Rate represents the percentage of all rooms in a hotel that are occupied.
# It is essential for hoteliers to monitor and optimize this metric, as it directly
# impacts revenue and can provide insights into demand and hotel performance.
#
# Desired Value:
# A higher Occupancy Rate is generally more desirable, indicating greater demand 
# and effective utilization of hotel resources.
# 
# Note: This script uses hard-coded values for demonstration. For real-world 
# applications, it's crucial to use data from actual hotel operations.

class OccupancyRateCalculator:
    def __init__(self, total_rooms, occupied_rooms):
        self.total_rooms = total_rooms
        self.occupied_rooms = occupied_rooms

    def calculate_occupancy_rate(self):
        """Calculate Occupancy Rate based on total rooms and occupied rooms."""
        return (self.occupied_rooms / self.total_rooms) * 100

    def display_occupancy_rate(self):
        """Display the calculated Occupancy Rate value."""
        occupancy_rate = self.calculate_occupancy_rate()
        print(f"Occupancy Rate: {occupancy_rate:.2f}%")

# Hard-coded values
# Example:
# total_rooms = 100 represents a hotel with 100 rooms.
# occupied_rooms = 75 represents 75 rooms currently occupied.
total_rooms = 100
occupied_rooms = 75

calculator = OccupancyRateCalculator(total_rooms, occupied_rooms)
calculator.display_occupancy_rate()
