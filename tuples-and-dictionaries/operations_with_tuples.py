# defines tuple
my_tuple = (1, 10, 100, 1000)

# prints first element
print(my_tuple[0])
# prints last element
print(my_tuple[-1])
# prints slice from second element to end
print(my_tuple[1:])
# prints slice from first element to penultimate
print(my_tuple[:-2])

# iterates throught the tuple and prints all its elements
for elem in my_tuple:
    print(elem)

# create new tuples by adding elements to my_tuple    
t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

# prints length of tuple
print(len(t2))
# print all elements in t1 and t2
print(t1)
print(t2)
# checks whether 10 belongs to the tuple
print(10 in my_tuple)
# checks whether -10 does not belong in the tuple
print(-10 not in my_tuple)
