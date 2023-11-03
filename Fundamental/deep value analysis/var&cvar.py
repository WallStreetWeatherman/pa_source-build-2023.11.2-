# Value at Risk (VaR) and Conditional VaR Analysis
# ------------------------------------------------
# Overview:
# VaR and CVaR are measures traditionally used for portfolio risk management to 
# understand the potential maximum loss over a given time horizon at a specific confidence level.
# Here, we adapt them for an individual investment to provide insights into worst-case scenarios.
#
# Desired Value:
# Lower VaR and CVaR values indicate a lower potential for extreme negative returns. 
# A lower value is preferable as it suggests lower risk.

import numpy as np

class InvestmentRisk:
    def __init__(self, investment_name, historical_returns):
        self.investment_name = investment_name
        self.historical_returns = np.array(historical_returns)

    def compute_var(self, confidence_level):
        """Calculate Value at Risk (VaR) at a given confidence level."""
        return -np.percentile(self.historical_returns, 100 - confidence_level)

    def compute_cvar(self, confidence_level):
        """Calculate Conditional Value at Risk (CVaR) at a given confidence level."""
        var = self.compute_var(confidence_level)
        return -np.mean(self.historical_returns[self.historical_returns < -var])

    def display_analysis(self, confidence_level=95):
        var = self.compute_var(confidence_level)
        cvar = self.compute_cvar(confidence_level)
        print(f"Value at Risk (VaR) for {self.investment_name} at {confidence_level}% confidence: ${var:.2f} million.")
        print(f"Conditional Value at Risk (CVaR) for {self.investment_name} at {confidence_level}% confidence: ${cvar:.2f} million.")

# Hardcoded values for a hypothetical investment's historical returns (e.g., past 12 months)
# Positive values indicate profits, and negative values indicate losses. 
# E.g., 0.05 denotes a $5 million profit, -0.10 denotes a $10 million loss.
historical_returns = [0.05, 0.02, -0.01, 0.04, -0.03, 0.01, -0.10, 0.03, 0.02, -0.08, 0.01, 0.04]

investment_analysis = InvestmentRisk("InvestmentA", historical_returns)
investment_analysis.display_analysis()
