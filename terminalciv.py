import random
import time

# add a time freeze that is aboolean value so that time only increases outside of battle or a menu. hvae a random chance for the country to implode natural disease etc.

coins = 10
food = 0
wood = 0
metal = 0
soldiers = 0

# These are the number of factories that the player starts with
farms = 0
mills = 0
mines = 0
barracks = 0

# These is the cost of a factory at the start of the game
farmCost = 10
millCost = 20
mineCost = 30
barracksCost = 50

# These are the actions that the player can take in battle
attack = 6
defend = 6
soldiersDefend = 0
hand = ["attack", "defend"]
enemyHealth = [100, 200, 500, 1000, 1500, 3000]
enemyStrength = [1, 2, 3, 5, 7, 10]
enemyDefend = 0
battleStage = 0 

choice = int(input("1. Check how many of each item you have \n2. Check how many of each factory you have \n3. Purchase more factories \n4. Go to battle at level " + str((battleStage + 1)) + " \n5. Wait for a certain number of years. \n6. Quit \nWhat would you like to do? "))

while choice != 6:

    if choice == 1:
        print("")
        print("    You have " + str(coins) + " coins. ")
        print("    You have " + str(food) + " food. ")
        print("    You have " + str(wood) + " wood. ")
        print("    You have " + str(metal) + " metal. ")
        print("    You have " + str(soldiers) + " soldiers. ")
        print("")

    elif choice == 2:
        print("")
        print("    You have " + str(farms) + " farms. ")
        print("    You have " + str(mills) + " mills. ")
        print("    You have " + str(mines) + " mines. ")
        print("    You have " + str(barracks) + " barracks. ")
        print("")

    elif choice == 3:
        factorychoice = input("    Which factory would you like to buy? \n    1. The farm costs " + str(farmCost) + "coins. You will have " + str(farms + 1) + " farms. \n    2. The mill costs " + str(millCost) + " food. You will have " + str(mills + 1) + " mills. \n    3. The mine costs " + str(mineCost) + " wood. You will have " + str(mines + 1) + " mines. \n    4. The barrack costs " + str(barracksCost) + "food, wood and metal. You will have " + str(barracks + 1) + " barracks. \n    5. I don't want to purchase anything. \nWhat would you like to do? ")
        factoryChoiceArray = factorychoice.split()
        factoryChoiceArray.append("1")
        factory = int(factoryChoiceArray[0])
        # short for numberOfFactories
        nOF = abs(int(factoryChoiceArray[1]))
        if (factory == 1) & (coins >= farmCost * nOF):
            farms += nOF 
            coins -= farmCost * nOF
        elif (factory == 2) & (food >= millCost * nOF):
            mills += 1
            food -= millCost * nOF
        elif (factory == 3) & (wood >= mineCost * nOF):
            mines += 1
            wood -= mineCost * nOF
        elif (factory == 4) & (food >= barracksCost * nOF) & (wood >= barracksCost * nOF) & (metal >= barracksCost * nOF):
            barracks += nOF
            food -= barracksCost * nOF
            wood -= barracksCost * nOF
            metal -= barracksCost * nOF
        elif factory > 5:
            print("        Please try again")
            # return to the same menu so that the user doesn't have to return manually 
        else:
            print("        You did not have enough resources. ")

    elif choice == 4:
        while (soldiers > 0):
            battlechoice = input(hand)
            if battlechoice == "attack":
                soldiersAttack = attack * soldiers
                enemyHealth[battleStage] -= soldiersAttack
                print("")
                print("    You did " + str(soldiersAttack) + " damage to the Enemy")
                print("")
            elif battlechoice == "defend":
                # change this to remove the soldiers once the battle is finished
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
    elif choice == 5:
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

    choice = int(input("1. Check how many of each item you have \n2. Check how many of each factory you have \n3. Purchase more factories \n4. Go to battle at level " + str((battleStage + 1)) + "\n5. Wait for a certain number of years. \n6. Quit \nWhat would you like to do? "))




