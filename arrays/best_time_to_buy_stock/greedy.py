def max_profit(prices: list[int]) -> int:
    pass
    # flips the approach from: "for each buy day, what's the best sell day after?"
    # greedy uses: "if I sell today, what's the best day I could have bought?"

    lowest = float('inf')
    best = 0
    for price in prices:
        lowest = min(lowest, price)
        best = max(best, price - lowest)

    return best