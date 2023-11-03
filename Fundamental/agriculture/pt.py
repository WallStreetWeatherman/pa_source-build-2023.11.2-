# Commodity Price Trends Tracker for Agricultural Products
# -------------------------------------------------------
# Overview:
# This script helps monitor the price trends of core agricultural commodities.
# It allows the user to input the price data for various commodities and then analyzes the trend.
# The trend could be rising, falling, or stable.
#
# Desired Value:
# For traders and agricultural businesses, understanding price trends is crucial.
# A rising trend might indicate a good time to sell, while a falling trend might suggest it's a good time to buy.
# Stable prices might indicate market equilibrium or low volatility.
#
# Note: This script uses hard-coded values for demonstration. In real-world applications,
# actual price data should be inputted.

class CommodityPriceTrendTracker:
    def __init__(self, commodity_prices):
        self.commodity_prices = commodity_prices

    def analyze_trend(self, prices):
        """Analyze and return the trend based on given price data."""
        if prices[-1] > prices[0]:
            return "rising"
        elif prices[-1] < prices[0]:
            return "falling"
        else:
            return "stable"

    def display_trends(self):
        """Display the price trends for each commodity."""
        for commodity, prices in self.commodity_prices.items():
            trend = self.analyze_trend(prices)
            print(f"The price trend for {commodity} is {trend}.")

# Hard-coded values
# Assume the price data is for the last 5 days for each commodity.
# Prices are in millions. Example: 1.20 means $1,200,000
commodity_data = {
    "Wheat": [1.20, 1.22, 1.21, 1.23, 1.25],
    "Corn": [0.80, 0.82, 0.81, 0.79, 0.78],
    "Soybean": [1.00, 1.00, 1.01, 1.01, 1.01]
}

tracker = CommodityPriceTrendTracker(commodity_data)
tracker.display_trends()
