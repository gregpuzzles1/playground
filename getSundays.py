# Cassidoo question of the week:
# September 21st, 2026
#
# Question:
# Given a year and month, return an array containing every date in that
# month that falls on a Sunday. Return each date in YYYY-MM-DD format.

import calendar

def getSundays(year, month):
    calendar.setfirstweekday(calendar.SUNDAY)
    weeks = calendar.monthcalendar(year, month)
    return [
        f"{year:04d}-{month:02d}-{week[0]:02d}"
        for week in weeks if week[0] != 0
    ]

print(getSundays(2026, 9))
print(getSundays(2024, 2))
print(getSundays(2026, 7))

# Expected output:
# ['2026-09-06', '2026-09-13', '2026-09-20', '2026-09-27']
# ['2024-02-04', '2024-02-11', '2024-02-18', '2024-02-25']
# ['2026-07-05', '2026-07-12', '2026-07-19', '2026-07-26']
