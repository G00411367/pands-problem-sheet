# this program outputs whether or not today is a weekday

# import the datetme module
import datetime 

# store weekdays in a list
weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

date = datetime.datetime.now()

# extract current day
today = date.strftime("%A")

# check if current day is in the weekDay list
if today in weekDays:
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend, yay!")

