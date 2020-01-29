from random import randint
import webbrowser as web

class Char:
    max_life_point = 12
    magic_dice = 12
    sword_dice = 8
    bow_dice = 10
    attack_points = 0
    defense_points = 0
    bow_bonus = 0
    sword_bonus = 0

    def __init__(self, name):
        self.name = name
        self.current_life = self.max_life_point
        self.inventory = []
        self._random_height = randint(170, 190)
        self._random_weight = randint(70, 90)

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
        bow_dice = randint(1, self.bow_dice)
        roll_dices = [["bow", bow_dice], ["swords", sword_dice], ["magic", magic_dice]]
        return roll_dices

    def attack(self):

        weapon, dmg = sorted(self.rolls_dice(), key=lambda x: x[1], reverse=True)[0]
        if weapon == "sword":
            dmg += self.sword_bonus
        elif weapon == "bow":
            dmg += self.bow_bonus
        print(self.name + " use " + weapon + " who's done " + str(dmg) + " DMG")
        return {"weapon": weapon, "dmg": dmg, "bonus": 0}

    def defense(self, weapon, dmg):

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

        attack_result = super().attack()
        weapon = attack_result["weapon"]
        dmg = attack_result["dmg"]
        bonus = attack_result["bonus"]
        magic_attack2 = randint(1, self.magic_dice)

        if dmg < magic_attack2:
            weapon = "magic"
            dmg = magic_attack2
        elif weapon == "sword":
            bonus += (self._random_height + self._random_weight) // 40
        elif weapon == "bow":
            bonus += (self._random_height - 170) % 3

        return {"weapon": weapon, "dmg": dmg, "bonus": bonus}


class Archer(Char):
    magic_dice = 10
    sword_dice = 8
    bow_dice = 12

    def attack(self):
        result_attack = super().attack()
        bonus = 0

        if result_attack["weapon"] in ["sword", "magic"]:
            bonus += 1
            print(self.name + " did 1 bonus DMG cause use " + str(result_attack["weapon"]) + ". Total = " + str(
                result_attack["dmg"]) + " DMG")
            if result_attack["weapon"] == "sword":
                bonus += self._random_height // 40

            elif result_attack["weapon"] == "magic":
                bonus += self._random_weight // 20
        result_attack["dmg"] += bonus
        result_attack["bonus"] += bonus
        return result_attack


class Warrior(Char):
    max_life_point = 16
    magic_dice = 8
    sword_dice = 12
    bow_dice = 8

    def attack(self):
        result_attack = super().attack()
        bonus = 0

        if result_attack["weapon"] == "magic":
            bonus += self._random_weight // 30

        elif result_attack["weapon"] == "bow":
            bonus += (self._random_height - 170) % 3

        result_attack["dmg"] += bonus
        result_attack["bonus"] += bonus
        return result_attack


class Dwarf:
    sword_bonus = 2


class Elfe:
    bow_bonus = 2


class ElfeWizard(Elfe, Wizard):
    def as_html(self):
        return open("as_html.html")
    pass


class DwarfWizard(Dwarf, Wizard):
    pass


class ElfeArcher(Elfe, Archer):
    pass


class DwarfArcher(Dwarf, Archer):
    pass


class ElfeWarrior(Elfe, Warrior):
    pass


class DwarfWarrior(Dwarf, Warrior):
    pass
