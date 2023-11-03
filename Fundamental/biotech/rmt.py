# Regulatory Milestones Tracker
# ------------------------------
# Overview:
# This script helps in tracking regulatory milestones crucial for drug approvals.
# It is used mainly in the pharmaceutical and biotech sectors where specific dates
# can represent significant events, such as clinical trial starts, results, or regulatory reviews.
#
# Desired Value:
# For those in the pharma or biotech sectors, it's imperative to have these dates tracked and monitored.
# Delays or advancements in these dates can have implications on company performance, stock prices, and drug rollout.
#
# Note: This script uses hard-coded values for demonstration and real-world data should be inputted as required.

import datetime

class Drug:
    def __init__(self, name):
        self.name = name
        self.milestones = {}

    def add_milestone(self, milestone_name, date):
        """Add a regulatory milestone date for the drug."""
        if not isinstance(date, datetime.date):
            raise ValueError("Provided date is not a valid datetime.date object.")
        self.milestones[milestone_name] = date

    def get_milestone(self, milestone_name):
        """Retrieve a regulatory milestone date for the drug."""
        return self.milestones.get(milestone_name, None)

    def display_milestones(self):
        """Display all milestones for the drug."""
        print(f"Milestones for {self.name}:")
        for milestone, date in self.milestones.items():
            formatted_date = date.strftime("%Y-%m-%d")
            print(f"{milestone}: {formatted_date}")

# Hard-coded values (expressed in millions where 1 million dollars is 1.00, 10 million is 10.00, etc.)
# Sample drug with its regulatory milestones
sample_drug = Drug("MedicineX")

# Adding regulatory milestones for the sample drug
sample_drug.add_milestone("Clinical Trial Start", datetime.date(2023, 1, 15))
sample_drug.add_milestone("Clinical Trial Phase II Results", datetime.date(2023, 7, 30))
sample_drug.add_milestone("FDA Review Date", datetime.date(2024, 2, 20))

# Displaying milestones
sample_drug.display_milestones()

