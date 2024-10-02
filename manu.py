from typing import Dict, List, Tuple, Optional

def parse_input(input_str: str) -> Tuple[str, Dict[str, Tuple[Optional[float], List[str]]]]:
    lines = input_str.strip().split('\n')
    target_product = lines[0].strip()
    recipes = {}

    for line in lines[1:]:
        parts = [part.strip() for part in line.split(',')]
        product = parts[0]
        price = float(parts[1]) if parts[1] != "null" else None
        input_count = int(parts[2])

        if input_count == 0:
            ingredients = []
        else:
            ingredients = [ing.strip() for ing in parts[3].split(';')]

        recipes[product] = (price, ingredients)

    return target_product, recipes

def cheapest_production(target: str, recipes: Dict[str, Tuple[Optional[float], List[str]]]) -> float:
    memo = {}

    def dfs(product: str) -> float:
        if product in memo:
            return memo[product]

        price, ingredients = recipes[product]

        if not ingredients:  # Can only be purchased
            return float('inf') if price is None else price

        if price is None:  # Can only be built
            total_cost = sum(dfs(ingredient) for ingredient in ingredients)
            memo[product] = total_cost
            return total_cost

        # Can be either purchased or built
        build_cost = sum(dfs(ingredient) for ingredient in ingredients)
        memo[product] = min(price, build_cost)
        return memo[product]

    return dfs(target)


# Example usage
input_str = """teddy_bear
eyeball, 10.5, 2, glass; paint
glass, 5, 0,
paint, 4, 0,
teddy_bear, null, 4, eyeball; shirt; fabric; thread
fabric, 15, 2, bear; yarn
bear, 100, 0,
yarn, 2, 0,
thread, 13, 0,
shirt, 24, 0,
"""

target_product, recipes = parse_input(input_str)
cost = cheapest_production(target_product, recipes)

print(f"{cost:.2f}")