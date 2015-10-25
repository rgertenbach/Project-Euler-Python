"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

yearid = 1900
monthid = 1
dayofmonth = 7
sunonfirst = 0

def daysinmonth(year, month):
    if month in [4, 6, 9, 11]: return 30
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): return 29
        else: return 28
    return 31

while yearid <= 2000 and monthid <= 12 and dayofmonth <= 31:
    dim = daysinmonth(yearid, monthid)
    if dayofmonth == 1 and yearid > 1900: sunonfirst += 1
    dayofmonth += 7
    if dayofmonth > dim:
        dayofmonth -= dim
        monthid += 1
        if monthid == 13:
            monthid = 1
            yearid += 1
print(sunonfirst)