# Land Utilization Tracker for Agriculture and Real Estate
# -------------------------------------------------------
# Overview:
# This script monitors and analyzes land utilization patterns. It categorizes
# different types of land usages and provides a summary of how land is used.
#
# Desired Value:
# For agricultural businesses, optimized land use can lead to better crop yields and higher profits.
# In real estate, understanding land utilization can inform zoning decisions and development potential.
# Ideally, a balanced use of land that aligns with the goals of the business or community is desired.
#
# Note: This script uses hard-coded values for demonstration. In real-world applications,
# actual land utilization data should be inputted.

class LandUtilizationTracker:
    def __init__(self, land_data):
        self.land_data = land_data

    def display_summary(self):
        """Display a summary of land utilization."""
        total_land = sum(self.land_data.values())
        print(f"Total Land: {total_land} million acres\n")
        print("Land Utilization Summary:")
        for usage, acres in self.land_data.items():
            percentage = (acres / total_land) * 100
            print(f"{usage}: {acres} million acres ({percentage:.2f}%)")

    def suggest_optimization(self):
        """Provide suggestions based on the land utilization."""
        # This can be more complex based on real-world needs.
        if self.land_data.get("Crop Land") > self.land_data.get("Pasture", 0):
            print("\nSuggestion: Consider converting some crop land into pasture for better diversity and soil health.")
        else:
            print("\nSuggestion: Evaluate the possibility of using more land for crops to increase yields and profit.")

# Hard-coded values
# Land utilization data in millions of acres. Example: 2.50 means 2,500,000 acres.
land_data = {
    "Crop Land": 2.50,  # Land used for crops
    "Pasture": 1.50,    # Land used as pasture
    "Forest": 3.00,     # Land covered with forests
    "Urban": 0.20,      # Land used for urban development
    "Wetlands": 0.10    # Wetlands
}

tracker = LandUtilizationTracker(land_data)
tracker.display_summary()
tracker.suggest_optimization()
