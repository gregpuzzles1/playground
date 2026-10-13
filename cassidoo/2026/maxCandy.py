# Cassidoo question of the week:
# October 11th, 2026
#
# Question:
# You're trick-or-treating down a street, and you're given an
# array that shows how many pieces of candy each house gives out.
# You can't visit two houses that are next to each other.
# Return the maximum number of candy pieces you can collect.


def maxCandy(houses):
    twoBack = 0
    oneBack = 0

    for candy in houses:
        # Choose between skipping this house or visiting it.
        current = max(oneBack, twoBack + candy)
        twoBack = oneBack
        oneBack = current

    return oneBack


print(maxCandy([2, 7, 9, 3, 1]))  # 12
print(maxCandy([5, 1, 1, 5]))     # 10
print(maxCandy([4]))             # 4
print(maxCandy([]))              # 0
