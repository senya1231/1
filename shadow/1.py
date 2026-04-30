class Human:
   class Human:
    # Статические поля
    default_name = "Unknown"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        # Публичные свойства
        self.name = name
        self.age = age
        # Приватные свойства (инкапсуляция)
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
        # Вычисляем итоговую цену через метод объекта дома
        cost = house_obj.final_price(discount)
        
        # Проверка наличия средств
        if self.__money >= cost:
            self.__make_deal(house_obj, cost)
            print(f"Успех! {self.name} купил дом за {cost} руб. (со скидкой {discount}%)")
        else:
            print(f"Ошибка: Недостаточно денег для покупки! Нужно: {cost}, есть: {self.__money}")

class House:
    def __init__(self, area, price):
        # Protected свойства (доступны в подклассах)
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)

class SmallHouse(House):
    def __init__(self, price):
        # Переопределение init: площадь всегда 40м2
        super().__init__(area=40, price=price)

# --- Часть 4. Тесты ---

# 1. Вызов статического метода
Human.default_info()

# 2. Создание объекта Human
person = Human("Марат", 17)

# 3. Вывод информации о человеке
person.info()

# 4. Создание объекта SmallHouse
my_small_house = SmallHouse(price=50000)

# 5. Попытка покупки (сначала денег нет)
person.buy_house(my_small_house, discount=10)

# 6. Пополнение финансового положения
person.earn_money(60000)

# 7. Снова попытка купить дом
person.buy_house(my_small_house, discount=10)

# 8. Проверка состояния объекта после сделки
person.info()