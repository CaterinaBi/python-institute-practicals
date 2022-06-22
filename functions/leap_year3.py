# defines is_year_leap(year) function
# the function takes one argument: year
# the function calculates whether any given year is leap or not
# the funtion returns True or False accordingly
def is_year_leap(year):
	if year%4 == 0 and year%100 != 0 or year%400 == 0:
        	return True
    	else:
        	return False

# defines days_in_month(year, month) function
# the function takes two arguments: year, month
# the function calculates the number of days in a given month and in a given year
# the function returns month_length
def days_in_month(year, month):
months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    is_year_leap(year)
    if is_year_leap(year) == True:
        months[2] = 29
    month_length = months[month]
    return 

def day_of_year(year, month, day):
#
# Write your new code here.
#

print(day_of_year(2000, 12, 31))
