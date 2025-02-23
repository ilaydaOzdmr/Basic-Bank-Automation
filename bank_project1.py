# A simple bank automation for 'Turkcell Gelecegi Yazan Kadınlar'

class Account:
    def __init__(self, name, acct_no, balance=0):
        self.name=name
        self.acct_no=acct_no
        self.__balance=balance
    
    def deposit_money(self, amount):
        if amount > 0:
            self.__balance +=amount
            print(f"{amount} TL has been deposited into your account. Your current balance is {self.__balance} TL.")
        else:
            print("You entered an invalid amount!")

    def withdraw_money(self,amount):
        if 0 < amount <=self.__balance:
            self.__balance -=amount
            print(f"{amount} TL was withdrawn from the amounts. Your current balance is {self.__balance} TL.")
        else:
            print("Insufficient funds or invalid amount!")
    
    def show_balance(self):
        return self.__balance
    
class CheckingAccount(Account):
    pass

class DepositAccount(Account):

    def __init__(self, name, acct_no, balance=0, bank_rate=1.2):
        super().__init__(name, acct_no, balance)
        self.bank_rate=bank_rate

    def calc_rate(self):
        rate_amount= int(self.show_balance()) * self.bank_rate
        print(f"Your earnings with interest: {rate_amount} TL")
        return rate_amount

    def withdraw_money(self, amount):
        print("Withdrawing money from a term deposit account may take up to 2 weeks.")
        super().withdraw_money(amount)

def main():
    name=input("Please Enter Your Name: ")
    acct_no=input("Please Enter Your Account Number: ")
    checking_account= CheckingAccount(name, acct_no, 2000)
    deposit_account= DepositAccount(name, acct_no, 3000)

    while True:
        print("\nActions:")
        print("1) View deposit account balance")
        print("2) View checking account balance")
        print("3) Deposit money into deposit account")
        print("4) Withdraw money from deposit account")
        print("5) Deposit money into checking account")
        print("6) Withdraw money from checking account")
        print("7) Exit")

        try:
            choice= int(input("Please enter your choice "))
        except ValueError:
            print("Please Enter a valid value")
        
        if choice==1:
            print(f"Deposit Account Balance: {deposit_account.show_balance()} TL")
            deposit_account.calc_rate()
        elif choice==2:
            print(f"Checking Account Balance: {checking_account.show_balance()} TL")
        elif choice==3:
            amount= float(input("Please enter the amount to be deposited: "))
            deposit_account.deposit_money(amount)
            deposit_account.calc_rate()
        elif choice==4:
            amount= float(input("Please enter the amount to be withdrawn: "))
            deposit_account.withdraw_money(amount)
            deposit_account.calc_rate()
        elif choice==5:
            amount=float(input("Please enter the amount to be deposited: "))
            checking_account.deposit_money(amount)
        elif choice==6:
            amount=float(input("Please enter the amount to be withdrawn: "))
            checking_account.withdraw_money(amount)
        elif choice==7:
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()