def calculate_nav(total_assets, total_liabilities, shares_outstanding):
    """Calculate the Net Asset Value (NAV) for an investment fund."""
    if shares_outstanding == 0:
        raise ValueError("Number of shares outstanding cannot be zero.")
    nav = (total_assets - total_liabilities) / shares_outstanding
    return nav

def main():
    # Hard-coded values
    total_assets = 1000000  # Example value, change to your desired value
    total_liabilities = 200000  # Example value, change to your desired value
    shares_outstanding = 5000  # Example value, change to your desired value

    try:
        # Calculate NAV
        nav = calculate_nav(total_assets, total_liabilities, shares_outstanding)
        
        # Print the result
        print(f"Net Asset Value (NAV) per share: ${nav:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
