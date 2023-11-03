# Magic Formula Investing Strategy
# --------------------------------
# Overview:
# The Magic Formula, proposed by Joel Greenblatt, is a stock screening method to find good quality companies at a discount.
# It ranks companies based on two factors: earnings yield and return on capital.
# Companies are ranked separately on these factors, and the two rankings are combined for a final ranking.
#
# Desired Value:
# The goal is to identify companies that rank highly on both earnings yield (indicating they might be undervalued)
# and return on capital (indicating they have a competitive advantage or are of high quality). 

class Company:
    def __init__(self, name, earnings, enterprise_value, capital_employed):
        self.name = name
        self.earnings = earnings  # Operating earnings or EBIT
        self.enterprise_value = enterprise_value  # EV = Market cap + debt - cash
        self.capital_employed = capital_employed  # Total assets - current liabilities
        
    @property
    def earnings_yield(self):
        return self.earnings / self.enterprise_value

    @property
    def return_on_capital(self):
        return self.earnings / self.capital_employed

def rank_companies_on_metric(companies, metric_func):
    """Rank companies based on the given metric. Lower rank is better."""
    return sorted(companies, key=metric_func)

def magic_formula_ranking(companies):
    ranked_by_earnings_yield = rank_companies_on_metric(companies, lambda x: -x.earnings_yield)  # Higher is better
    ranked_by_roc = rank_companies_on_metric(companies, lambda x: -x.return_on_capital)  # Higher is better
    
    scores = {}
    for idx, company in enumerate(ranked_by_earnings_yield):
        scores[company.name] = idx + 1

    for idx, company in enumerate(ranked_by_roc):
        scores[company.name] += idx + 1

    # Sort based on combined scores
    return sorted(scores.items(), key=lambda x: x[1])

# Hardcoded company data where 1.00 represents 1 million dollars
companies = [
    Company("CompanyA", 2.00, 20.00, 15.00),
    Company("CompanyB", 2.50, 25.00, 18.00),
    Company("CompanyC", 1.80, 15.00, 12.00),
]

ranked_companies = magic_formula_ranking(companies)
for idx, (name, score) in enumerate(ranked_companies, 1):
    print(f"{idx}. {name} with score {score}")