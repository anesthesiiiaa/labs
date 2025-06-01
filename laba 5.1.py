class Machine:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} is starting")

    def stop(self):
        print(f"{self.name} is stopping")

    def recharge(self):
        print(f"{self.name} is recharging")

    def malfunction(self):
        print(f"{self.name} has malfunctioned")


class Car(Machine):
    def drive(self):
        print(f"{self.name} is driving")

    def honk(self, another):
        print(f"{self.name} honks at {another.name}")


class Robot(Machine):
    def speak(self):
        print(f"{self.name} says: 'Hello, human!'")

    def help(self, other):
        print(f"{self.name} helps {other.name} with a task")


Tesla = Car("Tesla")
Robo = Robot("Robo")

Tesla.honk(Robo)
Robo.help(Tesla)

Tesla.start()
Tesla.drive()
Tesla.recharge()
Tesla.stop()

print()

Robo.start()
Robo.speak()
Robo.recharge()
Robo.malfunction()
