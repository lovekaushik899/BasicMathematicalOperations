def calculate_square(number):
  """Calculates the square of a given number.

  Args:
    number: The number to be squared.

  Returns:
    The square of the given number.
  """

  return number * number

# Get user input for the number to be squared
num = float(input("Enter a number: "))

# Calculate the square using the function
square = calculate_square(num)

# Print the result
print("The square of", num, "is", square)
