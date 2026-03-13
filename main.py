from core.landing_cost import LandingCostEngine
from core.profit_engine import ProfitEngine
from interface.cli import get_input

data = get_input()

engine = LandingCostEngine(
    data["product_cost"],
    data["freight"],
    data["insurance"],
    data["duty_rate"],
    data["vat_rate"],
    data["port_charge"],
    data["logistics"],
    data["quantity"]
)

result = engine.calculate()

profit_engine = ProfitEngine(
    result["unit_cost"],
    data["selling_price"]
)

profit = profit_engine.calculate()

print("\n----- RTIS RESULTS -----")

print("Total Landing Cost:", result["total_cost"])
print("Unit Cost:", result["unit_cost"])

print("Profit per Unit:", profit["profit_per_unit"])
print("Profit Margin:", profit["profit_margin"], "%")
