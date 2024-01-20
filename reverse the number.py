rev = 0

n = input("enter your number :")

n = int(n)

temp = n

while n > 0 :
    dig = n % 10
    rev = ((rev * 10) + dig)
    n = n//10

#checking for the palindrome

if (temp == rev) :
    print("the number is a palindrome")

else :
    print("the number is not a palindrome")