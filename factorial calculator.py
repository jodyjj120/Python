num = input("enter your number :")

factorial = 1

num = int(num)

if num < 0 :
    print("sorry cannot find the factorial")

elif num == 0 :
    print("the factorial of 0 is 1 ")

else :
    for i in range(1, num + 1) :
        factorial = factorial * i
    print("the factorial of", num, "is",  factorial)