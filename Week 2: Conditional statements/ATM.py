# This program simulates an ATM

# Define functions for withdrawing, depositing, and checking the balance
def withdraw(amount):
    """Withdraws money from the account"""
    global balance
    if amount > balance:
        print("Insufficient funds")
        return

    balance -= amount
    print("Withdrawal of $", amount, "successful")


def deposit(amount):
    """Deposits money into the account"""
    global balance
    balance += amount
    print("Deposit of $", amount, "successful")


def check_balance():
    """Checks the balance of the account"""
    print("Your balance is $", balance)


# Initialize the balance
balance = 1000

# Create a while loop that iterates indefinitely
while True:
    # Print a menu of options
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check balance")
    print("4. Exit")

    # Get the user's choice
    choice = input("Enter your choice: ")

    # Check the user's choice and call the appropriate function
    if choice == "1":
        # Withdraw money
        amount = int(input("Enter amount to withdraw: "))
        withdraw(amount)
    elif choice == "2":
        # Deposit money
        amount = int(input("Enter amount to deposit: "))
        deposit(amount)
    elif choice == "3":
        # Check the balance
        check_balance()
    elif choice == "4":
        # Exit the program
        exit()
    else:
        # Print an error message
        print("Invalid choice")