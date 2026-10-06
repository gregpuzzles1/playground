# Cassidoo question of the week:
# October 4th, 2026
#
# Question:
# On Halloween night, a town is represented by a grid where 0 is an
# empty lot, 1 is a living person, and 2 is an infected zombie.
# Every minute, infection spreads to any living person directly
# above, below, left, or right of an infected zombie.
# Return the minimum number of minutes until no living people
# remain, or -1 if some people can never be reached.

from collections import deque


def minutesUntilApocalypse(grid):
    if not grid or not grid[0]:
        return 0

    # Copy the grid so the original is not changed.
    grid = [row[:] for row in grid]

    rows = len(grid)
    cols = len(grid[0])
    zombies = deque()
    livingPeople = 0

    # Find all starting zombies and count living people.
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                zombies.append((row, col))
            elif grid[row][col] == 1:
                livingPeople += 1

    minutes = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while zombies and livingPeople > 0:
        # Process one minute of infection at a time.
        for _ in range(len(zombies)):
            row, col = zombies.popleft()

            for rowChange, colChange in directions:
                nextRow = row + rowChange
                nextCol = col + colChange

                if (
                    0 <= nextRow < rows
                    and 0 <= nextCol < cols
                    and grid[nextRow][nextCol] == 1
                ):
                    grid[nextRow][nextCol] = 2
                    livingPeople -= 1
                    zombies.append((nextRow, nextCol))

        minutes += 1

    return minutes if livingPeople == 0 else -1


print(minutesUntilApocalypse([
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]))  # 4

print(minutesUntilApocalypse([
    [2, 1, 1],
    [0, 1, 1],
    [1, 0, 1]
]))  # -1
