# Cassidoo question of the week:
# August 24th, 2026
#
# Question:
# Given an array of integers, return a new array where odd numbers come first,
# even numbers come next, and zeros appear at the end. The relative order of
# elements within each group must be preserved.


def partitionArray(nums):
    odds = []
    evens = []
    zeros = []

    for num in nums:
        if num == 0:
            zeros.append(num)
        elif num % 2 != 0:
            odds.append(num)
        else:
            evens.append(num)

    return odds + evens + zeros


print(partitionArray([0, 3, 2, 1, 4, 0, 7]))
print(partitionArray([0, 32, 8, 99, 19, 20, 4, 0, 12, 7, 14]))
