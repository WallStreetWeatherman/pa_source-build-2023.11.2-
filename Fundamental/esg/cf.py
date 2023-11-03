# ESG Carbon Footprint Calculator
# ---------------------------------------
# Overview:
# Environmental, Social, and Governance (ESG) metrics assess a company's behavior along these three factors.
# Carbon Footprint, a key ESG metric, quantifies the total emissions of greenhouse gases by a company.
# It's an indicator of the company's environmental impact.
#
# Formula: Carbon Footprint = Sum of (emission factor * activity data) for all emission sources
#
# Desired Value:
# A lower Carbon Footprint is more desirable, indicating environmentally responsible practices.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual emission and activity data should be input.

class CarbonFootprintCalculator:
    def __init__(self, emission_factors, activity_data):
        """
        Args:
        emission_factors (dict): Dictionary with emission sources as keys and emission factors as values (in GHG/Unit).
        activity_data (dict): Dictionary with emission sources as keys and activity data as values (in Units).
        """
        self.emission_factors = emission_factors
        self.activity_data = activity_data

    def calculate_footprint(self):
        """Calculate total Carbon Footprint."""
        total_footprint = 0
        for source, emission_factor in self.emission_factors.items():
            total_footprint += emission_factor * self.activity_data.get(source, 0)
        # Convert total carbon footprint so that 1 million units becomes 1.00, 10 million units becomes 10.00, etc.
        return total_footprint / 1000000

    def display_footprint(self):
        """Display the calculated Carbon Footprint."""
        footprint = self.calculate_footprint()
        print(f"Total Carbon Footprint: {footprint:.2f} (in Million GHG Units)")

# Hard-coded values for demonstration:
# Example emission factors (in GHG/Unit): Factory emissions, transportation emissions, etc.
# Example activity data (in Units): Amount of production, miles traveled, etc.
emission_factors = {
    'factory_emissions': 2000,  # GHG/Unit of production
    'transportation_emissions': 150  # GHG/Mile traveled
}

activity_data = {
    'factory_emissions': 500,  # Units of production
    'transportation_emissions': 10000  # Miles traveled
}

calculator = CarbonFootprintCalculator(emission_factors, activity_data)
calculator.display_footprint()
