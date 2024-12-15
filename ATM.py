print("welcome to swiss bank:ATM")
print("****************************")
userchoice = int(input('''1.balance check
2.withdraw cash
3.deposit cash
4.add account
*enter your choice
'''))
user = ["Mr.white","Mr.black"]
pins = [2439,6679]
balance = [1000,155]
username = input('''enter your name:
''')
if username == user[0]:
    pin = int(input('''enter your pin code:
'''))
    if pin == pins[0]:
        print("access granted")
        if userchoice == 1:
         print("your current balance is:", balance[0])
    else:
        print("invalid pin")

        # user:slim
if username == user[1]:
    pin = int(input("enter your pin"))
    if pin == pins[1]:
      print("access granted ")
    if userchoice == 1:
        print("your current balance is:", balance[1])
    else:
        print("access denied, invalid pin")
# withdraw
if userchoice == 2:
    if pin == pins[0]:
      a=int(input("enter amount"))
      if username == user[0]:
        print('''please wait,we're preparing your transaction..
you have successfully withdraw amount:rs.''',a)
        print('''collect your cash..
now, your remaining balance is:''', balance[0]-a, end="")

# deposit
if userchoice == 3:
 if pin == pins[0]:
    b = int(input("enter amount"))
    if username == user[0]:
        print('''please submit your cash..
you've successfully added cash..
now, your new available  balance is :''',balance[0]+b)
    else:
        print ("something went wrong, try again...")


# Add New Account
elif userchoice == 4:
    new_username = input("Enter a new username: ")
    if new_username in user:
        print("This username is already taken. Try a different one.")
    else:
        new_pin = int(input("Set a 4-digit PIN for your account: "))
        new_balance = int(input("Enter the initial deposit amount: "))

        # Append new details to respective lists
        user.append(new_username)
        pins.append(new_pin)
        balance.append(new_balance)

        print(f"Account created successfully! Welcome, {new_username}.")
        print(f"Your current balance is: {new_balance}")





