class Basket:
    def _init_(self, type, price):
        self.__type = type
        self.__price = price

    def set_type(self, type):
        self.__type = type
    def set_price(slf, price):
        self.__price = price

    def get_type(self):
        return self.__type
    def get_price(self):
        return self.__price

    def showDetails(self):
        print(f"{self._type} basket is Rs.{self._price:.2f}")

class Cane(Basket):
    pass
class Bamboo(Basket):
    pass

if _name_ == '_main_':
    caneObject = Cane('Cane', 250)
    bambooObject = Bamboo('Bamboo', 300)

    caneObject.showDetails()
    bambooObject.showDetails()