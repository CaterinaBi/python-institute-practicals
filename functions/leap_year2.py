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
    return month_length

# tests
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
