class Tomato:
    states = ("Отсутствует", "Цветение", "Зеленый", "Красный")

    def __init__(self, index):
        # Динамические protected свойства
        self._index = index
        self._state = Tomato.states[0]

    def grow(self):
        current_index = Tomato.states.index(self._state)
        if current_index < len(Tomato.states) - 1:
            self._state = Tomato.states[current_index + 1]

    def is_ripe(self):
        return self._state == Tomato.states[-1]

    def get_info(self):
        return f"Помидор №{self._index}: {self._state}"

class TomatoBush:
    def __init__(self, count):
        self.tomatoes = [Tomato(i + 1) for i in range(count)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []

    def get_all_info(self):
        return [t.get_info() for t in self.tomatoes]

class Gardener:
    def __init__(self, name, plant):
        self.name = name   
        self._plant = plant  

    def work(self):
        print(f"Садовник {self.name} ухаживает за кустом...")
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"Ура! {self.name} собрал полный урожай!")
            self._plant.give_away_all()
        else:
            print(f"Предупреждение: {self.name}, не все помидоры созрели!")

    @staticmethod
    def knowledge_base():
        # Статический метод со справкой
        print("--- Справка по садоводству ---")
        print("1. Регулярный полив ускоряет рост.")
        print("2. Помидоры готовы к сбору, когда они красные.")
        print("------------------------------")

if __name__ == "__main__":
    Gardener.knowledge_base()

    my_bush = TomatoBush(3)
    ivan = Gardener("Марат", my_bush)

    ivan.harvest()

    for stage  in range(3):
        print(f"\nЭтап роста {stage + 1}:")
        ivan.work()
        for info in my_bush.get_all_info():
            print(info)

    ivan.harvest()