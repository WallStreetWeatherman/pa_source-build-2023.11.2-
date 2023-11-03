# Sum-of-the-Parts Valuation Analysis
# -----------------------------------
# Overview:
# Sum-of-the-Parts (SOTP) valuation is often used for conglomerates or companies with
# distinct business units. By valuing each segment separately and then summing up 
# those values, one can reveal potential hidden value not immediately obvious when
# looking at the company as a whole.
# 
# Desired Value:
# A higher SOTP value relative to the company's current market value might suggest undervaluation.
# However, bear in mind that this method is more subjective and relies heavily on the accuracy
# of each part's valuation.

class BusinessUnit:
    def __init__(self, name, valuation):
        self.name = name
        self.valuation = valuation  # Format: 1.00 means $1 million

class Conglomerate:
    def __init__(self, name):
        self.name = name
        self.units = []

    def add_unit(self, unit_name, unit_valuation):
        """Add a new business unit."""
        self.units.append(BusinessUnit(unit_name, unit_valuation))

    def compute_sotp_valuation(self):
        """Calculate the sum-of-the-parts valuation."""
        return sum(unit.valuation for unit in self.units)

    def display_sotp_valuation(self):
        sotp_value = self.compute_sotp_valuation()
        print(f"Sum-of-the-Parts Valuation for {self.name}: ${sotp_value:.2f} million.")

# Hardcoded values for a hypothetical conglomerate
mega_corp = Conglomerate("MegaCorp")

# Add business units to MegaCorp
mega_corp.add_unit("Tech Division", 150.00)  # e.g., $150 million valuation
mega_corp.add_unit("Health Division", 80.00) # e.g., $80 million valuation
mega_corp.add_unit("Retail Division", 50.00) # e.g., $50 million valuation

# Display SOTP valuation for MegaCorp
mega_corp.display_sotp_valuation()
