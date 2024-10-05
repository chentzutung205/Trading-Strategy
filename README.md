# Trading Strategy

Two trading strategies were implemented in this repository: Weighted Moving Average (WMA) and Cheapest Production Calculator.

## Weighted Moving Average Calculator
### Overview

The `wma.py` script calculates the WMA of trades for different assets. Each trade consists of a key (symbol), value (price), quantity, and a sequence number. The WMA is computed based on the value and quantity of trades, considering the latest sequence number for each asset. The program ignores trades with outdated sequence numbers to ensure only the most recent data is included in the WMA calculation.

### Key Features
- Handle multiple trades for different assets (e.g., "AAPL", "GOOGL")
- Ignore outdated trades based on the sequence number
- Calculate WMA for each asset after every valid trade
- Output the WMA in real-time as new trades are processed

### Example

Consider the following list of trades:
```
trades = [
    Trade("AAPL", 150.0, 100, 1),
    Trade("GOOGL", 2800.0, 50, 1),
    Trade("AAPL", 151.0, 200, 2),
    Trade("AAPL", 149.0, 150, 3),
    Trade("GOOGL", 2750.0, 75, 2),
    Trade("AAPL", 148.0, 50, 1),  # This trade will be ignored due to lower sequence number
]
```

### Output

The output would be:
```
AAPL: 150.00
GOOGL: 2800.00
AAPL: 150.67
AAPL: 150.11
GOOGL: 2770.00
```

## Cheapest Production Calculator
### Overview

The `cheapest_production.py` script provides a solution for determining the cheapest production cost for a given target product based on a set of recipes. The recipes define how each product can either be directly purchased or constructed from other products. If a product can be constructed, the script explores whether it's cheaper to buy the components or build them from other subcomponents recursively. The result is the minimum cost to produce the target product.

### Input Format

The input is a multi-line string where:
- The first line contains the name of the target product.
- Each subsequent line defines a product and provides its:
  - Name
  - Purchase price (can be "null" if the product cannot be purchased)
  - Number of ingredients needed (0 if the product is not made from other ingredients)
  - List of ingredients (if applicable) separated by ;

### Example

Consider the following input:
```
teddy_bear
eyeball, 10.5, 2, glass; paint
glass, 5, 0,
paint, 4, 0,
teddy_bear, null, 4, eyeball; shirt; fabric; thread
fabric, 15, 2, bear; yarn
bear, 100, 0,
yarn, 2, 0,
thread, 13, 0,
shirt, 24, 0,
```

### Output

The output would be:
```
61.00
```

## Limitations
- If a product is not available for purchase or cannot be constructed due to missing ingredients, the function will return an infinite cost (inf).
- The input format must strictly follow the defined structure, with commas separating product properties and semicolons for ingredients.
