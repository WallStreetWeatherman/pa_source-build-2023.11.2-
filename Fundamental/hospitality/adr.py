# Average Daily Rate (ADR) Tracker
# --------------------------------
# Overview:
# ADR represents the average rental income per occupied room in a given period.
# It provides insights into a hotel's pricing strategy and its ability to 
# command room rates relative to its competitors.
#
# Desired Value:
# Higher ADR values are generally more desirable as they indicate the ability 
# to earn more revenue per occupied room, which could be due to factors such 
# as higher demand, better quality/service, or effective pricing strategies.
# 
# Note: This script uses hard-coded values for demonstration. For real-world 
# applications, it's crucial to use data derived from actual room sales.

class ADRCalculator:
    def __init__(self, total_room_revenue, number_of_rooms_sold):
        self.total_room_revenue = total_room_revenue
        self.number_of_rooms_sold = number_of_rooms_sold

    def calculate_adr(self):
        """Calculate ADR based on total room revenue and number of rooms sold."""
        return self.total_room_revenue / self.number_of_rooms_sold

    def display_adr(self):
        """Display the calculated ADR value."""
        adr = self.calculate_adr()
        print(f"Average Daily Rate (ADR): ${adr:.2f} (per million dollars)")

# Hard-coded values
# Example:
# total_room_revenue = 15.00 represents total room revenue of $15 million.
# number_of_rooms_sold = 7 represents 7 rooms sold.
total_room_revenue = 15.00
number_of_rooms_sold = 7

calculator = ADRCalculator(total_room_revenue, number_of_rooms_sold)
calculator.display_adr()
