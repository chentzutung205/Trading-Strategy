from typing import NamedTuple
from collections import defaultdict

class Trade(NamedTuple):
    key: str
    value: float
    quantity: int
    sequence: int

def calculate_wma(trades):
    trade_data = defaultdict(list)

    for trade in trades:
        if trade_data[trade.key] and trade.sequence < trade_data[trade.key][-1].sequence:
            continue

        trade_data[trade.key].append(trade)

        total_quantity = sum(t.quantity for t in trade_data[trade.key])
        weighted_sum = sum(t.value * t.quantity for t in trade_data[trade.key])

        wma = weighted_sum / total_quantity
        print(f"{trade.key}: {wma:.2f}")

# Example usage
trades = [
    Trade("AAPL", 150.0, 100, 1),
    Trade("GOOGL", 2800.0, 50, 1),
    Trade("AAPL", 151.0, 200, 2),
    Trade("AAPL", 149.0, 150, 3),
    Trade("GOOGL", 2750.0, 75, 2),
    Trade("AAPL", 148.0, 50, 1),
]

calculate_wma(trades)