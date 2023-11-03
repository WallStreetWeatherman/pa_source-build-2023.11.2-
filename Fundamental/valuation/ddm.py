# Dividend Discount Model (DDM) Calculator
# ----------------------------------------
# Overview:
# The Dividend Discount Model (DDM) is a specialized form of the Discounted Cash Flow (DCF) method 
# for valuing companies that pay dividends. It calculates the present value of expected future 
# dividends to determine a company's intrinsic value.
#
# Desired Value:
# A higher calculated intrinsic value indicates a potentially undervalued stock, while a lower 
# intrinsic value might suggest overvaluation. However, the real-world stock price should be compared 
# to the DDM value for context.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# financial data should be sourced from the company's financial statements and reliable forecasts.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for a hypothetical company
dividend_next_year = convert_to_actual_value(0.05)  # Expected dividend for the next year in actual value
growth_rate = 0.05  # Expected annual dividend growth rate (5% growth rate as an example)
discount_rate = 0.10  # Investor's required rate of return or discount rate (10% as an example)

def ddm_calculator(dividend_next_year, growth_rate, discount_rate):
    intrinsic_value_per_share = dividend_next_year / (discount_rate - growth_rate)
    return intrinsic_value_per_share

intrinsic_value = ddm_calculator(dividend_next_year, growth_rate, discount_rate)

# Output the result
print("Dividend Discount Model (DDM) Calculation:\n")
print("Expected Dividend for Next Year: ${:,.2f}".format(dividend_next_year / 1000000))
print("Expected Annual Dividend Growth Rate: {:.2%}".format(growth_rate))
print("Discount Rate (Required Rate of Return): {:.2%}".format(discount_rate))
print("\nIntrinsic Value per Share: ${:,.2f}".format(intrinsic_value / 1000000))

