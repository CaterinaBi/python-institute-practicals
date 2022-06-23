# creates a while loop
while True:
# creates try-except
    try:
        # code to test
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    # catches ValueError exception
    except ValueError:
        print("Wrong value.")
    # catches ZeroDivisionError exception
    except ZeroDivisionError:
        print("Sorry. I cannot divide by zero.")
    # catches other exceptions
    except:
        print("I don't know what to do...")
