# Gregorian Date to Ordinal Date

# This function take three integers as parameters and returns the day within the year for that date

def isLeap(year: int) -> bool:
    if (year % 400) == 0:
        isLeap = True
    elif (year % 100) == 0:
        isLeap = False
    elif (year % 4) == 0:
        isLeap = True
    else:
        isLeap = False
    
    return isLeap

def ordinalDate(day: int, month: int, year: int) -> str:
    from math import floor
    
    if month == 1 or month == 2:
        month += 12
        day   -= 365
    
    if isLeap(year):
        i = 2
    else:
        i = 3
    
    ordinalDay = (30 * (month - 1)) + floor(0.6 * (month + 1)) - i + day

    return "{}-{:03d}".format(year, ordinalDay)

def main():
    day, month, year = input("Enter the date (use the format DD-MM-YYYY): ").split('-')
    day, month, year = (int(day), int(month), int(year))
    print(ordinalDate(day, month, year))

if __name__ == "__main__":
    main()