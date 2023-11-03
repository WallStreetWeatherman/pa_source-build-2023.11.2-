# Price to Research Ratio Calculation
# -----------------------------------
# Overview:
# The Price to Research Ratio provides insights into a company's valuation relative to its investment in research and development (R&D). 
# For companies where R&D is a significant factor, this ratio might be a better indicator of value than traditional P/E ratios.
#
# Desired Value:
# A lower Price to Research Ratio could indicate that the company is undervalued given its investment in R&D, 
# suggesting potential upside. Conversely, a higher ratio may signal overvaluation. However, it's important 
# to compare this ratio with peers in the same industry for meaningful insights.

# Hardcoded values for the company
current_market_cap = 3029.00 # Market Cap in Tikr
annual_r_and_d_expenditure = 5.00

# Hardcoded values for the industry average
industry_avg_market_cap = 105.00  # Assuming for the sake of example
industry_avg_r_and_d_expenditure = 5.50  # Assuming for the sake of example

def calculate_price_to_research(market_cap, r_and_d):
    """Calculate Price to Research Ratio."""
    return market_cap / r_and_d

company_price_to_research_ratio = calculate_price_to_research(current_market_cap, annual_r_and_d_expenditure)
industry_avg_price_to_research_ratio = calculate_price_to_research(industry_avg_market_cap, industry_avg_r_and_d_expenditure)

print(f"Company's Price to Research Ratio: {company_price_to_research_ratio:.2f}")
print(f"Industry Average Price to Research Ratio: {industry_avg_price_to_research_ratio:.2f}")

print("\nFactors and Scenarios potentially influencing the Price to Research Ratio:")
print("- **R&D Efficiency:** Not all R&D investments yield productive outcomes. Companies that efficiently translate R&D into marketable products may warrant higher valuations.")
print("- **Industry Disruption Potential:** In industries poised for disruption, significant R&D investment might indicate a company's commitment to leading innovation.")
print("- **Competitive Landscape:** Companies that invest heavily in R&D in highly competitive markets might be aiming to secure a technological edge or meet regulatory demands.")
print("- **R&D Capitalization vs. Expensing:** Accounting treatments can differ; some companies might capitalize a portion of R&D, affecting the immediate impact on earnings.")
print("- **Product Lifecycle:** If a company's key products are nearing the end of their lifecycle without a clear next-generation product, heavy R&D investment might be critical.")
print("- **Patent Portfolio:** The quality and potential commercial value of a company's patents can affect how the market values its R&D investment.")
print("- **Economic Conditions:** During economic downturns, companies slashing R&D might be viewed negatively, as this could impact long-term growth.")
print("- **Regulatory Environment:** In industries like pharmaceuticals, regulatory hurdles can mean even significant R&D investments might not lead to profitable outcomes.")

print("\nImplications:")
if company_price_to_research_ratio < industry_avg_price_to_research_ratio:
    print("The company's valuation relative to its R&D investment is lower than industry peers, potentially signaling undervaluation. However, it's crucial to evaluate the effectiveness of its R&D activities and future growth prospects.")
elif company_price_to_research_ratio == industry_avg_price_to_research_ratio:
    print("The company's valuation in relation to its R&D expenditure aligns with the industry norm. A deep dive into the nature and outcomes of its R&D activities would provide more clarity on its growth potential.")
else:
    print("The company's higher Price to Research Ratio compared to the industry suggests a premium valuation relative to its R&D spend. Investors should scrutinize the potential reasons behind this premium and whether it's justified.")
