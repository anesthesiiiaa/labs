from abc import ABC, abstractmethod  # Імпортуємо модуль abc для абстрактних класів і методів

# 1. Наслідування та абстрактний клас
class Animal(ABC):  # Оголошуємо абстрактний клас Animal, який успадковує ABC
    def __init__(self, name):
        self._name = name  # protected (напівзакритий) атрибут — використовується для зберігання імені

    @abstractmethod
    def make_sound(self):
        """Абстрактний метод, який зобов'язаний реалізовуватись у всіх похідних класах"""
        pass  # Не має реалізації тут, лише у дочірніх класах

    def describe(self):
        """Звичайний метод, який повертає опис тварини (назва класу та ім'я)"""
        return f"This is a {self.__class__.__name__} named {self._name}."

# 2. Інкапсуляція в похідних класах
class Dog(Animal):  # Клас Dog наслідує Animal
    def __init__(self, name, breed):
        super().__init__(name)  # Викликаємо конструктор базового класу Animal
        self.__breed = breed    # приватний атрибут __breed (інкапсуляція)

    def make_sound(self):
        return "Woof!"  # Реалізуємо звук собаки

    def get_breed(self):  # Геттер для породи
        return self.__breed

    def set_breed(self, breed):  # Сеттер для породи
        self.__breed = breed

class Cat(Animal):  # Клас Cat наслідує Animal
    def __init__(self, name, color):
        super().__init__(name)   # Викликаємо конструктор Animal
        self.__color = color     # приватний атрибут __color (інкапсуляція)

    def make_sound(self):
        return "Meow!"  # Звук кота

    def get_color(self):   # Геттер для кольору
        return self.__color

    def set_color(self, color):  # Сеттер для кольору
        self.__color = color

class Parrot(Animal):  # Клас Parrot наслідує Animal
    def __init__(self, name, vocabulary):
        super().__init__(name)         # Викликаємо конструктор Animal
        self.__vocabulary = vocabulary # приватний атрибут __vocabulary

    def make_sound(self):
        return "Squawk!"  # Звук папуги

    def get_vocabulary(self):  # Геттер для словникового запасу
        return self.__vocabulary

    def set_vocabulary(self, vocabulary):  # Сеттер для словникового запасу
        self.__vocabulary = vocabulary

# 3. Поліморфізм: колекція та виклик методу
animals = [  # Створюємо список різних тварин — всі вони спадкоємці Animal
    Dog("Rex", "Labrador"),                  # Собака Rex породи Labrador
    Cat("Murchyk", "Black"),                 # Кіт Murchyk чорного кольору
    Parrot("Kesha", ["Hello", "Bye"])        # Папуга Kesha з початковим словниковим запасом
]

for animal in animals:                 # Перебираємо усіх тварин
    print(animal.describe())           # Виводимо опис (тип + ім'я) — метод з базового класу
    print(animal.make_sound())         # Викликаємо відповідний звук (реалізується у дочірніх класах)
    print()                            # Виводимо пустий рядок для відступу

# Приклад взаємодії з інкапсульованими полями:
print("Dog's breed:", animals[0].get_breed())  # Отримуємо породу собаки через геттер
animals[0].set_breed("Husky")                  # Змінюємо породу через сеттер
print("Dog's new breed:", animals[0].get_breed())  # Перевіряємо нову породу

print("Cat's color:", animals[1].get_color())  # Отримуємо колір кота через геттер
animals[1].set_color("White")                  # Змінюємо колір через сеттер
print("Cat's new color:", animals[1].get_color())  # Перевіряємо новий колір

print("Parrot vocabulary:", animals[2].get_vocabulary())  # Отримуємо словниковий запас папуги через геттер
animals[2].set_vocabulary(["Hi", "Good morning"])         # Змінюємо словниковий запас через сеттер
print("Parrot's new vocabulary:", animals[2].get_vocabulary())  # Перевіряємо оновлений словниковий запас

