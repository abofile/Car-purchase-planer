# Car Purchase Planner

A Python CLI tool that evaluates whether a car purchase is a sound financial decision based on established personal finance guidelines.

## Overview

The tool takes your financial profile as input and runs it against three financial rules to produce a verdict on the purchase. It handles both cash and lease scenarios.

## Features

- Cash and lease plan evaluation
- Down payment recommendation
- Monthly cost affordability check
- Income and net worth guideline check
- First-time buyer guidance
- Quick rules summary on launch

## Financial Rules Applied

**20/4/10 Rule**
The most practical guideline — 20% minimum down payment, loan term no longer than 4 years, and monthly transportation costs no more than 10% of gross monthly income.

**1/10th Income Rule**
Car price should not exceed 10% of gross annual income. Conservative but wealth-focused — keeps cash flow available for appreciating assets.

**Net Worth Guideline**
Car price should not exceed 10% of net worth. A car depreciates 15–20% in year one — tying up a large portion of net worth in a depreciating asset is a drag on wealth building.

**First-Time Buyer Exception**
For those just starting out with low accumulated net worth, up to 25% of annual income is considered acceptable for a first vehicle.

## Usage

```bash
python main.py
```

The tool runs interactively and prompts for input at each step.

**Example session:**
```
Enter car price: 30000
Enter monthly income: 12000
Enter annual_income: 222000
Enter your net worth: 0
Your payment plan Cash or Lease: cash

Car cost is too high — should not exceed 22200.0

This is a poor financial decision. The car exceeds both your
income and net worth guidelines. Consider a less expensive option.

Starting out? A car up to 25% of your annual income is considered
acceptable for a first vehicle. Make sure it doesn't exceed: 55500.0
```

## Requirements

- Python 3.x
- No external libraries

## References

- 20/4/10 Rule: https://www.thebalancemoney.com/how-much-car-can-you-afford-4156674
- 1/10th Rule: https://www.financialsamurai.com/the-110th-rule-for-car-buying-everyone-must-follow/
