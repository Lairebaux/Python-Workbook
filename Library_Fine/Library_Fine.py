"""
Your local library needs your help! Given the expected and
actual return dates for a library
book, create a program that calculates the fine (if any).
The fee structure is as follows:

1. If the book is returned on or before the expected return
date, no fine will be charged (i.e.:
fine = 0

2. If the book is returned after the expected return day but
 still within the same calendar
month and year as the expected return date
fine = 15 Hackos x (number days late)

3. If the book is returned after the expected return month but
 still within the same calendar
year as the expected return date, the
fine = 500 Hackos x (number months late)

4. If the book is returned after the calendar year in which it
 was expected, there is a fixed fine
of 1000 Hackos.

Charges are based only on the least precise measure of lateness.
For example, whether a
book is due January 1, 2017 or December 31, 2017, if it is
returned
January 1, 2018, that is a
year late and the fine would be 10,000 Hackos.

1<= d <= 31
1<= m <= 12
1<= y <= 3000

The first line contains == returned date d,m,y.
The second line == expected date d,m,y.

d1: returned date: 9 6 2015
d2: expected date: 6 6 2015
fee: 45
"""
def library_fine(d1, m1, y1, d2, m2, y2):
    if y1 < y2 or (m1 < m2 and y1 == y2) or \
         (d1 <= d2 and m1 == m2 and y1 == y2):
        return 0
    elif d1 > d2 and m1 == m2 and y1 == y2:
        return (d1 - d2) * 15
    elif m1 > m2 and y1 == y2:
        return (m1 - m2) * 500
    else:
        return 10000



