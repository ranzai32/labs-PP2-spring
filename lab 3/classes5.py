class bankAccount:
    def __init__(self):
        self.owner = ""
        self.balance = 0

    def getBalance(self):
        self.owner = input("Введите ФИО: ")
        self.balance = int(input("Введите ваш баланс: "))

    def deposit(self):
        aqshaqosu = int(input("Сумма депозита: "))
        self.balance += aqshaqosu
        print("Успешно!")
        print("Ваш текущий баланс(тг): {}".format(self.balance))
    
    def withdraww(self):
        withdraw = int(input("Сумма вывода: "))
        if withdraw > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= withdraw
            print("Успешно!")
            print("Ваш текущий баланс: {}".format(self.balance))

bankOperation = bankAccount()
bankOperation.getBalance()
while True:
    typeoper = input("Введите тип операции (Withdraw/Deposit/Exit): ")
    if typeoper == "Withdraw":
        bankOperation.withdraww()
    elif typeoper == "Deposit":
        bankOperation.deposit()
    elif typeoper == "Exit":
        break
    else:
        print("Неправильный ввод операции.")




    
    


