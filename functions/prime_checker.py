# defines the function is_prime;
# is_prime takes one argument (the value to check)
# is_prime returns True if the argument is a prime number, and False otherwise
def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
