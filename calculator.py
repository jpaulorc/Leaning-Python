print("\n******************* Python Calculator *******************\n")

print("Select the operation:\n")
print("1 - Sum")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division\n")

operation = int(input("Input your option: (1/2/3/4): "))

first  = float(input("Input your firts number: "))
second = float(input("Input your second number: "))

sum_func = lambda a, b: a + b
sub_func = lambda a, b: a - b
mul_func = lambda a, b: a * b
div_func = lambda a, b: a / b

if operation == 1:
    print(sum_func(first, second))
elif operation == 2:
    print(sub_func(first, second))
elif operation == 3:
    print(mul_func(first, second))
elif operation == 4:
    print(div_func(first, second))
else:
    print("Invalid Operation!")

