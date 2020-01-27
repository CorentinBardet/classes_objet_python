from random import randint


class Char:
    max_life_point = 12
    magic_dice = 12
    sword_dice = 8
    bow_dice = 10
    attack_points = 0
    defense_points = 0

    def __init__(self, name):
        self.name = name
        self.current_life = self.max_life_point
        self.inventory = []
        self.random_height = randint(170, 190)
        self.random_weight = randint(70, 90)

    def get_height(self):
        return self._random_height

    def set_height(self, value):
        self._random_height = value

    height = property(get_height, set_height)

    def get_weight(self):
        return self._random_weight

    def set_weight(self, value):
        self._random_weighht = value

    weight = property(get_weight, set_height)

    def rolls_dice(self):
        magic_dice = randint(1, self.magic_dice)
        sword_dice = randint(1, self.sword_dice)
        bow_dice = randint(1, self.sword_dice)
        roll_dices = [["bow", bow_dice], ["swords", sword_dice], ["magic", magic_dice]]
        return roll_dices

    def attack(self):
        result_attack = sorted(self.rolls_dice(), key=lambda x: x[1], reverse=True)[0]
        weapon, dmg = result_attack
        print(self.name + " use " + weapon + " who's done " + str(dmg) + " DMG")
        return result_attack

    def defense(self, weapon, dmg):

        global damages_done
        roll_dices = dict(self.rolls_dice())
        def_roll = roll_dices[weapon]

        if def_roll <= dmg:
            damages_done = dmg - def_roll
            print(self.name + " defend himself with " + weapon + " who defend " + str(def_roll) + " DMG")
            print(self.name + " lost " + str(damages_done) + " HP ")
            self.current_life = self.current_life - damages_done

        else:
            print(self.name + " defend himself with " + weapon + " who defend " + str(def_roll) + " DMG")
            print(self.name + " has defend so lost no HP")

        print(self.name + " got " + str(self.current_life) + " HP ")
        return self.current_life


class Wizard(Char):
    magic_dice = 12
    sword_dice = 8
    bow_dice = 10

    def attack(self):
        weapon, dmg = super().attack()
        magic_attack2 = randint(1, self.magic_dice)

        if dmg < magic_attack2:
            return ["magic", magic_attack2]
        elif weapon == "sword":
            dmg += (self.random_height + self.random_weight) // 40
            return [weapon, dmg]
        elif weapon == "bow":
            dmg += (self.random_height - 170) % 3
        else:
            return [weapon, dmg]


class Archer(Char):
    magic_dice = 10
    sword_dice = 8
    bow_dice = 12

    def attack(self):
        result_attack = super().attack()

        if result_attack[0] in ["sword", "magic"]:
            result_attack[1] += 1
            print(self.name + " did 1 bonus DMG cause use " + str(result_attack[0]) + ". Total = " + str(
                result_attack[1]) + " DMG")
            if result_attack[0] == "sword":
                result_attack[1] += (self.random_height) // 40
            elif result_attack[0] == "magic":
                result_attack[1] += (self.random_weight) // 20
        return result_attack


class Warrior(Char):
    max_life_point = 16
    magic_dice = 8
    sword_dice = 12
    bow_dice = 8

    def attack(self):
        result_attack = super().attack()

        if result_attack[0] == "magic":
            result_attack[1] += (self.random_weight) // 30

        elif result_attack[0] == "bow":
            result_attack[1] += (self.random_height - 170) % 3

        return result_attack
