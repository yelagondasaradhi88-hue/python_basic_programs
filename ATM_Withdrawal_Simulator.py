pin=12345
current_balance=1500
entered_pin=int(input("Enter your PIN NO:"))
withdrawal_amount=int(input("Enter your withdrawal amount:")) 
if entered_pin!=pin :
       print("your pin is incorrect")
elif withdrawal_amount <= 0:
    print("Please enter a valid amount")
elif current_balance<withdrawal_amount:
   print("your withdrawal amount is more than current balance")
else:
    balance=current_balance-withdrawal_amount
    print(f"Please collect your cash. Remaining balance: ₹{balance}")