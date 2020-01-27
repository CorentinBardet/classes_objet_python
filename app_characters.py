import characters as char


def main():

    merlin = char.Wizard("Merlin")
    weapon, dmg = merlin.attack()


    stark = char.Wizard("Stark")

    stark.defense(weapon, dmg)
    weapon, dmg = stark.attack()
    merlin.defense(weapon, dmg)

    eve = char.Archer("Eve")
    weapon, dmg = eve.attack()

    garen = char.Warrior("Garen")

    garen.defense(weapon, dmg)


if __name__ == "__main__":
    main()
