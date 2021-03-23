from atm_card import ATMCard

class Costumer:

    def __init__(self, id, custPin = 1234, custBalance = 10000):
        self.id = id
        self.pin = custPin
        self.balance = custBalance

    def checkid(self):
        return self.id

    def checkPin(self):
        return self.pin

    def checkBalance(self):
        return self.balance

    def withdrawBalance(self, nominal):
        self.balance -= nominal

    def depositBalance(self, nominal):
        self.balance += nominal