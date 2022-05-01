class BankAccount():

    bank_name = None
    bank_num = None

    def __init__(self):
        self.holder = "ולריה איינבינדר"
        self.account_num = 12345
        self.balance = 0
        self.limit = 1000

    def deposit(self, amnt):
        pass

    def transfer(self, amnt, recepient_account):
        print(f"Called transfer: BankAccount ")


class IBAN():
    def __init__(self):
        self.holder = "Valeria Aynbinder"
        self.iban_num = 11223344556677889900123

    def swift_transfer(self, amnt, recepient_account):
        print(f"Called transfer: IBAN ")



class DiscountAccount(BankAccount, IBAN):

    bank_name = "Discount"
    bank_num = 11



class LeumiAccount(BankAccount):

    bank_name = "Leumi"
    bank_num = 10


da = DiscountAccount()
print(da.holder)
print(DiscountAccount.mro())

