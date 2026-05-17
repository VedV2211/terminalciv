import random
import time


# Allows for the player to input a save ID that will bring their items, factories and battle stage to a new run
saveDataUsed = False
saveDataQuery = input("What is your save ID? (leave empty if N/A) ")
if saveDataQuery != "":
    saveData = saveDataQuery.split()
    saveDataUsed = True
    difficultyQuery = saveData[14]
elif saveDataQuery == "":
    saveData = [0, 0, 0, 0, 0, 1, 0, 0, 0, 10, 20, 30, 50, 0, 1, 0]
    difficultyQuery = input("How difficult would you like this game to be? \nEasy (Press 1) \nNormal (Press 2) \nHard (Press 3) \nImpossible (Press 4) \nWhich difficulty? ")
    saveData[14] = difficultyQuery

    print("")
    print("You have just suceeded your ancestors as the new monarch of your country. \nYou must manage your kingdom's resources effectively while defeating the enemies that your family has been fighting for centuries. ")
    print("To begin with, you have been bequeathed with one farm. ")
    print("Will you rise to the challenge? ")
    print("")

timeSpent = saveData[15]
    
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

if difficultyQuery.lower() == "1":
    enemyHealth = [100, 200, 700, 2000, 5000, 10000, 20000]
    enemyStrength = [1, 2, 3, 5, 7, 10, 20]
elif difficultyQuery.lower() == "2":
    enemyHealth = [300, 600, 1200, 2700, 7000, 15000, 30000]
    enemyStrength = [2, 3, 5, 7, 10, 20, 25]
elif difficultyQuery.lower() == "3":
    enemyHealth = [1000, 2000, 7000, 5000, 10000, 25000, 50000]
    enemyStrength = [5, 10, 15, 25, 35, 50, 60]
elif difficultyQuery.lower() == "4":
    enemyHealth = [5000, 10000, 20000, 50000, 150000, 500000, 1000000]
    enemyStrength = [15, 35, 50, 75, 120, 200, 500]
else:
    print("Please start over. ")

enemyDefend = 0
battleStage = int(saveData[13])

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
        if (factory == 1) & (coins >= ((farmCost * nOF) + (((nOF ** 2) - nOF))/2)):
            for i in range(nOF):
                farms += 1
                coins -= farmCost
                farmCost += 1
        elif (factory == 2) & (food >= ((millCost * nOF) + (((nOF ** 2) - nOF))/2)): 
            for i in range(nOF):
                mills += 1
                food -= millCost
                millCost += 1
        elif (factory == 3) & (wood >= ((mineCost * nOF) + (((nOF ** 2) - nOF))/2)): 
            for i in range(nOF):
                mines += 1
                wood -= mineCost
                mineCost += 1
        elif (factory == 4) & (food >= ((barrackCost * nOF) + (((nOF ** 2) - nOF))/2)) & (wood >= ((barrackCost * nOF) + (((nOF ** 2) - nOF))/2)) & (metal >= ((barrackCost * nOF) + (((nOF ** 2) - nOF))/2)):
            for i in range(nOF):
                barracks += 1
                food -= barrackCost
                wood -= barrackCost
                metal -= barrackCost
                barrackCost += 1
        elif factory >= 5:
            print("Come again soon! ")
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
                    enemyAttack = (random.randint(20, 60)) * ((enemyStrength[battleStage]) ** 2)
                    soldiersDefend -= enemyAttack
                    if soldiersDefend < 0:
                        soldiers += round(soldiersDefend/soldiers)
                    print("    The enemy did " + str(enemyAttack) + " damage to you.")

                elif enemyAttackchoice == 2:
                    enemyHealed = (random.randint(5,20)) * (enemyStrength[battleStage] ** 2)
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
            coins += farms + mills + mines + barracks
            food += farms
            wood += mills
            metal += mines
            soldiers += barracks 
            time.sleep(1)
            timeSpent += 1
            if i == 0:
                print("    It has now been 1 year.")
            else:
                print("    It has now been " + str(i + 1) + " years.")
            if (coins < 0) or (food < 0) or (wood < 0) or (metal < 0):
                print("You have run out of resources, and your kingdom is on the brink of perishing. ")
                break
        print("")
    
    # The user's save ID is printed out
    elif choice == "6":
        print(str(coins) + str(" ") + str(food) + str(" ") + str(wood) + str(" ") + str(metal) + str(" ") + str(soldiers) + str(" ") + str(farms) + str(" ") + str(mills) + str(" ") + str(mines) + str(" ") + str(barracks) + str(" ") + str(farmCost) + str(" ") + str(millCost) + str(" ") + str(mineCost) + str(" ") + str(barrackCost) + str(" ") + str(battleStage) + str(" ") + str(difficultyQuery) + str(" ") + str(timeSpent))
    
    # The user can get basic help
    elif choice.lower() == "help":
        print("Choose a number for your choice unless in battle, where you choose to attack or defend. ")
   
    if battleStage == 7:
        print("")
        print("")
        print("You beat the game! ")
        print("You had: \n    " + str(coins) + " coins\n    " + str(food) + " food\n    " + str(wood) + " wood\n    " + str(metal) + " metal\n    " + str(soldiers) + " soldiers.")
        print("It took you " + str(timeSpent) + " years. Think you can do better? ")
        print("")
        print("")
        choice = "7"
    else: 
        choice = input("1. Check how many of each item you have \n2. Check how many of each factory you have \n3. Purchase more factories \n4. Go to battle at level " + str((battleStage + 1)) + "\n5. Wait for a certain number of years. \n6. Obtain your Save Data \n7. Quit \nWhat would you like to do? (help for help) ")
