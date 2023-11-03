# Average Length of Stay (ALOS) Tracker
# -------------------------------------
# Overview:
# This script tracks the average number of days patients spend in a healthcare facility. 
# ALOS can provide insights into the quality of care, resource utilization, and overall 
# operational efficiency of a healthcare facility.
#
# Desired Value:
# Too high ALOS may indicate inefficiencies, potential complications, or lack of post-care 
# options, while a very low ALOS may suggest premature discharges potentially leading to 
# higher readmissions. Therefore, healthcare providers should aim for an optimal ALOS 
# based on their patient profile and the nature of treatments provided.
# 
# Note: This script uses hard-coded values for demonstration. In real-world applications,
# actual patient data should be inputted.

class AverageLengthOfStayTracker:
    def __init__(self, lengths_of_stay):
        self.lengths_of_stay = lengths_of_stay

    def calculate_average_length(self):
        """Calculate the average length of stay based on provided data."""
        total_length = sum(self.lengths_of_stay)
        total_patients = len(self.lengths_of_stay)
        return total_length / total_patients if total_patients else 0

    def display_average_length(self):
        """Display the calculated average length of stay."""
        average_length = self.calculate_average_length()
        print(f"Average Length of Stay: {average_length:.2f} days")

# Hard-coded values
# Example: [2.00, 3.50, 4.00] represents lengths of stay for three patients 
# (2 million days, 3.5 million days, and 4 million days respectively).
lengths_of_stay = [2.00, 3.50, 4.00]  # This is just an exaggerated example for demonstration.

tracker = AverageLengthOfStayTracker(lengths_of_stay)
tracker.display_average_length()
