def calculate_difference(num1, num2):
  """Calculates the difference between two numbers.

  Args:
    num1: The first number.
    num2: The second number.

  Returns:
    The difference between num1 and num2.
  """

  return num1 - num2

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the difference
difference = calculate_difference(num1, num2)

# Print the result
print("The difference between", num1, "and", num2, "is:", difference)
