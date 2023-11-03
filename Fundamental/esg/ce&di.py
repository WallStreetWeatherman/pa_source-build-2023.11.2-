# ESG Community Engagement and Development Initiatives Calculator
# ---------------------------------------------------------------
# Overview:
# Environmental, Social, and Governance (ESG) metrics reflect a company's commitment to sustainability and ethical operations.
# Community Engagement and Development Initiatives provide insight into a company's investment in local communities.
# This metric assesses investments in infrastructure, education, job creation, etc.
#
# Desired Value:
# A higher value indicates a greater commitment and investment in community development.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual investment data should be input.

class CommunityDevelopmentCalculator:
    def __init__(self, initiatives_data):
        """
        Args:
        initiatives_data (dict): Dictionary with initiative names as keys and investment amounts as values (in millions).
        """
        self.initiatives_data = initiatives_data

    def calculate_total_investment(self):
        """Calculate total investment in community development."""
        return sum(self.initiatives_data.values())

    def display_investment(self):
        """Display the calculated investment in Community Development."""
        total_investment = self.calculate_total_investment()
        print(f"Total Investment in Community Development: ${total_investment:.2f} Million")

# Hard-coded values in millions for demonstration:
initiatives_data = {
    'Local Infrastructure': 2.50,   # 2.50 million
    'Educational Programs': 0.50,   # 0.50 million
    'Job Creation': 3.00,          # 3.00 million
    'Healthcare Initiatives': 1.50 # 1.50 million
}

calculator = CommunityDevelopmentCalculator(initiatives_data)
calculator.display_investment()
