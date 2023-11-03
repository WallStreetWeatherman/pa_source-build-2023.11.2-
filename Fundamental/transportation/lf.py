# Airline Load Factor Calculator
# ------------------------------
# Overview:
# This script calculates the Load Factor for airlines. Load Factor is a measure of 
# how well an airline fills its seats. It's an indicator of both the airline's 
# efficiency and its ability to generate revenue.
#
# Desired Value:
# Higher Load Factors are generally more desirable for airlines, indicating that 
# they are filling a larger percentage of their seats with paying passengers. However, 
# extremely high Load Factors might indicate that the airline has little room to 
# accommodate increased demand or to re-accommodate passengers from canceled flights.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual seating and passenger data for the respective airline should be inputted.

class LoadFactorCalculator:
    def __init__(self, total_seats, occupied_seats):
        # Convert seat numbers from millions representation to actual values
        # For instance, 1.00 means 1 million seats
        self.total_seats = total_seats * 10**6
        self.occupied_seats = occupied_seats * 10**6

    def calculate_load_factor(self):
        """Calculate and return the Load Factor in percentage."""
        if self.total_seats == 0:
            return 0.0  # Return 0% if total seats is 0 to avoid division by zero
        return (self.occupied_seats / self.total_seats) * 100

    def display_load_factor(self):
        """Display the calculated Load Factor."""
        factor = self.calculate_load_factor()
        print(f"Load Factor: {factor:.2f}%")

# Hard-coded values
sample_total_seats = 1.50  # Example: 1.5 million total seats available
sample_occupied_seats = 1.20  # Example: 1.2 million seats occupied by passengers

load_factor_calculator = LoadFactorCalculator(sample_total_seats, sample_occupied_seats)
load_factor_calculator.display_load_factor()
