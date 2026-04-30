import string

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_letters(self):
        """Метод для печати всех букв алфавита"""
        print(f"Буквы алфавита ({self.lang}): {' '.join(self.letters)}")

    def letters_num(self):
        """Метод для подсчета количества букв"""
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self, lang='En', letters_str=string.ascii_uppercase):
        super().__init__(lang, list(letters_str))

    def is_en_letter(self, letter):
        """Проверяет, входит ли буква в английский алфавит"""
        return letter in self.letters

    def letters_num(self):
        """Переопределенный метод, возвращающий приватное статическое свойство"""
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        """Статический метод с примером текста"""
        return "Hello, this is an English text example."

#

print("--- Тест класса Alphabet ---")
ru_alphabet = Alphabet("RU", ['А', 'Б', 'В', 'Г'])
ru_alphabet.print_letters()
print(f"Количество букв: {ru_alphabet.letters_num()}")

print("\n--- Тест класса EngAlphabet ---")
en_alphabet = EngAlphabet()
en_alphabet.print_letters()
print(f"Количество букв (через переопределенный метод): {en_alphabet.letters_num()}")

char_to_check = 'G'
print(f"Буква '{char_to_check}' в английском алфавите? {en_alphabet.is_en_letter(char_to_check)}")

char_to_check = 'Я'
print(f"Буква '{char_to_check}' в английском алфавите? {en_alphabet.is_en_letter(char_to_check)}")

print(f"Пример текста: {EngAlphabet.example()}")