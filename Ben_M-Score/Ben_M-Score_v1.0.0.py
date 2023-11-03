def calculate_beneish_m_score(DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA):
    M = -4.84 + 0.92 * DSRI + 0.528 * GMI + 0.404 * AQI + 0.892 * SGI + 0.115 * DEPI - 0.172 * SGAI - 0.327 * LVGI + 4.679 * TATA - 0.327 * LVGI
    return M

# Example usage with arbitrary values for each variable
DSRI = 0.89
GMI = 0.78
AQI = -0.01
SGI = 1.17
DEPI = 1.05
SGAI = 1.1
LVGI = 1.2
TATA = 0.02

m_score = calculate_beneish_m_score(DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA)

print(f"The Beneish M-Score is: {m_score}")

# Interpretation
if m_score > -1.78:
    print("High likelihood of earnings manipulation.")
else:
    print("Low likelihood of earnings manipulation.")
