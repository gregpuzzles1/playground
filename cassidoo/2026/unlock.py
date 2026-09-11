# Cassidoo question of the week:
# September 6th, 2026
#
# Question:
# You have a backpack lock's starting position, and the code to unlock it,
# represented as two strings of integers. In one move, you may rotate any
# single digit one step up or down, with 0 and 9 considered adjacent.
# Return the minimum number of moves needed to transform the starting
# code into the unlock code.


def minMoves(start, unlock):
    moves = 0

    for current, target in zip(start, unlock):
        difference = abs(int(current) - int(target))
        moves += min(difference, 10 - difference)

    return moves


print(minMoves("8051", "1199"))  # 10
print(minMoves("000", "555"))    # 15
print(minMoves("109", "990"))    # 4
