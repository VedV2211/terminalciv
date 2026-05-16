import random
import time

# Allows for the player to input a save ID that will bring their items, factories and battle stage to a new run 

saveDataUsed = False

saveDataQuery = input("What is your save ID? (leave empty if N/A) ")
if saveDataQuery != "":
    saveData = saveDataQuery.split()
    difficultyQuery = saveData[14]
    saveDataUsed = False
elif saveDataQuery == "":
    saveData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 20, 30, 50, 0]
    difficultyQuery = input("How difficult would you like this game to be? \nEasy\nMedium\nHard\nImpossible\nWhich difficulty? ")

# These are the items that the player starts with
coins = int(saveData[0])
food = int(saveData[1])
wood = int(saveData[2])
metal = int(saveData[3])
soldiers = int(saveData[4])


# These are the number of factories that the player starts with
farms = int(saveData[5])
mills = int(saveData[6])
mines = int(saveData[7])
barracks = int(saveData[8])

# These is the cost of a factory at the start of the game
farmCost = int(saveData[9])
millCost = int(saveData[10])
mineCost = int(saveData[11])
barrackCost = int(saveData[12])

# These are related to the player's battles 
attack = 6
defend = 6
soldiersDefend = 0
hand = ["attack", "defend"]

if difficultyQuery.lower() == "easy":
    enemyHealth = [100, 200, 700, 2000, 5000, 10000, 20000]
    enemyStrength = [1, 2, 3, 5, 7, 10, 20]
elif difficultyQuery.lower() == "normal":
    enemyHealth = [300, 600, 1200, 2700, 7000, 15000, 30000]
    enemyStrength = [2, 3, 5, 7, 10, 20, 25]
elif difficultyQuery.lower() == "hard":
    enemyHealth = [1000, 2000, 7000, 5000, 10000, 25000, 50000]
    enemyStrength = [5, 10, 15, 25, 35, 50, 60]
elif difficultyQuery.lower() == "impossible":
    enemyHealth = [5000, 10000, 20000, 50000, 150000, 500000, 1000000]
    enemyStrength = [15, 35, 50, 75, 120, 200, 500]

enemyDefend = 0
battleStage = int(saveData[13])
if saveDataQuery == "":
    choice = input("Press 5 to wait for a certain number of years to start the game. ")
else:
    choice = input("Press any key to continue. ")
while choice != "7":
    # Prints out all of the player's items
    if choice == "1":
        print("")
        print("    You have " + str(coins) + " coins. ")
        print("    You have " + str(food) + " food. ")
        print("    You have " + str(wood) + " wood. ")
        print("    You have " + str(metal) + " metal. ")
        print("    You have " + str(soldiers) + " soldiers. ")
        print("")
    
    # Prints out all of the player's factories
    elif choice == "2":
        print("")
        print("    You have " + str(farms) + " farms. ")
        print("    You have " + str(mills) + " mills. ")
        print("    You have " + str(mines) + " mines. ")
        print("    You have " + str(barracks) + " barracks. ")
        print("")
    
    # This is a menu where the player can buy new factories 
    elif choice == "3":
        factorychoice = input("    Which factory would you like to buy? \n    1. The farm costs " + str(farmCost) + " coins. You will have " + str(farms + 1) + " farms. \n    2. The mill costs " + str(millCost) + " food. You will have " + str(mills + 1) + " mills. \n    3. The mine costs " + str(mineCost) + " wood. You will have " + str(mines + 1) + " mines. \n    4. The barrack costs " + str(barrackCost) + " food, wood and metal. You will have " + str(barracks + 1) + " barracks. \n    5. I don't want to purchase anything. \nWhat would you like to do? ")
        factoryChoiceArray = factorychoice.split()
        factoryChoiceArray.append("1")
        factory = int(factoryChoiceArray[0])
        # short for numberOfFactories
        nOF = abs(int(factoryChoiceArray[1]))
        if (factory == 1) & (coins >= farmCost * nOF):
            farms += nOF 
            coins -= farmCost * nOF
        elif (factory == 2) & (food >= millCost * nOF):
            mills += nOF
            food -= millCost * nOF
        elif (factory == 3) & (wood >= mineCost * nOF):
            mines += nOF
            wood -= mineCost * nOF
        elif (factory == 4) & (food >= barrackCost * nOF) & (wood >= barrackCost * nOF) & (metal >= barrackCost * nOF):
            barracks += nOF
            food -= barrackCost * nOF
            wood -= barrackCost * nOF
            metal -= barrackCost * nOF
        elif factory > 5:
            print("        Please try again")
        else:
            print("        You did not have enough resources. ")
    
    # This is for the battles
    elif choice == "4":
        if soldiers == 0:
            print("")
            print("You have no soldiers yet. Try getting barracks in the shop. ")
            print("")

        while (soldiers > 0):
            print(hand)
            battlechoice = input("What would you like to do? ")

            if battlechoice == "attack":
                soldiersAttack = attack * soldiers
                enemyHealth[battleStage] -= soldiersAttack
                print("")
                print("    You did " + str(soldiersAttack) + " damage to the Enemy")
                print("")

            elif battlechoice == "defend":
                soldiersDefend = defend * soldiers
                print("")
                print("    You applied a shield for " + str(soldiersDefend) + " shield points. ")

            enemyAttackchoice = random.randint(1,2)

            if enemyHealth[battleStage] > 0:
                if enemyAttackchoice == 1:
                    enemyAttack = ((random.randint(20, 60)) * enemyStrength[battleStage])
                    soldiersDefend -= enemyAttack
                    if soldiersDefend < 0:
                        soldiers += round(soldiersDefend/soldiers)
                    print("    The enemy did " + str(enemyAttack) + " damage to you.")

                elif enemyAttackchoice == 2:
                    enemyHealed = (random.randint(5,20)) * enemyStrength[battleStage]
                    print("    The enemy used their medical supplies and healed " + str(enemyHealed) + " health points. ")
                    enemyHealth[battleStage] += enemyHealed

            if enemyHealth[battleStage] <= 0:
                print("")
                print("    You have won this battle stage! ")
                print("")
                battleStage += 1
                break

            elif soldiers <= 0:
                print("")
                print("    All of your soldiers died. ")
                soldiers = 0
                print("")
                break

            else:
                print("")
                print("    You have " + str(soldiers) + " soldiers. ")
                print("    The enemy has " + str(enemyHealth[battleStage]) + " health")
                print("")

    # The user can wait for a certain number of years (seconds) which gains resources 
    elif choice == "5":
        years = int(input("How long would you like to wait for? "))
        print("")
        for i in range(years):
            coins += 1
            food += farms
            wood += mills
            metal += mines
            soldiers += barracks
            time.sleep(1)
            if i == 0:
                print("    It has now been 1 year.")
            else:
                print("    It has now been " + str(i + 1) + " years.")
        print("")

    # The user's save ID is printed out
    elif choice == "6":
        print(str(coins) + str(" ") + str(food) + str(" ") + str(wood) + str(" ") + str(metal) + str(" ") + str(soldiers) + str(" ") + str(farms) + str(" ") + str(mills) + str(" ") + str(mines) + str(" ") + str(barracks) + str(" ") + str(farmCost) + str(" ") + str(millCost) + str(" ") + str(mineCost) + str(" ") + str(barrackCost) + str(" ") + str(battleStage) + str(" ") + str(difficultyQuery))
    
    # The user can get basic help
    elif choice.lower() == "help":
        print("Choose a number for your choice unless in battle, where you choose to attack or defend. ")
    
    if battleStage == 7:
        print("")
        print("")
        print("You beat the game! ")
        print("")
        print("")
        choice = 7
    else: 
        choice = input("1. Check how many of each item you have \n2. Check how many of each factory you have \n3. Purchase more factories \n4. Go to battle at level " + str((battleStage + 1)) + "\n5. Wait for a certain number of years. \n6. Obtain your Save Data \n7. Quit \nWhat would you like to do? (help for help) ")




