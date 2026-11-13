from datetime import datetime

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

cleanEventTitle = eventTitle.strip().title()

while True:
    try:
        eventDate = datetime(year, month, day)
        print("\nFormatted Output: ")
        print(f"Event: {cleanEventTitle.upper()}")
        print(f"Date: {eventDate.strftime("%B %d, %Y")}")
        print(f"Year: {eventDate.strftime("%Y")}")
        print(f"Month: {eventDate.strftime("%B")}")
        print(f"Day: {eventDate.strftime("%d")}")
        print(f"Weekday: {eventDate.strftime("%A")}")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break
