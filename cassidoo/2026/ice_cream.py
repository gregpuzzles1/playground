# Cassidoo question of the week:
# July 27th, 2026
#
# Question:
# Given an array of ice cream orders and a freezer stock map,
# return how many orders can be fulfilled before the first
# unavailable flavor.


def fulfilled_orders_before_failure(orders, stock):
    fulfilled = 0

    for order in orders:
        # Count how many of each flavor this order needs.
        needed = {}

        for flavor in order:
            needed[flavor] = needed.get(flavor, 0) + 1

        # Stop if any flavor is unavailable or insufficient.
        if any(
            stock.get(flavor, 0) < amount
            for flavor, amount in needed.items()
        ):
            break

        # Remove the fulfilled order from stock.
        for flavor, amount in needed.items():
            stock[flavor] -= amount

        fulfilled += 1

    return fulfilled


# Test 1
print(fulfilled_orders_before_failure(
    [["chocolate"], ["chocolate"], ["chocolate"]],
    {"chocolate": 2}
))
# Expected output: 2


# Test 2
print(fulfilled_orders_before_failure(
    [
        ["vanilla", "vanilla"],
        ["chocolate", "mint"],
        ["strawberry"],
        ["strawberry", "mint"]
    ],
    {
        "vanilla": 2,
        "chocolate": 1,
        "mint": 1,
        "strawberry": 5
    }
))
# Expected output: 3


# Test 3
print(fulfilled_orders_before_failure(
    [["rocky road"], ["vanilla"]],
    {"vanilla": 3}
))
# Expected output: 0
