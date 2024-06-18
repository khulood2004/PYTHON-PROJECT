
import math

def calculate_square_root(number):
    if number < 0:
        return "Cannot calculate square root of a negative number"
    else:
        return math.sqrt(number)

number = float(input("Enter a number: "))
result = calculate_square_root(number)
print(f"The square root of {number} is: {result}")
