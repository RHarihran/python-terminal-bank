def bank_system():
    accounts = {}
    
    print("=" * 40)
    print("      WELCOME TO PYTHON TERMINAL BANK")
    print("=" * 40)
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Create New Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            print("\n--- Create New Account ---")
            acc_num = input("Enter a new account number: ")
            if acc_num in accounts:
                print("Error: Account number already exists!")
            else:
                name = input("Enter account holder name: ")
                try:
                    initial_deposit = float(input("Enter initial deposit amount: "))
                    if initial_deposit < 0:
                        print("Error: Deposit amount cannot be negative.")
                        continue
                    accounts[acc_num] = {"name": name, "balance": initial_deposit}
                    print(f"Success! Account created for {name} with balance: ${initial_deposit:.2f}")
                except ValueError:
                    print("Error: Please enter a valid numerical amount.")
                    
        elif choice == '2':
            print("\n--- Check Balance ---")
            acc_num = input("Enter your account number: ")
            if acc_num in accounts:
                print(f"Account Holder: {accounts[acc_num]['name']}")
                print(f"Current Balance: ${accounts[acc_num]['balance']:.2f}")
            else:
                print("Error: Account not found!")
                
        elif choice == '3':
            print("\n--- Deposit Money ---")
            acc_num = input("Enter your account number: ")
            if acc_num in accounts:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    if amount <= 0:
                        print("Error: Deposit amount must be greater than zero.")
                        continue
                    accounts[acc_num]['balance'] += amount
                    print(f"Success! Deposited ${amount:.2f}.")
                    print(f"New Balance: ${accounts[acc_num]['balance']:.2f}")
                except ValueError:
                    print("Error: Please enter a valid numerical amount.")
            else:
                print("Error: Account not found!")
                
        elif choice == '4':
            print("\n--- Withdraw Money ---")
            acc_num = input("Enter your account number: ")
            if acc_num in accounts:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    if amount <= 0:
                        print("Error: Withdrawal amount must be greater than zero.")
                        continue
                    if amount > accounts[acc_num]['balance']:
                        print("Error: Insufficient funds!")
                    else:
                        accounts[acc_num]['balance'] -= amount
                        print(f"Success! Withdrew ${amount:.2f}.")
                        print(f"Remaining Balance: ${accounts[acc_num]['balance']:.2f}")
                except ValueError:
                    print("Error: Please enter a valid numerical amount.")
            else:
                print("Error: Account not found!")
                
        elif choice == '5':
            print("\nThank you for banking with us. Have a great day!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    bank_system()