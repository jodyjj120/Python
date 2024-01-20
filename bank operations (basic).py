balance = ("5000")

operator = input("enter choice(deposit, withdraw, check balance):" )

amount = input("enter the amount :")

balance = int(balance)

amount = int(amount)

if operator == "deposit":
    print(balance + amount)

elif operator == "withdraw":
    print(balance - amount)

elif operator == "check balance" :
    print(balance)
