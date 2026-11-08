# Cassidoo question of the week:
# November 2nd, 2026
#
# Question:
# Given a chronological log of local "HH:MM" timestamps from
# the night daylight saving time ends, return the actual number
# of minutes between the first and last entries.
# The log contains a consecutive pair that reveals the clock's
# one-hour rollback.


def elapsedMinutes(timestamps):
    if len(timestamps) < 2:
        return 0

    def toMinutes(timestamp):
        hours, minutes = map(int, timestamp.split(":"))
        return hours * 60 + minutes

    total = 0
    previous = toMinutes(timestamps[0])

    for timestamp in timestamps[1:]:
        current = toMinutes(timestamp)
        difference = current - previous

        if difference < 0:
            difference += 60

        total += difference
        previous = current

    return total


print(elapsedMinutes([
    "00:50", "01:10", "01:50", "01:10", "02:10"
]))
# 140

print(elapsedMinutes([
    "01:55", "01:05", "01:25", "01:40"
]))
# 45
