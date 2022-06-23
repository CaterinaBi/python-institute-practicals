# create an empty dictionary for the input data
# the student's name is used as a key
# the associated scores will be stored in a tuple
school_class = {}

# creates loop
# sets name as input
# breaks loop if input is null
# sets score as input
# breaks loop if score is not in desired range
# if the student's name is unknown to the dictionary, create a new entry
while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

# iterate through the sorted students' names
# initialize the data needed to evaluate the average (sum and counter)
# iterate through the tuple, taking all the subsequent scores and updating the sum, together with the counter
# evaluate and print the student's name and average score.
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
