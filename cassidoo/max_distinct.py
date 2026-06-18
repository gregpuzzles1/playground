# Cassidoo Interview Question of the Week
# June 15, 2026
#
# Question:
# Given a positive integer n, return the maximum number of
# distinct positive integers that can be added together to
# equal n.
#
# Examples:
# n = 5  -> 2  (2 + 3 = 5)
# n = 8  -> 3  (1 + 2 + 5 = 8)
# n = 15 -> 5  (1 + 2 + 3 + 4 + 5 = 15)
#
# Strategy:
# Start adding the smallest distinct positive integers:
# 1, 2, 3, 4, ...
# Continue as long as the running total does not exceed n.
# The number of integers added is the maximum possible count.

def max_distinct_count(n):
    total = 0      # Running sum
    count = 0      # Number of distinct integers used

    while total + (count + 1) <= n:
        count += 1
        total += count

    return count


# Test cases
print(max_distinct_count(5))   # 2
print(max_distinct_count(8))   # 3
print(max_distinct_count(15))  # 5
print(max_distinct_count(99))  # 13
