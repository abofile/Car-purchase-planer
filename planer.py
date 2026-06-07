print("""
╔══════════════════════════════════════════╗
║                                          ║
║        🚗  CAR AFFORDABILITY TOOL        ║
║                                          ║
║   Analyze whether a car purchase fits    ║
║   your financial profile before you      ║
║   commit to a decision.                  ║
║                                          ║
║   Rules applied:                         ║
║   • 20/4/10 Rule                         ║
║   • 1/10th Income Rule                   ║
║   • Net Worth Guideline                  ║
║                                          ║
╚══════════════════════════════════════════╝
""")

def show_rules():
    see_rules = input("Would you like a quick summary of the rules? (y/n): ")
    if see_rules.strip().upper() == "Y":
        print("""
┌─────────────────────────────────────────────────────────────┐
│                   FINANCIAL RULES SUMMARY                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📌 20/4/10 Rule                                             │
│     The most practical guideline. It keeps your monthly      │
│     burden manageable by capping transportation costs at     │
│     10% of gross income, requiring 20% down to reduce        │
│     loan size, and limiting the loan to 4 years to avoid     │
│     paying excessive interest on a depreciating asset.       │
│                                                              │
│  📌 1/10th Income Rule                                       │
│     Conservative but wealth-focused. A car loses value       │
│     the moment you drive it off the lot. Keeping the         │
│     purchase price at 10% of annual income ensures you       │
│     preserve cash flow for investments that actually grow.   │
│     Strict in most markets but a useful benchmark.           │
│                                                              │
│  📌 Net Worth Guideline                                      │
│     A car is a liability not an asset. Tying up more than    │
│     10% of your net worth in something that depreciates      │
│     15-20% in year one is a drag on wealth building.         │
│     The higher your net worth the more flexibility you have. │
│                                                              │
│  ⚠️  These rules are guidelines not laws. Breaking one       │
│     does not mean financial ruin. Breaking all three         │
│     usually does.                                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
""")

show_rules()
car_price = float(input("Enter car price: "))
monthly_income = float(input("Enter monthly income: "))
annual_income = float(input("Enter annual_income: "))
net_worth = float(input("Enter your net worth: "))


def grab_payment_type():
    while True:
        payment_type = input("Your payment plan Cash or Lease: ")
        if payment_type.strip().upper() in ("LEASE", "CASH"):
            return payment_type.strip().upper()
        elif payment_type.strip().upper() not in ("LEASE", "CASH"):
            print("Worng entry try again")

def lease_cost_grab(payment_type):
    if payment_type.strip().upper() == "LEASE":
        lease = float(input("Enter Lease cost: "))
        return lease
    else:
        pass

def analyzer(purchace):
    if purchace == "LEASE":
        down_payment = car_price * 0.20
        monthly_cost = monthly_income * 0.10
        return down_payment, monthly_cost, None
    elif purchace == "CASH":
        cash_plan = annual_income * 0.10
        return None, None, cash_plan
    else:
        raise ValueError("Unknown purchase type")

def planner(lease_cost, monthly_cost, cash_plan, payment_type):
    if payment_type == "LEASE":
        if monthly_cost <= lease_cost:
            print(f"\nThe lease cost more than adviced the monthly payment should be no more than {monthly_cost}")
        elif monthly_cost >= lease_cost:
            print(f"\nThe lease cost is ideal it's under or equal to {monthly_cost}")
    elif payment_type == "CASH":
        if car_price >= cash_plan:
            print(f"\nCar cost is to high it's more than 10% of your annual income should not exceed {cash_plan}")
        elif car_price <= cash_plan:
            print(f"\nCar cost is ideal it's under or equal to {cash_plan}")

def results():
    if car_price > annual_income * 0.1 and car_price > net_worth * 0.1:
        print("\nThis is a poor financial decision. The car exceeds both your income and net worth guidelines. Consider a less expensive option.")
        print(f"Starting out? A car up to 25% of your annual income is considered acceptable for a first vehicle. Make sure it dosen't exceed: {annual_income * 0.25}")
    elif car_price < annual_income * 0.1 and car_price < net_worth * 0.1:
        print("\nThis is a financially sound purchase. Car price is within both your income and net worth guidelines.")
    elif car_price > annual_income * 0.1 and car_price < net_worth * 0.1:
        print("\nProceed with caution. The car is within your net worth but exceeds the recommended 10% of annual income. Monthly costs may strain your budget.")

plan = grab_payment_type()
lease_amount = lease_cost_grab(plan)
down_payment, monthly_cost, cash_plan = analyzer(plan)
planner(lease_amount, monthly_cost, cash_plan, plan)
if plan == "LEASE":
    print(f"\nThe down payment have to be atleast: {car_price * 0.20}")
results()

print("\nFor more information visit:")
print("- 20/4/10 Rule: https://www.thebalancemoney.com/how-much-car-can-you-afford-4156674")
print("- 1/10th Rule: https://www.financialsamurai.com/the-110th-rule-for-car-buying-everyone-must-follow/")
