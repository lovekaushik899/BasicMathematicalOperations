def calculate_sum(num1, num2):
  """Calculates the sum of two numbers.

  Args:
    num1: The first number.
    num2: The second number.

  Returns:
    The sum of num1 and num2.
  """

  return num1 + num2

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum
sum = calculate_sum(num1, num2)

# Print the result
print("The sum of", num1, "and", num2, "is:", sum)



