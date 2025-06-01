# === Composite Pattern ===

# Базовий компонент — спільний інтерфейс для окремих ігор та колекцій
class GameComponent:
    def show(self):
        # Абстрактний метод для відображення (має бути реалізований у нащадків)
        raise NotImplementedError()


# Leaf — окрема гра, що може бути у колекції
class GameItem(GameComponent):
    def __init__(self, game):
        self.game = game  # Об'єкт гри

    def show(self):
        # Делегуємо виклик show() самій грі
        self.game.show()


# Composite — колекція ігор, може містити інші GameComponent (ігри або підколекції)
class GameCollection(GameComponent):
    def __init__(self, name):
        self.name = name         # Назва колекції
        self.games = []          # Список компонентів (ігри/колекції)

    def add(self, component: GameComponent):
        # Додає компонент у колекцію
        self.games.append(component)

    def remove(self, component: GameComponent):
        # Видаляє компонент з колекції
        self.games.remove(component)

    def show(self):
        # Виводить назву колекції і всі її елементи
        print(f"\nКолекція: {self.name}")
        for game in self.games:
            game.show()  # Для кожного елемента викликає show() (поліморфізм)


# === Конкретні типи ігор (Action, Strategy) ===

class ActionGame:
    def __init__(self, title, developer, difficulty):
        self.title = title           # Назва гри
        self.developer = developer   # Розробник
        self.difficulty = difficulty # Складність

    def show(self):
        # Вивід інформації про action-гру
        print(f"[Action] {self.title} — by {self.developer} (Difficulty: {self.difficulty})")


class StrategyGame:
    def __init__(self, title, developer, players):
        self.title = title           # Назва гри
        self.developer = developer   # Розробник
        self.players = players       # Кількість гравців

    def show(self):
        # Вивід інформації про стратегію
        print(f"[Strategy] {self.title} — {self.players}-player by {self.developer}")


# === Facade Pattern ===

# Фасад — спрощує роботу з бібліотекою ігор для користувача
class GameLibraryManager:
    def __init__(self):
        # Головна колекція, корінь структури
        self.root_collection = GameCollection("Моя Ігрова Бібліотека")

    def add_action_game(self, title, developer, difficulty):
        # Створює action-гру та додає її до бібліотеки
        game = ActionGame(title, developer, difficulty)
        self.root_collection.add(GameItem(game))

    def add_strategy_game(self, title, developer, players):
        # Створює стратегію та додає її до бібліотеки
        game = StrategyGame(title, developer, players)
        self.root_collection.add(GameItem(game))

    def create_collection(self, name):
        # Створює нову підколекцію і додає її до root_collection
        group = GameCollection(name)
        self.root_collection.add(group)
        return group  # Повертає колекцію для подальшого наповнення

    def add_to_collection(self, group: GameCollection, item: GameComponent):
        # Додає гру/елемент до конкретної підколекції
        group.add(item)

    def show_all(self):
        # Відображає всю бібліотеку
        self.root_collection.show()


# === Демонстрація роботи Composite і Facade ===

def run_game_library_demo():
    manager = GameLibraryManager()  # Створюємо фасад

    print("== Додавання ігор ==")
    manager.add_action_game("CyberBlade", "NeoGames", "Hard")        # Додаємо action-гру
    manager.add_strategy_game("Empire Mind", "LogicSoft", 4)         # Додаємо стратегію

    print("\n== Створення підколекції ==")
    classics = manager.create_collection("Класичні Ігри")  # Створюємо підколекцію
    manager.add_to_collection(classics, GameItem(ActionGame("Retro Runner", "OldStudio", "Easy")))
    manager.add_to_collection(classics, GameItem(StrategyGame("Battle Grid", "TactiCorp", 2)))

    print("\n== Вміст бібліотеки ==")
    manager.show_all()   # Відображаємо всю ієрархію

# Точка входу
if __name__ == "__main__":
    run_game_library_demo()
