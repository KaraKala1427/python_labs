year = int(input("Input a year: "))
leap = bool
if year % 4 == 0 or year % 400 == 0:
    leap = True
else:
    leap = False

month = int(input("Input a month(1-12): "))
if month in (1, 3, 5, 7, 8, 10, 12):
    m_length = 31
elif month == 2:
    if leap:
        m_length = 29
    else:
        m_length = 28
else:
    m_length = 30

day = int(input("Input a day: "))
if day < m_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next day is: ", year, "-", month, "-", day)