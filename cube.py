def calculate_cube(number):
  """Calculates the cube of a given number.

  Args:
    number: The number to be cubed.

  Returns:
    The cube of the given number.
  """

  return number * number * number

# Get user input for the number to be cubed
num = float(input("Enter a number: "))

# Calculate the cube using the function
cube = calculate_cube(num)

# Print the result
print("The cube of", num, "is", cube)
