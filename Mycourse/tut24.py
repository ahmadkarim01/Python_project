""" Try execpt exceptional handling in python. """
print("Enter the first number:")
num3 = int(input())
print("Enter the second number:")
num4 = int(input())
print("The sum of the two numbers are:")
print(num3+num4)

# Try accept
num1 = int(input("Enter any integer number: "))
num2 = int(input("Enter another integer number: "))
print("Ther sum of two numbers are: ",num1 + num2)

try:
    print("The sum of the two numbers are this one: ",int(num1)+int(num2))

except Exception as x:
    print(x)
