from abc import ABC, abstractmethod  # Імпортуємо модуль abc для створення абстрактних класів та методів

# Абстрактний клас для повідомлень (Open/Closed Principle)
class Message(ABC):  # Базовий клас для різних типів повідомлень
    @abstractmethod
    def send(self):
        # Абстрактний метод: повинен бути реалізований у підкласах
        pass

# Реалізація SRP: кожен клас має одну відповідальність
class EmailMessage(Message):  # Клас для Email-повідомлення
    def __init__(self, recipient, subject):
        self.recipient = recipient  # Одержувач листа
        self.subject = subject      # Тема листа

    def send(self):
        # Реалізований метод send для Email
        return f"Sending email to {self.recipient} with subject '{self.subject}'"

class SMSMessage(Message):  # Клас для SMS-повідомлення
    def __init__(self, phone_number, text):
        self.phone_number = phone_number  # Номер телефону
        self.text = text                  # Текст повідомлення

    def send(self):
        # Реалізований метод send для SMS
        return f"Sending SMS to {self.phone_number}: '{self.text}'"

# Клас, відповідальний лише за логування (SRP)
class DeliveryLogger:  # Відповідає лише за виведення інформації про доставку
    def log_delivery(self, message: Message):
        print(message.send())  # Виводить результат відправки повідомлення

def start_delivery():
    # Демонструємо OCP: можна легко додати новий тип повідомлення
    email = EmailMessage("user@example.com", "Welcome to US!")   # Створюємо Email-повідомлення
    sms = SMSMessage("+38000234535", "Your code is 9876")        # Створюємо SMS-повідомлення
    # Можна додати новий тип, не змінюючи DeliveryLogger або Message

    logger = DeliveryLogger()   # Створюємо логгер для доставки
    logger.log_delivery(email)  # Виводимо результат доставки Email
    logger.log_delivery(sms)    # Виводимо результат доставки SMS

if __name__ == "__main__":     # Запускаємо функцію лише якщо цей файл є основним
    start_delivery()
