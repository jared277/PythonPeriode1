# Oefening 1
# Print de volgende zin "Hello World"

from os import name


print("Hello World")


# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = "Jared"
leeftijd = 16
woonstad = "Maarssen"


# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")
print (f"hallo mijn naam is {naam}")


# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"
game = "Subnautica "
uren = "65,7 "
cijfer = "10/10 "
print("Mijn favoriete game is " + game + "ik heb deze game " + str(uren) + "uur gespeeld", "Ik geef deze game een " + str(cijfer))


# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit
number1 = 2
number2 = 5
trueorfalse = number1 + number2 == 7
wasd = number2 - number1 == 3
dsaw = number1 * number2 == 10

print(dsaw)
# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit
name = "winston"
health = 100
level = 27
damage = 20
print(f"winston kreeg 20 damage health is nu:  {health - damage}")

# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 
wapen = "exalibur"
damage = 25
level = 28
print(f"winston heeft nu een {wapen} en zijn damage is nu {damage} en zijn level is nu {level}")

# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe
name = "winston"
age = 16
favouritegame = "subnautica"
hoursplayed = 65.7
level = 28
score = 1000
print(f"Naam: {name}")
print(f"Leeftijd: {age}")
print(f"Favoriete game: {favouritegame}")
print(f"Uren gespeeld: {hoursplayed}")
print(f"Niveau: {level}")
print(f"Score: {score}")