"""
Back-end programming and routines that
will calculate some basic values of museum visitors.
In Python, calculate the average number
 of visitors per day. Using Python, use a function.

 Using Python, I want to calculate the average number
 of visitors per day who go to this museum.



"""


# the dictionary to store the number of visitors for each day
weekday_names = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def get_num_visitors_for_day(day):
    while True:
        try:
            numVisitortsForDay = input("Enter the number of visitors for {}s of the month: ".format(day.title()))
            if numVisitortsForDay.lower() == "q":
                print("Goodbye")
                exit()
            else:
                numVisitortsForDay = int(numVisitortsForDay)
            if numVisitortsForDay < 0:
                print("Please enter a positive number")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    return numVisitortsForDay

# show total visitors throughout all week days
def get_total_visitors():
    return sum(visitors_by_day.values())

# show visitors for weekdays
def get_visitors_weekdays():
	return get_total_visitors() - get_visitors_weekends()

# show visitors for weekends
def get_visitors_weekends():
	return visitors_by_day["saturday"] + visitors_by_day["sunday"]

# method to calculate the average
def calc_averages(no_of_days):
	return get_total_visitors() / no_of_days




""" time for reports """
def printReports():
	print("-"*50)
	print("\nThis is the monthly report:")

	print("\nTotal visitor for the month: {}".format(get_total_visitors()))

	print("Average number of visitors for the month: {0:.2f}".format(calc_averages(30)))
	# change line
	# show the visitors by weekday and weekends
	print("\nNumber of visitors on weekdays: {}".format(get_visitors_weekdays()))
	print("Number of visitors on weekends: {}".format(get_visitors_weekends()))

	# get the average number of visitors per weekday
	#avgNumVisitorWeekday = visitorsWeekdays/5

	# get the average number of visitors per week end day
	#avgNumVisitorWeekend = visitorsWeekends/2

	# print
	print("\nAverage number of visitors on a weekday: {0:.2f}".format(get_visitors_weekdays()/5))
	print("Average number of visitors on a weekend day: {0:.2f}\n".format(get_visitors_weekends()/2))

while True:
    choice = input("Enter q to quit anytime or any other key to continue: ")
    if choice.lower() == "q":
        print("Goodbye")
        break
    visitors_by_day = {day: get_num_visitors_for_day(day) for day in weekday_names}
    # finally call print reports
    printReports()
