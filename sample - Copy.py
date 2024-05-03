def greet(name):
    """
    This function prints a greeting message.
    """
    print (f"My name is {name}")
# Call the function
#greet('reh')

n = input("Enter the name") 
greet(n)

import math_operations

result_add = math_operations.add(3, 4)
result_subtract = math_operations.subtract(7, 2)

print(result_add)
print(result_subtract)

from math_operations import multiply, divide

result_multiply = multiply(5, 6)
result_divide = divide(8, 2)

print(result_multiply)
print(result_divide)