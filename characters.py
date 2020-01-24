from random import randint


class Wizard:
    max_life_point = 15
    magic_dice = 12
    sword_dice = 8
    bow_dice = 10
    attack_points = 0
    defense_points = 0

    def __init__(self, name, ):
        self.name = name
        self.current_life = self.max_life_point
        self.inventory = []

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




