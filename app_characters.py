import characters as char

merlin = char.Wizard("Merlin")
weapon, dmg = merlin.attack()

stark = char.Wizard("Stark")

stark.defense(weapon, dmg)
weapon, dmg = stark.attack()
merlin.defense(weapon, dmg)