from abc import ABC, abstractmethod

# === STRATEGY PATTERN ===
# Абстрактна стратегія для руху робота
class MoveStrategy(ABC):
    @abstractmethod
    def move(self):
        # Абстрактний метод: реалізується в конкретних стратегіях руху
        pass

# Конкретна стратегія — рух пішки
class WalkStrategy(MoveStrategy):
    def move(self):
        print("Робот іде пішки.")

# Конкретна стратегія — рух на колесах
class RollStrategy(MoveStrategy):
    def move(self):
        print("Робот їде на колесах.")

# Конкретна стратегія — політ
class FlyStrategy(MoveStrategy):
    def move(self):
        print("Робот летить.")

# === STATE PATTERN ===
# Абстрактний стан робота
class RobotState(ABC):
    @abstractmethod
    def handle(self, robot):
        # Абстрактний метод: приймає робота як параметр
        pass

# Конкретний стан — очікування
class IdleState(RobotState):
    def handle(self, robot):
        print("Робот у режимі очікування.")

# Конкретний стан — робота (робот рухається)
class WorkingState(RobotState):
    def handle(self, robot):
        print("Робот виконує роботу.")
        robot.perform_move()  # Використовує поточну стратегію руху

# Конкретний стан — заряджання
class ChargingState(RobotState):
    def handle(self, robot):
        print("Робот заряджається.")

# === CONTEXT ===
# Клас робота, який має стратегію руху та поточний стан
class Robot:
    def __init__(self, move_strategy: MoveStrategy, state: RobotState):
        self.move_strategy = move_strategy  # Поточна стратегія руху
        self.state = state                  # Поточний стан робота

    def set_move_strategy(self, strategy: MoveStrategy):
        # Зміна стратегії руху
        self.move_strategy = strategy
        print("Змінено спосіб руху.")

    def set_state(self, state: RobotState):
        # Зміна стану робота
        self.state = state
        print("Змінено стан робота.")

    def perform_move(self):
        # Виклик методу поточної стратегії руху
        self.move_strategy.move()

    def do_action(self):
        # Виклик дії відповідно до поточного стану
        self.state.handle(self)

# === MAIN MENU ===
def main():
    # Створюємо робота з початковою стратегією руху (ходити) та станом (очікування)
    robot = Robot(WalkStrategy(), IdleState())

    while True:
        # Виводимо меню для взаємодії з користувачем
        print("\n=== Робот Меню ===")
        print("1. Змінити спосіб руху")
        print("2. Змінити стан")
        print("3. Виконати дію")
        print("4. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            # Вибір нової стратегії руху
            print("Виберіть спосіб руху:")
            print("a. Ходити")
            print("b. Їхати")
            print("c. Летіти")
            move_choice = input("Ваш вибір: ")
            if move_choice == 'a':
                robot.set_move_strategy(WalkStrategy())
            elif move_choice == 'b':
                robot.set_move_strategy(RollStrategy())
            elif move_choice == 'c':
                robot.set_move_strategy(FlyStrategy())
            else:
                print("Невірний вибір.")
        elif choice == '2':
            # Вибір нового стану робота
            print("Виберіть стан:")
            print("a. Очікування")
            print("b. Робота")
            print("c. Заряджання")
            state_choice = input("Ваш вибір: ")
            if state_choice == 'a':
                robot.set_state(IdleState())
            elif state_choice == 'b':
                robot.set_state(WorkingState())
            elif state_choice == 'c':
                robot.set_state(ChargingState())
            else:
                print("Невірний вибір.")
        elif choice == '3':
            # Виконати дію відповідно до поточного стану
            robot.do_action()
        elif choice == '4':
            # Завершити програму
            print("Завершення програми.")
            break
        else:
            print("Невірний вибір.")

# Запуск головної функції, якщо скрипт запускається напряму
if __name__ == "__main__":
    main()
