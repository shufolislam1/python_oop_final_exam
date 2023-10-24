class Bank:
    accounts = []
    totalBankBalance = 0

    def bankrupt(self):
        if self.totalBankBalance < 0:
            print('Bank is Bankrupt')

class Users(Bank):
    account_number = 1000 

    def __init__(self, name, email, address, type) -> None:
        super().__init__()
        self.name = name
        self.email = email
        self.address = address
        self.type = type
        # users idividual balance, which is initially zero
        self.balance = 0
        # self.accountNo = accountNo
        self.accountNo = Users.account_number
        Users.account_number += 1

        self.loanTransaction = []
 

        Users.accounts.append(self)

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            
            Bank.totalBankBalance += amount
            self.loanTransaction.append({"type": "deposit", "amount": amount})
            print(f"\nDeposited ${amount}. New balance: ${self.balance}")
        else:
            print('\nInvalid amount')

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            Bank.totalBankBalance -= amount
            self.loanTransaction.append({"type": "withdraw", "amount": amount})
            print(f"\nWithdrew ${amount}. New balance: ${self.balance}")
        elif amount>self.balance:
            print("\nWithdrawal amount exceeded")
        else:
            print("\nInvalid withdrawal amount")


    def availableBalance(self):
        print(f'\nAvailable balance is {self.balance}')

    def transactionHistory(self):
        print('Transaction History: ')

        for history in self.loanTransaction:
            if history['type'] == 'loan':
                print(f'Loan: {history["amount"]}')
            elif history['type'] == 'deposit':
                print(f'Deposit: {history["amount"]}')
            if history['type'] == 'withdraw':
                print(f'withdraw: {history["amount"]}')

                
    def loanFromBank(self, amount):
        if len(self.loanTransaction) < 2:
            limit = 1000
            if amount > 0 and amount <= limit:
                self.balance += amount
                Bank.totalBankBalance += amount
                self.loanTransaction.append({"type": "loan", "amount": amount})
                print(f"Loan of ${amount} granted. New balance: ${self.balance}")
            else:
                print(f"Invalid loan amount. Maximum loan limit is ${limit}.")
        else:
            print("Can not take more than 2 times.")

    def transferMoney(self, accountNo, amount):
        if amount<self.balance:
            reciver = None
        for user in Users.accounts:
            if user.accountNo == accountNo:
                reciver = user
                break
            if reciver is not None:
                self.balance -= amount
                reciver.balance += amount
                print(f"Transferred ${amount} to account {accountNo}.")
            else:
                print("Account does not exist.")


class Admin(Bank):
    def createAccount(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

        Users.accounts.append(self)
          

    def deleteUserAccount(self, accountNo):
        for user in Bank.accounts:
            if user.accountNo == accountNo:
                Bank.accounts.remove(accountNo)
                print(f'Successfully delete')

            else:
                print("Account does not exist")


    def showAllUsersAccountList(self):
        for user in Bank.accounts:
            print(f'Name: {user.name}')
            print(f'Email: {user.email}')
            print(f'Address: {user.address}')
            # print(f'Account No: {user.accountNo}')

    def checkTotalAvailableBalanceInBank(self):
        print(f'Total available balance in Bank: {Bank.totalBankBalance}')

    def totalLoanAmountFromBank(self):
        loanAmount = 0
        for user in Users.accounts:
            for transaction in user.loanTransaction:
                if transaction['type'] == 'loan':
                    loanAmount += transaction['amount']
        return loanAmount

    def toggleLoanFeature(self, enable):
        pass


# dbbl = Bank('dbbl')
shufol = Users('shufol', 'shhufol@islam.com', 'tangail', 'normal')
shufol.deposit(5000)
shufol.withdraw(5001)
shufol.availableBalance()
shufol.loanFromBank(1000)

admin = Admin()
admin.createAccount('admin', 'admin@admin.com', 'dhaka')
admin.showAllUsersAccountList()
# admin.checkTotalAvailableBalanceInBank()
admin.totalLoanAmountFromBank()
# currentUser = admin


# while True:
