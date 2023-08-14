from essentials import Region
from essentials import Army

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


Freljord= Region('Freljord', 70, 50, False, {})
Player= Army("Bro", 80, 200)
clout= 20

test= combat(Player, Freljord, clout)
print(test)




        






    

    
