import random

# Data
male_names = ["Kael", "Aether", "Rin", "Zero"]
female_names = ["Luna", "Nyx", "Eclipse", "Salem"]

fantasy_powers = ["Fire magic", "Healing", "Ice manipulation"]
cyberpunk_powers = ["Hacking", "Electric powers", "Cyber vision"]
horror_powers = ["Curse magic", "Fear illusion", "Soul stealing"]

fantasy_weapons = ["Sword", "Magic staff", "Bow"]
cyberpunk_weapons = ["Laser blade", "Tech gun", "Energy chains"]
horror_weapons = ["Rusty axe", "Scythe", "Dagger"]

personalities = [
    "Chaotic",
    "Cold",
    "Energetic",
    "Mysterious",
    "Quiet",
    "Manipulative"
]

# Title
print("=== FULL INTERACTIVE OC GENERATOR ===")

# Gender
print("\nChoose gender:")
print("1. Male")
print("2. Female")

gender_choice = input("Enter choice: ")

if gender_choice == "1":
    gender = "Male"
    names = male_names

elif gender_choice == "2":
    gender = "Female"
    names = female_names

else:
    print("Invalid choice.")
    exit()

# Genre
print("\nChoose genre:")
print("1. Fantasy")
print("2. Cyberpunk")
print("3. Horror")

genre_choice = input("Enter choice: ")

if genre_choice == "1":
    genre = "Fantasy"
    powers = fantasy_powers
    weapons = fantasy_weapons

elif genre_choice == "2":
    genre = "Cyberpunk"
    powers = cyberpunk_powers
    weapons = cyberpunk_weapons

elif genre_choice == "3":
    genre = "Horror"
    powers = horror_powers
    weapons = horror_weapons

else:
    print("Invalid choice.")
    exit()

# Personality
print("\nChoose personality:")

for i, personality in enumerate(personalities, start=1):
    print(f"{i}. {personality}")

personality_choice = int(input("Enter choice: "))

if 1 <= personality_choice <= len(personalities):
    personality = personalities[personality_choice - 1]
else:
    print("Invalid choice.")
    exit()

# Weapon
print("\nChoose weapon:")

for i, weapon in enumerate(weapons, start=1):
    print(f"{i}. {weapon}")

weapon_choice = int(input("Enter choice: "))

if 1 <= weapon_choice <= len(weapons):
    weapon = weapons[weapon_choice - 1]
else:
    print("Invalid choice.")
    exit()

# Power
print("\nChoose power:")

for i, power in enumerate(powers, start=1):
    print(f"{i}. {power}")

power_choice = int(input("Enter choice: "))

if 1 <= power_choice <= len(powers):
    power = powers[power_choice - 1]
else:
    print("Invalid choice.")
    exit()

# Random name
name = random.choice(names)

# Final OC
print("\n=== YOUR OC ===")
print("Name:", name)
print("Gender:", gender)
print("Genre:", genre)
print("Personality:", personality)
print("Weapon:", weapon)
print("Power:", power)
