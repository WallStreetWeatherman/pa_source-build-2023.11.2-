# Ad Revenue Growth Tracker
# --------------------------
# Overview:
# This script keeps a record of earnings from advertising and calculates the 
# year-over-year growth rate. By tracking this growth, businesses can assess 
# the effectiveness of their advertising strategies and the market's demand 
# for their advertising platforms.
#
# Desired Value:
# For businesses relying on advertising, higher ad revenue growth is typically
# preferable, as it indicates rising demand and possibly improving ad quality 
# or targeting. However, growth should be sustainable, and companies should be 
# wary of short-term spikes driven by factors that may not be repeatable.
# 
# Note: This script uses hard-coded values for demonstration. In real-world applications,
# actual revenue data should be inputted.

class AdRevenueGrowthTracker:
    def __init__(self, ad_revenues):
        self.ad_revenues = ad_revenues

    def calculate_growth(self, previous, current):
        """Calculate the growth rate between two values."""
        return ((current - previous) / previous) * 100 if previous else 0

    def display_growth_over_years(self):
        """Display revenue and growth for each year."""
        print("Ad Revenue Growth Summary:\n")
        prev_revenue = 0
        for year, revenue in enumerate(self.ad_revenues, 1):
            growth = self.calculate_growth(prev_revenue, revenue)
            print(f"Year {year}:")
            print(f"\tAd Revenue: ${revenue:.2f} million")
            if year > 1:  # We can't calculate growth for the first year
                print(f"\tYoY Growth Rate: {growth:.2f}%\n")
            else:
                print("\tYoY Growth Rate: N/A (First Year)\n")
            prev_revenue = revenue

# Hard-coded values
# Revenues over 5 years in millions. Example: 5.00 means $5,000,000.
ad_revenues = [5.00, 5.50, 6.10, 6.80, 7.50]  # Represents ad revenues over 5 years.

tracker = AdRevenueGrowthTracker(ad_revenues)
tracker.display_growth_over_years()
