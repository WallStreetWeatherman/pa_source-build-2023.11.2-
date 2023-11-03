import requests
import pandas as pd

def fetch_treasury_yields():
    url = "https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=year(NEW_DATE) eq 2023"
    r = requests.get(url)
    data = r.json()['d']['results']
    yield_curve = {item['MONTH']: item['BC_30YEARMATURITY'] for item in data if item['MONTH'] != None}
    return yield_curve

def interpolate_yield(yield_curve, days_to_expiry):
    closest_points = sorted(yield_curve.keys(), key=lambda x: abs(x - days_to_expiry))[:2]
    if closest_points[0] == closest_points[1]:
        return yield_curve[closest_points[0]]
    y1, y2 = yield_curve[closest_points[0]], yield_curve[closest_points[1]]
    x1, x2 = closest_points[0], closest_points[1]
    interpolated_yield = y1 + ((y2 - y1) / (x2 - x1)) * (days_to_expiry - x1)
    return interpolated_yield / 100

def main():
    print("Fetching latest Treasury yield curve data for 2023...")
    yield_curve = fetch_treasury_yields()

    days_to_expiry = float(input("Enter the number of days to expiry for the option: "))
    risk_free_rate = interpolate_yield(yield_curve, days_to_expiry)
    
    print(f"Approximate risk-free rate for an option with {days_to_expiry} days to expiry is: {risk_free_rate:.5f}")

if __name__ == "__main__":
    main()
