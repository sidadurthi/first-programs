"""
- user input for operation to be performed
Ex: Addition, subtraction, multiplication, division, exponential
- user input two numbers
"""


print("Enter operation to be performed")
print("1: Addition")
print("2: subtraction")
print("3: multiplication")
print("4: division")
print("5: exponential")

operation = input("select one option: ")
print(operation)

number1 = input("Input number1 ")
number2 = input("input number2 ")

if operation == '1':
    print("performing addition")
    print(int(number1)+int(number2))
elif operation == '2':
    print("performing subtraction")
    print(int(number1)-int(number2))
elif operation == '3':
    print("performing multiplcation")
    print(int(number1)*int(number2))
elif operation == '4':
    print("performing divison")
    print(int(number1)/int(number2))
elif operation == "5":
    print("performing exponential")
    print(int(number1)**int(number2))
else:
    print("Invalid option")