from bank import Bank, SavingsAccount

def raw_input(param):
    pass

class ATM(object):
    '''This class represents terminal-based
    ATM transactions.'''

    def __init__(self, bank):
        self._account = None
        self._bank = bank
        self._methods = {}  
        self._methods["1"] = self._getBalance
        self._methods["2"] = self._deposit
        self._methods["3"] = self._withdraw
        self._methods["4"] = self._quit

    def run(self):
        '''Logs in users and processes their accounts.'''
        failureCount = 0
        while True:
            userName = raw_input("Enter Name : ")
            pin = raw_input("Enter PIN : ")
            self._account = self._bank.get(pin)
            if (self._account == None):
                print("Error, unrecognized PIN")
                failureCount += 1
            elif (self._account.getName() != userName):
                print("Error, unrecognized name")
                failureCount += 1

            else:
                self._processAccount()

            if (failureCount >= 3):
                print("Shutting down and calling the cops!")
                return

    def _processAccount(self):

        '''A menu-driven command processor for a user.'''

        while True:
            print("1 View your balance")
            print("2 Make a deposit")
            print("3 Make a withdrawal")
            print("4 Quit\n")

            number = raw_input("Enter a number: ")
            theMethod = self._methods.get(number, None)

            if theMethod == None:
                print("Unrecognized number")
            else:
                theMethod()

            if self._account == None:
                break

    def _getBalance(self):
        print("Your balance is $", self._account.getBalance())

    def _deposit(self):
        amount = float(raw_input("Enter the amount to deposit: "))
        self._account.deposit(amount)

    def _withdraw(self):
        amount = float(raw_input("Enter the amount to withdraw: "))
        message = self._account.withdraw(amount)

        if message:
            print(message)

    def _quit(self):
        self._bank.save()
        self._account = None
        print("Have a nice day!")

def main():
    '''Instantiate an ATM and run it.'''
    bank = Bank("bank.dat")
    atm = ATM(bank)
    atm.run()

def createBank(number=0):
    """Saves a bank with the specified number of accounts.
    Used during testing."""

    bank = Bank()

    for i in range(number):
        bank.add(SavingsAccount('Name' + str(i + 1), str(1000 + i), 100.00))
        bank.save("bank.dat")

createBank(5)
main()
