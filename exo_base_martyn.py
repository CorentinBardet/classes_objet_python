from random import randint


class Animal:
    hair_style = "lisse"
    life_esperance = None
    weight = 0
    color = None
    son_animal = None

    def __init__(self, name, weight, color, age):
        self.name = name
        self.weight = weight
        self.color = color
        self.age = age

    def get_life_esperance(self):
        if self.life_esperance is None:
            raise ValueError
        if self.life_esperance is not None:
            raise self.life_esperance

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 0 < value < self.life_esperance:
            self.__age = value
        else:
            raise Exception("l'age n'est pas le bon")

    age = property(get_age, set_age)

    def get_diet(self):
        aliments_diet = ["carotte", "choux", "croquette"]
        return aliments_diet

    def eat(self, aliments_diet):
        diet = self.get_diet()

        for aliment in diet:
            if aliment == aliments_diet:
                self.weight += (self.weight * 5 / 100)
                print(self.name + " a mangé")
                print(self.name + " fait " + str(self.weight))
                return True
            else:
                print(self.name + " n'a pas mangé ")
                return False

    def talk(self):
        return self.son_animal


class Cat(Animal):
    life_esperance = 15
    son_animal = "miaou"


class Snail(Animal):
    life_esperance = 2
    son_animal = "slurp"


class Snake(Animal):
    life_esperance = 8
    son_animal = "sss"


# -----------------------


lechat = Cat("lechat", 12, "noir", 2)
print(lechat.name + " fait " + lechat.talk())
lechat.eat("carotte")
lechat.eat("pascarotte")

lescargot = Snail("lescargot", 0.2, "marron", 3)
print(lescargot.name + " fait " + lescargot.talk())
lescargot.eat("goutte")

leserpent = Snake("leserpent", 2, "gris", 6)
print(leserpent.name + " fait " + leserpent.talk())

print(lescargot.age)
