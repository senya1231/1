class Human:
    default_name = "Unknown"
    default_age = 0
    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None
    def info(self):
        print(f"--- Информация о человеке ---")
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Дом: {self.__house}")
        print(f"Деньги: {self.__money} руб.")
        print(f"----------------------------")
    @staticmethod
    def default_info():
        print(f"Стандартные значения: Имя = {Human.default_name}, Возраст = {Human.default_age}")

    def __make_deal(self, house_obj, final_cost):
        """Приватный метод для проведения технической части сделки"""
        self.__money -= final_cost
        self.__house = house_obj

    def earn_money(self, amount):
        self.__money += amount
        print(f"Пополнение счета: +{amount} руб. Текущий баланс: {self.__money}")

    def buy_house(self, house_obj, discount=0):
        cost = house_obj.final_price(discount)
        
        if self.__money >= cost:
            self.__make_deal(house_obj, cost)
            print(f"Успех! {self.name} купил дом за {cost} руб. (со скидкой {discount}%)")
        else:
            print(f"Ошибка: Недостаточно денег для покупки! Нужно: {cost}, есть: {self.__money}")

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)

class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)

#1
Human.default_info()

# 2.
person = Human("Иван", 25)

# 3.
person.info()

# 4.
my_small_house = SmallHouse(price=50000)

# 5.
person.buy_house(my_small_house, discount=10)

# 6.
person.earn_money(60000)

# 7.
person.buy_house(my_small_house, discount=10)

# 8.
person.info()