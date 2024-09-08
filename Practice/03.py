balance = 1000
correct_pin = "1234"

attempts = 3
while attempts > 0:
    pin = input("Enter your pin: ")
    if pin == correct_pin:
        print("Access Granted.")
        break
    else:
        attempts -= 1
        print(f"Incorrect Pin. You have {attempts} attempts left.")
if attempts==0:
    print("Too many incorrect attempts. Access Denied")
else:
    while True:
        print("\nATM Menu")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"Your Current Balance is ${balance}")

        elif choice == "2":
            amount = float(input("Enter deposite amount: $"))
            if amount>0:
                balance+=amount
                print(f"${amount} deposited. \nNew balance: ${balance}")
            else:
                print("Invalid Deposite")

        elif choice == "3":
            amount = float(input("Enter Withdrawl amount: $"))
            if 0 < amount<=balance:
                balance-=amount
                print(f"${amount} withdrawn. \nNew balance is: ${balance}")
            else:
                print("Invalid withdrawl amount or insufficient balance.")
        elif choice== "4":
            print("Thank you for using pyATM. \nHave a nice day!!!")
            break
        else:
            print("Invalid options. Please try again/later.") 


