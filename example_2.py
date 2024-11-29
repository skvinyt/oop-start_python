import random

class House:
    def __init__(self):
        self.food = 50
        self.money = 0

    def __str__(self):
        return f"Дом: Еда = {self.food}, Деньги = {self.money}"

class Human:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        if self.house.food >= 10:
            self.satiety += 10
            self.house.food -= 10
            print(f"{self.name} поел. Сытость = {self.satiety}, Еда в доме = {self.house.food}")
        else:
            print(f"{self.name} не может поесть: недостаточно еды в доме.")

    def work(self):
        self.satiety -= 10
        self.house.money += 50
        print(f"{self.name} работал. Сытость = {self.satiety}, Деньги в доме = {self.house.money}")

    def play(self):
        self.satiety -= 10
        print(f"{self.name} играл. Сытость = {self.satiety}")

    def shop_for_food(self):
        if self.house.money >= 50:
            self.house.food += 50
            self.house.money -= 50
            print(f"{self.name} сходил в магазин. Еда в доме = {self.house.food}, Деньги в доме = {self.house.money}")
        else:
            print(f"{self.name} не может сходить в магазин: недостаточно денег.")

    def live_day(self):
        dice = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.shop_for_food()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()

        if self.satiety < 0:
            print(f"{self.name} умер от голода.")
            return False
        return True

    def __str__(self):
        return f"Человек: {self.name}, Сытость = {self.satiety}, {self.house}"

# Пример использования
house = House()
human1 = Human("Артём", house)
human2 = Human("Мария", house)

for day in range(1, 366):
    print(f"\nДень {day}:")
    if not human1.live_day():
        break
    if not human2.live_day():
        break
    print(human1)
    print(human2)
else:
    print("Оба человека выжили 365 дней!")
