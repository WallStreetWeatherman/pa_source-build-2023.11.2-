# Patient Volume Growth Tracker
# -----------------------------
# Overview:
# This script monitors the changes in the number of patients over a set period. 
# By evaluating this growth, healthcare institutions can gauge the effectiveness 
# of their services, marketing strategies, or broader trends in healthcare demand.
#
# Desired Value:
# A growing patient volume indicates increasing demand or effectiveness of services.
# However, too rapid an increase might strain resources. On the other hand, a 
# declining volume could suggest problems that need attention. Ideally, healthcare 
# providers would aim for sustainable growth.
# 
# Note: This script uses hard-coded values for demonstration. In real-world applications,
# actual patient data should be inputted.

class PatientVolumeGrowthTracker:
    def __init__(self, patient_volumes):
        self.patient_volumes = patient_volumes

    def calculate_growth(self, previous, current):
        """Calculate the growth rate between two values."""
        return ((current - previous) / previous) * 100 if previous else 0

    def display_growth_over_periods(self):
        """Display patient volume and growth for each period."""
        print("Patient Volume Growth Summary:\n")
        prev_volume = 0
        for period, volume in enumerate(self.patient_volumes, 1):
            growth = self.calculate_growth(prev_volume, volume)
            print(f"Period {period}:")
            print(f"\tPatients: {volume*1000000:.0f}")  # Convert back to actual numbers
            if period > 1:  # We can't calculate growth for the first period
                print(f"\tVolume Growth Rate: {growth:.2f}%\n")
            else:
                print("\tVolume Growth Rate: N/A (First Period)\n")
            prev_volume = volume

# Hard-coded values
# Patient volumes over 5 periods. Example: 1.00 means 1,000,000 patients.
patient_volumes = [1.00, 1.10, 1.05, 1.15, 1.20]  # Represents patient volumes over 5 periods.

tracker = PatientVolumeGrowthTracker(patient_volumes)
tracker.display_growth_over_periods()
