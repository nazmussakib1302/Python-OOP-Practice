class AtmModel:

    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        while True:
            user_input = input("""
Hello, how would you like to proceed?
    1. Enter 1 to create PIN
    2. Enter 2 to deposit balance
    3. Enter 3 to withdraw balance
    4. Enter 4 to check the balance
    5. Enter 5 to exit
""")

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Bye")
                break
            else:
                print("Invalid option, please try again")

    def create_pin(self):
        self.pin = input("Enter your new PIN: ")
        print("PIN created successfully")

    def check_pin(self):
        if self.pin == "":
            print("Please create a PIN first")
            return False
        if input("Enter your PIN: ") != self.pin:
            print("Incorrect PIN")
            return False
        return True

    def read_amount(self, prompt):
        try:
            amount = float(input(prompt))
        except ValueError:
            print("Please enter a valid number")
            return None
        if amount <= 0:
            print("Amount must be greater than 0")
            return None
        return amount

    def deposit(self):
        if not self.check_pin():
            return
        amount = self.read_amount("Enter amount to deposit: ")
        if amount is None:
            return
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self):
        if not self.check_pin():
            return
        amount = self.read_amount("Enter amount to withdraw: ")
        if amount is None:
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")

    def check_balance(self):
        if not self.check_pin():
            return
        print(f"Your balance is: {self.balance}")
