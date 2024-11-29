class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = False
        self.hungry = True

    def __str__(self):
        calm_status = "спокоен" if self.calm else "не спокоен"
        hungry_status = "сыт" if not self.hungry else "голоден"
        return f"Ребёнок: {self.name}, Возраст: {self.age}, Состояние: {calm_status}, Голод: {hungry_status}"

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, child):
        if self.age - child.age >= 16:
            self.children.append(child)
        else:
            print(f"Ребёнок {child.name} не может быть добавлен: разница в возрасте меньше 16 лет.")

    def info(self):
        return f"Родитель: {self.name}, Возраст: {self.age}, Дети: {len(self.children)}"

    def calm_child(self, child):
        if child in self.children:
            child.calm = True
            print(f"{self.name} успокоил {child.name}.")
        else:
            print(f"{child.name} не является ребёнком {self.name}.")

    def feed_child(self, child):
        if child in self.children:
            child.hungry = False
            print(f"{self.name} покормил {child.name}.")
        else:
            print(f"{child.name} не является ребёнком {self.name}.")

    def __str__(self):
        children_info = "\n".join(str(child) for child in self.children)
        return f"{self.info()}\nДети:\n{children_info}"

# Пример использования
parent = Parent("Вася", 35)
child1 = Child("Коля", 10)
child2 = Child("Маша", 5)

parent.add_child(child1)
parent.add_child(child2)

print(parent)

parent.calm_child(child1)
parent.feed_child(child2)

print(parent)
