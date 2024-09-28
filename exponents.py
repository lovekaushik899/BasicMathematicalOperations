def calculate_power(x, y):
  """Calculates x raised to the power of y.

  Args:
    x: The base number.
    y: The exponent.

  Returns:
    The result of x raised to the power of y.
  """

  result = x ** y
  return result

# Get user input for x and y
x = float(input("Enter the base number: "))
y = float(input("Enter the exponent: "))

# Calculate the power using the function
power = calculate_power(x, y)

# Print the result
print(x, "raised to the power of", y, "is", power)
