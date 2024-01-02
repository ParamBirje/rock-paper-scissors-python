import random
import time

options = ["🪨", "📃", "✂️"]

def displayResult(p:int, e:int) -> bool:

    if p == 0 and e == 1:
        return False
    elif p == 1 and e == 2:
        return False
    elif p == 2 and e == 0:
        return False
    elif p == e:
        return None
    else:
        return True


print("----------- 🕹️ ROCK PAPER SCISSORS -----------")

name = str(input("Enter your name: "))

print(f"\n👋 Hello! {name.capitalize()}")
print("\nLet's GO 💨")

play = True

while play:
    print("\nYour choice: ")
    print('1 <-- 🪨 ROCK')
    print('2 <-- 📃 PAPER')
    print('3 <-- ✂️ SCISSORS')
    print('4 <-- Quit')
    playerChoice = int(input("--> ")) - 1

    rndm = random.randint(0, len(options)-1)
    enemyChoice = rndm

    print("\nEnemyAI's turn..")
    time.sleep(2)

    print(f"\n{name} --> {options[playerChoice]} .VS. {options[enemyChoice]} <-- EnemyAI")

    if playerChoice != 4:
        result = displayResult(playerChoice, enemyChoice)
    else:
        play = False
        continue

    print("\n")
    if result == True:
        print("🔥 VICTORY!")
    elif result == False:
        print('📛 DEFEAT')
    elif result == None:
        print('📍 DRAW')
    
    time.sleep(3)