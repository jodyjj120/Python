# first project = Calculator

first = input("enter first number :")
operator = input("enter operator (+,-,*,/,%) :")
second = input("what is the second number :")

first = int(first)
second = int(second)

if operator == "+" :
    print(first + second)

elif operator == "-" :
    print(first - second)

elif operator == "*" :
    print(first * second)

elif operator == "/" :
    print(first / second)

elif operator == "%" :
    print(first % second)

else :
    print("invalid query")