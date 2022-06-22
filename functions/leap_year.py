# defines is_year_leap(year) function
# the function takes one argument: year
# the function calculates whether any given year is leap or not
# the funtion returns True or False accordingly
def is_year_leap(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        return True
    else:
        return False

# tests
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
