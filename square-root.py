import math

# Function to calculate square root
def calculate_square_root(number):
    if number < 0:
        return "Square root of negative numbers is not real."
    else:
        return math.sqrt(number)

# Input from the user
num = float(input("Enter a number: "))

# Call the function and print the result
result = calculate_square_root(num)
print(f"The square root of {num} is: {result}")

