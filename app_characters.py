import characters as char



def main():

    merlin = char.ElfeWizard("Merlin")
    attack_result = merlin.attack()
    weapon = attack_result["weapon"]
    dmg = attack_result["dmg"]

    stark = char.DwarfWizard("Stark")
    stark.defense(weapon, dmg)
    attack_result = stark.attack()
    weapon = attack_result["weapon"]
    dmg = attack_result["dmg"]

    merlin.defense(weapon, dmg)


    eve = char.Archer("Eve")
    attack_result = eve.attack()
    weapon = attack_result["weapon"]
    dmg = attack_result["dmg"]

    garen = char.Warrior("Garen")
    garen.defense(weapon, dmg)


if __name__ == "__main__":
    main()
