class BankAccount:
    def __init__(self, initial_balance=0.0):
        self._balance = float(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return self._balance
        raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds for this withdrawal.")
        if amount > 0:
            self._balance -= amount
            return self._balance
        raise ValueError("Withdrawal amount must be positive.")

    def get_balance(self):
        return self._balance

my_account = BankAccount(1000.0)  # Starting with $1000

print(f"Initial Balance: ${my_account.get_balance():,.2f}")

my_account.deposit(500.0)
print(f"Balance after deposit: ${my_account.get_balance():,.2f}")

my_account.withdraw(200.0)
print(f"Balance after withdrawal: ${my_account.get_balance():,.2f}")

# Trying to withdraw more than the available balance
try:
    my_account.withdraw(2000.0)
except ValueError as e:
    print(f"Withdrawal Error: {e}")