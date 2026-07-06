# Cassidoo question of the week
# July 6th, 2026
#
# Question:
# Given an n x m grid, an odd integer size, and a coordinate (row, col)
# representing where a firework explodes, return all grid coordinates
# impacted by the blast.
#
# A firework affects every cell within Math.floor(size / 2) rows and columns
# of the center, clipped to the grid boundaries.
#
# Examples:
#
# get_impacted_coordinates(5, 5, 3, 1, 1)
#
# get_impacted_coordinates(3, 3, 1, 2, 1)
#
# get_impacted_coordinates(5, 5, 3, 4, 4)
#
# Strategy:
# Use size // 2 to find how far the blast reaches from the center.
# Then calculate the affected row and column ranges, using max() and min()
# to keep the coordinates inside the grid boundaries.


def get_impacted_coordinates(n, m, size, fw_row, fw_col):
    impact_range = size // 2
    impacted = []

    start_row = max(0, fw_row - impact_range)
    end_row = min(n - 1, fw_row + impact_range)

    start_col = max(0, fw_col - impact_range)
    end_col = min(m - 1, fw_col + impact_range)

    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            impacted.append([row, col])

    return impacted


print(get_impacted_coordinates(5, 5, 3, 1, 1))
print(get_impacted_coordinates(3, 3, 1, 2, 1))
print(get_impacted_coordinates(5, 5, 3, 4, 4))