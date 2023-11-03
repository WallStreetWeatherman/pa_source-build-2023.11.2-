def calculate_AQI(this_year_non_current_assets, this_year_ppe, last_year_non_current_assets, last_year_ppe, last_year_total_assets):
    """
    Calculate Asset Quality Index (AQI).
    
    Parameters:
        this_year_non_current_assets (float): This year's Non-Current Assets.
        this_year_ppe (float): This year's Property, Plant, and Equipment.
        last_year_non_current_assets (float): Last year's Non-Current Assets.
        last_year_ppe (float): Last year's Property, Plant, and Equipment.
        last_year_total_assets (float): Last year's Total Assets.
        
    Returns:
        float: Asset Quality Index (AQI).
    """
    
    this_year_aq = this_year_non_current_assets - this_year_ppe
    last_year_aq = last_year_non_current_assets - last_year_ppe
    
    AQI = (this_year_aq - last_year_aq) / last_year_total_assets
    
    return AQI

# Example usage:
this_year_non_current_assets = 55_146_000_000
this_year_ppe = 2_002_000_000
last_year_non_current_assets = 56_041_000_000
last_year_ppe = 1_973_000_000
last_year_total_assets = 67_580_000_000

AQI = calculate_AQI(this_year_non_current_assets, this_year_ppe, last_year_non_current_assets, last_year_ppe, last_year_total_assets)

print(f"The Asset Quality Index (AQI) is: {AQI}")