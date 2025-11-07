"""
Options:
- check the balance: prints current balance
- withdraw money:
    ask you how much to withdraw
    reduce the balance by that amount
    if you try to withdraw more than you have...
        print error don't update the balance
    don't withdraw a negative amount
- deposit money:
    ask you how to deposit
    increase the balance by that amount
    don't deposit a negative amount
- loop (with a while loop) until the user says "exit"
"""

# start with 1 million dollars
balance = 1000000
while True:
    value = input("ATM at your service")
    if value == "Check":
        print(balance)
    if value == "Withdraw":
        withdrawal = int(input("How much would you like to withdraw?"))
        if withdrawal < balance and withdrawal > 0:
            balance = balance - withdrawal
        if withdrawal < 0:
            print("Error")
        if withdrawal > balance: 
            print("Error")
       
    if value == "Deposit":
        deposit = input("How much would you like to deposit?")
        balance = balance + deposit


    


