class BankAccount:
    def __init__(self, name, account_number, balance=50000):
        # Constructor to initialize the BankAccount object
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, d_amount):
        # Method to handle deposits
        self.d_amount = d_amount
        self.balance += self.d_amount
        print(f"Deposit amount is credited to the account {self.account_number}")
        print(f"Your current balance is {self.balance}")

    def withdrawal(self, w_amount):
        # Method to handle withdrawals
        self.w_amount = w_amount
        self.balance -= self.w_amount
        print(f"Amount is withdrawn from your account {self.w_amount}")
        print(f"Your current balance is {self.balance}")

    def display_acc_details(self):
        # Method to display account details
        print(f"Account Holder name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account balance: {self.balance}")


def main():
    # Main function to interact with the BankAccount class
    name = input("Enter your name: ")
    account_number = input("Enter your 16-digit account number: ")

    # Validation for the length of the account number
    if len(account_number) != 16:
        print("ERROR: Invalid account number. Please enter a 16-digit account number.")
        return

    try:
        account_number = int(account_number)
    except ValueError:
        print("Error: Account number must be a valid integer.")
        return

    # Creating a BankAccount object
    bank_account = BankAccount(name, account_number)

    # Making a deposit
    bank_account.deposit(5000)


if __name__ == "__main__":
    main()
