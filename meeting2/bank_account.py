# Person (encapsulating data)
class Person:

    def __init__(self, id, first_name, last_name, age, phone_number=None):
        # print(f"Called __init__ with id {id}")
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.age = age

    def is_child(self):
        print(f"Called is_child for id {self.id}")
        return self.age <= 16


    def __str__(self):
        return f"{self.id} : {self.first_name} {self.last_name}"


class BankAccount:

    max_limit = 100000

    def __init__(self, account_num: int, holder: Person, branch_num: int, bank_num: int):
        self.account_num = account_num
        self.owner: Person = holder
        self.branch_num = branch_num
        self.bank_num = bank_num
        self.__balance = 0
        self.limit = 1000

    def get_balance(self):
        return self.__balance

    def deposit(self, amnt):
        self.__balance += amnt
        # self.balance = self.balance + amnt

    def withdraw(self, amnt):
        if self.__balance - amnt >= -self.limit:
            self.__balance -= amnt
            return True
        else:
            print("You cannot withdraw")

    def transfer(self, amnt, destination):
        if self.withdraw(amnt):
            destination.deposit(amnt)

    def __str__(self):
        return f"Account {self.account_num}\nBalance: {self.__balance}"

    def foo(self):
        pass


class IBAN():
    # def __init__(self, name, num):
    #     self.holder_name = name
    #     self.iban_num = num

    def swift_transfer(self, amnt, recepient_iban):
        print(f"Called transfer: IBAN ")

    def set_num(self, num):
        self.iban_num = num

    def foo(self):
        pass


class DiscountBankAccount(BankAccount, IBAN):
    def __init__(self, account_num: int, holder: Person,
                 branch_num: int, bank_num: int):
        super().__init__(account_num, holder, branch_num, bank_num)
        # super(DiscountBankAccount, self).__init__()
        # super(IBAN, self).__init__(name, num)



valeria = Person("123456789", "Valeria", "aynbinder", 35)
# dan = Person("987654321", "Dan", "Dan", 25)

dis = DiscountBankAccount(123123, valeria, 22, 4)
dis.set_num(4856048576045760982475687)
print(dis.__dict__)
dis.swift_transfer(30, None)

# account_valeria = BankAccount(123, valeria, 33, 11)
# account_dan = BankAccount(234, dan, 22, 10)

# print(account_valeria.__dict__)

# print(f"Balance: {account_valeria._BankAccount__balance}")
# account_valeria.balance = "dgdfgdf"
# account_valeria.withdraw(2000)
# account_valeria.balance = 5000
# account_valeria.__balance = "blabla"

# account_valeria.deposit(100)
# account_valeria.withdraw(2000)
# print(f"Balance: {account_valeria.__balance}")