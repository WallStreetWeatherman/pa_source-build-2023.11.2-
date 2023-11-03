import requests
import json

def fetch_treasury_yields():
    """
    Fetches U.S. Treasury yield curve data.
    """
    url = "https://api.stlouisfed.org/fred/series/observations?series_id=GS1&realtime_start=2023-01-01&api_key=1507e0687be4cf788697d5397425aa96&file_type=json"
    r = requests.get(url)
    
    # Print the full JSON response to debug
    print(f"Full JSON Response: {json.dumps(r.json(), indent=4)}")
    
    try:
        data = r.json()['observations']
        return {d['date']: float(d['value']) for d in data if 'value' in d}
    except KeyError:
        print("Could not find 'observations' key in the JSON response.")
        return {}


def interpolate_rate(r_short, t_short, r_long, t_long, t_target):
    """
    Linearly interpolates the yield for the target time period.
    """
    return r_short + ((t_target - t_short) / (t_long - t_short)) * (r_long - r_short)

def main():
    # Fetch U.S. Treasury yield curve data (example data here, replace with fetched data)
    yield_curve = fetch_treasury_yields()

    if '3_month' in yield_curve:
        r_3month = yield_curve['3_month']
        print(f"3-month yield: {r_3month}%")
    else:
        print("Could not find '3_month' key in the yield curve data.")

    r_1year = yield_curve['1_year']
    
    # Option expiration period in months
    t_option_months = 5
    t_option_years = t_option_months / 12.0
    
    # Time to expiration for 3-month and 1-year T-Bills in years
    t_3month = 3 / 12.0
    t_1year = 1.0
    
    # Interpolate the yield for the option expiration period
    r_option = interpolate_rate(r_3month, t_3month, r_1year, t_1year, t_option_years)
    
    # Current inflation rate (e.g., 2%)
    inflation_rate = 0.02
    
    # Calculate the real risk-free rate
    real_risk_free_rate = r_option - inflation_rate
    
    print(f"Interpolated yield for {t_option_months}-month option: {r_option * 100:.2f}%")
    print(f"Real risk-free rate: {real_risk_free_rate * 100:.2f}%")

if __name__ == "__main__":
    main()
