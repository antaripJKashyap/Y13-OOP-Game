class Army(object):

    def __init__(self, name, power, health):

        self.name= name
        self.power= power
        self.health= health
        enhancements= []    

    def sethealth(self, power):
        self.power= power

    def enhancements(self):
        return enhancements

    def addenhancement(self, power):
        enhacements.append(power)


class Region(object):

    def __init__(self, name, hitpoints, attack, conquered, nav):

        self.name= name
        self.hitpoints= hitpoints
        self.attack= attack
        self.conquered= conquered
        self.nav = {}

    def getname(self):
        return self.name
        

    def getnav(self):
        return self.nav

    def setnav(self, navupdate):
        self.nav= navupdate  


    def move(self, goto):

        if goto in self.nav:
            return self.nav[goto]

        else:
            print("Negative, sir, I do not see a way through there")
            return self





    

    
