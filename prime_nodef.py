# Input: Get the number from the user
number = int(input("Enter a number: "))

# Assume the number is prime
is_prime = True

# A prime number is greater than 1
if number > 1:
    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
else:
    is_prime = False  # Numbers less than or equal to 1 are not prime

# Output: Display if the number is prime or not
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
