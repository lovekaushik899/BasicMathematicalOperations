# Define the function to check if a number is prime
def is_prime(number):
    """
    Function to check if a number is prime.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    # Prime numbers are greater than 1
    if number <= 1:
        return False
    
    # Check if the number has any divisors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True

# Function to take input from the user and check if the number is prime
def check_prime():
    """
    Function to take user input and check if the number is prime.
    """
    try:
        # Take user input and convert it to an integer
        num = int(input("Enter a number to check if it is prime: "))
        
        # Check if the number is prime and print the result
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Call the function to check for prime numbers
check_prime()

