import random

class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        return('Спасибо, хозяин!')

class ClovenFooted(Animal):
    def milk(self):
        return('Мы подоили корову')

class Sheep(Animal):
    def hair_cut(self):
        return('Баран пострижен')
    def say(self):
        return('Беее')

class Bird(Animal):
    def get_eggs(self):
        return(f'Снесено яиц: {random.randint(0,10)}')

class Duck(Bird):
    def say(self):
        return("Кря")

class Goose(Bird):
    def say(self):
        return("Гогого")

class Hen(Bird):
    def say(self):
        return("Кококо")

class Cow(ClovenFooted):
    def say(self):
        return("Мууу")

class Goat(ClovenFooted):
    def say(self):
        return("Меее")

duck = Duck("Кряква", 3)
grey = Goose('Серый',4)
white = Goose('Белый', 4.5)
koko = Hen('Ко-ко',1.3)
kukareku = Hen('Кукареку',1.4)
maria = Cow('Манька', 200)
horns = Goat('Рога', 50)
cloven = Goat('Копыта', 51)
barashek = Sheep('Барашек', 40)
curly = Sheep('Кудрявый', 45)

koko.get_eggs()
print(f'Наша утка орёт: "{duck.say()}"')
print(f'А гуси кричат: "{grey.say()}"')
print(f'Козы: "{horns.say()}"')
print(f'Бараны: "{curly.say()}"')
print(f'Корова: "{maria.say()}"')
print(maria.milk())
print(horns.feed())
print(koko.get_eggs())
print(barashek.hair_cut())

farm_animals = [grey, white, maria, barashek, curly, koko, kukareku, horns, cloven, duck]
total_weight = 0
hardest_animal = farm_animals[0]
for a in farm_animals:
    total_weight += a.weight
    if hardest_animal.weight < a.weight:
        hardest_animal = a
print(f'Общий вес скотины: {total_weight}. Самая тяжелая скотина - {hardest_animal.name}, её вес - {hardest_animal.weight}.')

