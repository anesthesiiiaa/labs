import copy  # Імпортуємо модуль для глибокого копіювання об'єктів

# === Базовий клас Prototype ===
class DocumentTemplate:
    def __init__(self, title, content):
        self.title = title      # Назва документа
        self.content = content  # Вміст документа

    def duplicate(self):
        # Метод для створення повної копії (клонування) об'єкта
        return copy.deepcopy(self)

    def show(self):
        # Абстрактний метод для відображення інформації про документ
        # Має бути реалізований у дочірніх класах
        raise NotImplementedError("Subclasses must implement this method")

# === Клас для текстового документа ===
class TextDocument(DocumentTemplate):
    def __init__(self, title, content, font):
        # Викликаємо конструктор батьківського класу
        super().__init__(title, content)
        self.font = font  # Додаємо додатковий атрибут: шрифт

    def show(self):
        # Виводимо інформацію про текстовий документ
        print(f"TextDocument:\n Title: {self.title}\n Font: {self.font}\n Content: {self.content}\n")

# === Клас для таблиці ===
class Spreadsheet(DocumentTemplate):
    def __init__(self, title, content, rows, columns):
        # Викликаємо конструктор батьківського класу
        super().__init__(title, content)
        self.rows = rows        # Кількість рядків
        self.columns = columns  # Кількість стовпців

    def show(self):
        # Виводимо інформацію про таблицю
        print(f"Spreadsheet:\n Title: {self.title}\n Size: {self.rows}x{self.columns}\n Content: {self.content}\n")

# === Демонстрація патерну Prototype ===
def run_demo():
    print("== Створення шаблонів документів ==")
    # Створюємо шаблон текстового документа
    text_template = TextDocument("Звіт", "Це шаблон звіту.", "Arial")
    # Створюємо шаблон таблиці
    sheet_template = Spreadsheet("Таблиця", "Шаблон фінансових даних", 10, 5)

    # Виводимо початкові шаблони
    text_template.show()
    sheet_template.show()

    print("== Клонування шаблонів ==")
    # Клонування об'єктів (створення копій)
    text_clone = text_template.duplicate()
    sheet_clone = sheet_template.duplicate()

    # Змінюємо атрибути у копіях
    text_clone.title = "Звіт про прибутки"
    text_clone.content = "Детальний звіт за квартал"
    text_clone.font = "Times New Roman"

    sheet_clone.title = "Копія таблиці"
    sheet_clone.rows = 20  # Зміна розміру таблиці

    print("Оригінали:")
    # Виводимо оригінальні шаблони — вони не змінились!
    text_template.show()
    sheet_template.show()

    print("Копії:")
    # Виводимо копії — зміни видно тільки у них
    text_clone.show()
    sheet_clone.show()

# Стартуємо програму, якщо файл запущено напряму
if __name__ == "__main__":
    run_demo()
