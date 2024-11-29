class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2

class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"

class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        else:
            return "Обычный"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            raise ValueError('Недопустимый тип животного')

# Пример использования
factory = AnimalFactory()

# Создание птицы
bird = factory.create_animal('Bird', 'Орёл', 200)
print(f"Птица: {bird.name}, Размах крыльев: {bird.wingspan}, Длина крыла: {bird.wing_length()}")

# Создание рыбы
fish = factory.create_animal('Fish', 'Лосось', 50)
print(f"Рыба: {fish.name}, Максимальная глубина: {fish.max_depth}, Категория глубины: {fish.depth()}")

# Создание млекопитающего
mammal = factory.create_animal('Mammal', 'Слон', 5000)
print(f"Млекопитающее: {mammal.name}, Вес: {mammal.weight}, Категория: {mammal.category()}")
