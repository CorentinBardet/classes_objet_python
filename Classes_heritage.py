class Personnage:

    max_life_point = 15
    def __init__(self):
        self.attack
        self.defense(points, arme)

class Warrior(Personnage):
    max_life_point = 25
    def __init__(self):
        self.name = "A determiner"

class Wizard(Personnage):
    max_life_point = 10
    def __init__(self):
        self.name = "A determiner"
class Archer(Personnage):
    def __init__(self):
        self.name = "A determiner"


wizard = Wizard("wiz1")
archer = Archer("arc1")

points, arme = archer.attack()
wizard.defense(points, arme)
wizard.life_point