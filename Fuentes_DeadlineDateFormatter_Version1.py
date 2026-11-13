eventTitle = input("Enter event title: ")

while True:
    try:
        year = int(input("Enter year: "))
        while year < 1:
            print("Invalid input.")
            print("Please enter a positive integer.")
            year = int(input("Enter year: "))
        break
    except ValueError:
        print("Invalid input.")
        print("Please enter a positive integer.")

leap = False
if year % 4 == 0:
    leap = True
if year & 100 == 0:
    leap = False
if year % 400 == 0:
    leap = True

months = ["January", "February", "March", "April", "May", "June", "July", "August", "November", "December"]
maxDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if leap:
    maxDays[1] = 29

while True:
    try:
        month = int(input("Enter month: "))
        while month < 1 or month > 12:
            print("Invalid input.")
            print("Please enter a positive integer from 1 to 12.")
            month = int(input("Enter month: "))
        break
    except ValueError:
        print("Invalid input.")
        print("Please enter a positive integer from 1 to 12.")

while True:
    maxDay = maxDays[month - 1]
    try:
        day = int(input("Enter day: "))
        while day < 1 or day > maxDay:
            print("Invalid input.")
            print(f"Please enter a positive integer from 1 to {max_day}.")
            day = int(input("Enter day: "))
        break
    except ValueError:
        print("Invalid input.")
        print(f"Please enter a positive integer from 1 to {max_day}.")

def get_weekday(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    
    k = year % 100
    j = year // 100
    
    h = (day + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7
    
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[h]

weekday = get_weekday(year, month, day)
cleanEventTitle = eventTitle.strip().title()
monthName = months[month]

while True:
    try:
        print("\nBasic Output: ")
        print(f"Event: {cleanEventTitle.upper()}")
        print(f"Year: {year}")
        print(f"Month: {monthName}")
        print(f"Day: {day}")
        print(f"Weekday: {weekday}")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break
