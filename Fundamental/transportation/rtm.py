# Revenue Ton Mile (RTM) Calculator for Transportation Companies
# --------------------------------------------------------------
# Overview:
# This script calculates the Revenue Ton Mile (RTM) which is a metric used 
# primarily in the transportation industry. It represents the transportation of 
# one ton of cargo for one mile. It's a useful metric to gauge the efficiency of 
# a transportation company's operations.
#
# Desired Value:
# Higher RTM indicates that the transportation company is generating more 
# revenue from transporting goods. An increasing RTM over time can be an 
# indicator of a company's growing operational efficiency and demand.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual transportation and revenue data should be inputted.

class RTMCalculator:
    def __init__(self, tonnage, miles_traveled, revenue):
        # Convert revenue from millions representation to actual values
        # For instance, 1.00 means 1 million dollars
        self.tonnage = tonnage  # tons of cargo
        self.miles_traveled = miles_traveled  # miles the cargo was transported
        self.revenue = revenue * 10**6  # revenue generated from transportation in dollars

    def calculate_rtm(self):
        """Calculate and return the Revenue Ton Mile."""
        return self.tonnage * self.miles_traveled

    def revenue_per_rtm(self):
        """Calculate and return the Revenue per RTM."""
        rtm = self.calculate_rtm()
        if rtm == 0:
            return 0.0  # Return 0 if RTM is 0 to avoid division by zero
        return self.revenue / rtm

    def display_rtm_and_revenue(self):
        """Display the calculated RTM and Revenue per RTM."""
        rtm = self.calculate_rtm()
        revenue_rtm = self.revenue_per_rtm()
        print(f"Revenue Ton Mile (RTM): {rtm} ton-miles")
        print(f"Revenue per RTM: ${revenue_rtm:.2f} per ton-mile")

# Hard-coded values
sample_tonnage = 50000  # Example: 50,000 tons of cargo transported
sample_miles_traveled = 1000  # Example: The cargo was transported for 1,000 miles
sample_revenue = 2.50  # Example: The transportation generated $2.5 million in revenue

rtm_calculator = RTMCalculator(sample_tonnage, sample_miles_traveled, sample_revenue)
rtm_calculator.display_rtm_and_revenue()
