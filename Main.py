from essentials import Region
from essentials import Army
import random
import pickle

##mechanics##

def combat(Army, Region, clout):

    #main combat subroutine to facilitate player attacking regions to conquer them

    retreat= False
    victory= False
    alive= True
    startinghp= Region.hitpoints
    damagedone= 0

    while alive == True and retreat == False and victory== False:
        
        Army.health= Army.health - Region.attack
        Region.hitpoints= Region.hitpoints - Army.power
        
        if Army.health <= 0:
            print("Farron: We're GOING UNDER!")
            alive = False
            return False

        if Region.hitpoints <=0 :
            victory= True
            damagedone = damagedone + (startinghp - Region.hitpoints)
            clout= clout + (damagedone/2)
            print("Farron: Defences are down, move in!")
            return True

        if Region.hitpoints > 0:
            damagedone = damagedone + (startinghp - Region.hitpoints)
            clout= clout + (damagedone/2)
            action= str(input("Sir, our army has", Army.health, "shall we continue? [Y/N]"))
            action= action.upper()
            actions= [ 'Y', 'N']
            if action in actions:
                valid= True

            while valid != True:
                action= str(input("try again"))                    
                if action in actions:
                    valid= True

            if action== 'Y':
                print("Farron: Affirmative! All forces, FALL BACK!")
                retreat= True
                return True

            elif action== 'N':
                print("Farron: COUNTER ATTACK!")
                
                
def saving():

    with open('game_save.dat', 'wb') as f:
        pickle.dump(Region.alldata, f)
        pickle.dump(Army.alldata, f)
        pickle.dump(worlddata, f)

def load():
    
    with open('game_save.dat', 'rb') as f:
        pickle.load(Region.alldata, f)


def dialogue(scenario):

    #random dialogues spoken by regions when they are attacked, chosen randomly

    select= random.randint(1,9)

    #under construction

   
        
##Regions and initialising their mechanics##

Valoran= Region('Valoran', 100, 0, True, {})
Raptor= Region('Port Raptor', 100, 20, True, {})
Bastion= Region('Bastion', 150, 120, True, {})
Freljord= Region('Freljord', 70, 50, False, {})
Icathia= Region('Icathia', 30, 70, False, {})
Targon= Region('Targon', 120, 40, False, {})
Shurima= Region('Shurima', 170, 90, False, {})
Demacia= Region('Demacia', 350, 40, False, {})
Ionia= Region('Ionia', 40, 60, False, {})

##Navigation##

Valoran.setnav({'North':Freljord, 'West':Demacia, 'South':Shurima, 'East':Bastion})
Raptor.setnav({'North':Bastion, 'Port':Ionia})
Bastion.setnav({'West':Valoran, 'South':Raptor, 'North':Freljord})
Freljord.setnav({'South':Valoran})
Targon.setnav({'West':Shurima, 'North':Valoran})
Shurima.setnav({'North':Valoran, 'East':Targon, 'West':Icathia})
Demacia.setnav({'West':Valoran, 'Port':Ionia})
Ionia.setnav({'Port':Raptor})

gameregions= [Valoran, Raptor, Bastion, Freljord, Icathia, Targon, Shurima, Demacia, Ionia]

##army##

Player= Army("", 80, 200)

#Everything Beyond this point is the main game loop

def main():

    ##vital variables##

    funds= 20000
    clout= 0
    income= 500
    navy= 1
    seigemod= 1
    negativemod= 1
    alive= True
    end= False
    
    current= Valoran
    print("Aide: Wake up, General, it is time")
    print("We need to consolidate our forces. Might wanna head back to the capital")
    
    while alive== True and end== False:

        actions= [ 'M', 'A']
        print("")
        print("[Current Location-", current.name,"]")
        print("[Funds-", funds,"]")
        print("[Income-", income," per turn]")
        print("[Clout-", clout, "]")
        print("")
        #entering a allows interactions with regions and their services or to conquer it
        action= str(input("Your orders, General.... ('m' to move or 'a' to summon Captain Farron)"))
        action= action.upper()

        #These if statements determine the actions you can perform depending on the region you are in
        
        if action in actions:

            if action == 'M':

                ##################IMPORTANT- TO MOVE, ENTER IN THE DIRECTION LIKE THIS- for east type in 'East' with first letter capital##############
                
                Direction= str(input("affirmative, general, where do we go"))
                current= current.move(Direction)

            elif action == 'A' and current.name== "Valoran":
                print("Captain Farron: General, This place is a waste land. I suggest we move along")

            elif action == 'A' and current.name== "Bastion":
                print("Captain Farron approaches you near the great city center. You see black granite walls all around you")
                print("Farron: Welcome to the heart of our Empire, The Bastion")
                print("We should demand an audience in the great court, consult the Emperor (Y)")                
                print("---------------")
                print("what do you say-")
                print("Y- 'Set up the meeting, It's about time we had a word with Emperor Titus'")
                print("N- 'On second thought, let's just move along'")
                actions= [ 'Y', 'N']                
                action= str(input("-"))
                action= action.upper()
                valid= False
                if action in actions:
                    valid= True

                while valid != True:
                    action= str(input("try again"))                    
                    if action in actions:
                        valid= True

                if action == 'Y':
                    print("[The Bastion-Upper Districts, Palace of the emperor]")
                    print("As you enter the room, you see Emperor Titus Mede II in his Rose gold royal robe")
                    print("Mede: Ah, General, you have returned")
                    print("Mede: I suppose you are here to propose your military reform initiaves, go on, I am listening")
                    print( clout, "here's how much clout you have right now, be sure to use your tongue wisely, im sure you know what the")
                    print("consequnce of insubordination is")
                    print("Farron: here's what we can propose, sir")
                    print("A: Increase military funding- permanently increase how much money you earn per turn, reduces cost of army (30)")
                    print("B: Military engineers- permanently increase the effectiveness of seige weaponry (20)")
                    print("C: Increase personnel- Request more soldiers (10)")
                    print("D: Onboard rations- Increases the survivability of your army in harsh conditions(25)")
                    print("E: Challenge for the imperial throne- Instantly wins the game (150)")
                    print("input N to back out")
                    actions= [ 'A', 'B', 'C', 'D', 'E', 'N']                
                    action= str(input("-"))
                    action= action.upper()
                    valid= False
                    if action in actions:
                        valid= True

                    while valid != True:
                        action= str(input("try again"))                    
                        if action in actions:
                            valid= True
                    if action == 'A':
                        if clout < 30:
                            alive = False

                        else:
                            income = income*2

                    if action == 'B':
                        if clout < 20:
                            alive = False
                        else:
                            seigemod = seigemod + 1

                    if action == 'C':
                        if clout < 10:
                            alive = False

                        else:
                            print("working on it")
                    
                    if action == 'D':
                        if clout < 25:
                            alive = False

                        else:
                            negativemod= negativemod/2

                    if action == 'F':
                        if clout < 150:
                            alive = False

            elif action == 'A' and current.name== "Freljord":
                print("Farron: Freljord, the Northern lands. I hope the army's packed up their warm wear, they'll need it.")
                print("Not much to say, the natives don't seem very organised so getting through the defences should be easy.")
                print("There are various tribes though, so they should have plenty of strong offensive capabilities")
                        
                                    

            elif action == 'A' and current.name== "Port Raptor":
                print("Farron: Welcome to Port Raptor sir, what's the plan?")
                print("Would you like to consult naval power? (N)")
                print("or would you like to upgrade our weaponry? {S)")
                print("---------------")
                print("what do you say-")
                print("N- 'take us to the admiral, I'll handle this myself'")
                print("S- 'take us to the quartermaster, the catapults could use more oil'")
                print("E- 'at ease, captain, we'll move along'")
                actions= [ 'N', 'S', 'E']                
                action= str(input("-"))
                action= action.upper()
                valid= False
                if action in actions:
                    valid= True

                while valid != True:
                    action= str(input("try again"))                    
                    if action in actions:
                        valid= True

                if action == 'N':
                    #Allows the Player to make conquests easier by weakening enemy regions
                    print("[Port Raptor, Salughter Docks]")
                    print("Admiral: Pleasure to see you again, would you like to acquire a Naval distress Flair?")
                    print("Out there, an army will do you good, but with Naval support, nothing can stand in your way")
                    print("you currently have", navy, "distress calls left to use, you can buy one more for 9000")
                    print("[Y/N]")
                    actions= [ 'Y', 'N']
                    action= str(input(""))
                    action= action.upper()
                    valid= False
                    if action in actions:
                        valid= True

                    while valid != True:
                        action= str(input("try again"))                    
                        if action in actions:
                            valid= True

                    if action == 'Y':
                        if funds < 9000:
                            print("You do not have the appropriate funds to finance another naval support incursion")

                        else:
                            funds= funds - 9000
                            navy= navy + 1

                
                if action == 'S':
                    #Allows the Player to make conquests easier by strengthening your army
                    print("[Port Raptor, Barracks]")
                    print("Quarter-master: Welcome, General, what will you have?")
                    print("We can replace your weaponry with the sturdier Iron Breaker mine produced swords and crossbows for 12000 (W)")                    
                    print("or if you prefer prefer superior armor, that can be arragend too for 11000 (A)")
                    print("[W/A/N(to ignore)]")
                    actions= [ 'W', 'A', 'N']
                    action= str(input(""))
                    action= action.upper()
                    valid= False
                    if action in actions:
                        valid= True

                    while valid != True:
                        action= str(input("try again"))                    
                        if action in actions:
                            valid= True

                    if action == 'W':
                        if funds < 12000:
                            print("You do not have the appropriate funds to finance another naval support incursion")

                        else:
                            funds= funds - 12000
                            Player.power += 40

                    elif action == 'A':
                        if funds < 11000:
                            print("You do not have the appropriate funds to finance another naval support incursion")

                        else:
                            funds= funds - 11000
                            Player.health += 35
                            

        else:
            print("")
            print("I didnt catch that")
            print("")

        funds= funds + income
        
        print("--------------------------------------------------------------------")
        print("--------------------------------------------------------------------")
        print("--------------------------------------------------------------------")
        print("--------------------------------------------------------------------")

main()
print("mission failed, Generla, its over")
