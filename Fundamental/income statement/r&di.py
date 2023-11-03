# R&D Intensity Calculator
# ------------------------------
# Overview:
# The R&D Intensity metric shows the significance of a company's investment in research and development 
# in relation to its sales. For innovative companies, especially in sectors like tech or pharma, 
# a higher R&D Intensity can suggest an emphasis on innovation and future growth.
#
# Formula:
# R&D Intensity = (R&D Expenditure / Sales) * 100
#
# Desired Value:
# The ideal value for R&D Intensity depends on the industry. In sectors where innovation is vital, 
# a high R&D Intensity may be viewed positively, as it indicates strong investment in future growth. 
# However, excessive spending without correlating benefits can be seen negatively.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# R&D Expenditure for the period (in $1M)
rd_expenditure = 5.00  # Example value representing $5 million

# Sales for the period (in $1M)
sales = 50.00  # Example value representing $50 million

# Calculate R&D Intensity
rd_intensity = (rd_expenditure / sales) * 100

# Output the results
print(f"R&D Expenditure (in $1M): ${rd_expenditure:.2f}M")
print(f"Sales (in $1M): ${sales:.2f}M")
print(f"R&D Intensity: {rd_intensity:.2f}%")

if rd_intensity > 15:  # Arbitrary threshold, adjust based on industry benchmarks
    print("The company has a high R&D Intensity, indicating strong investment in research and potential future growth.")
    print("\nFactors possibly contributing to a higher R&D Intensity include:")
    print("- A strategic emphasis on innovation to capture new market opportunities.")
    print("- Entry into a new market segment that requires significant research and product development.")
    print("- Strong financial health that allows for aggressive R&D spending.")
    print("- Operating in a high-tech or fast-evolving industry where staying ahead of competitors is crucial.")
else:
    print("The company has a moderate to low R&D Intensity, suggesting cautious or balanced spending on research relative to sales.")
    print("\nFactors that might lead to moderate or low R&D Intensity include:")
    print("- An established product portfolio that doesn't require significant incremental R&D.")
    print("- A focus on expanding current product lines rather than developing new ones.")
    print("- Financial constraints or a strategic decision to allocate capital elsewhere.")
    print("- Operating in a mature or stable industry where product differentiation is less reliant on constant innovation.")
