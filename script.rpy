# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define a = Character('Announcer', color="#c8ffc8")

# the python starts here!

init python:
    fightType = 'one'
    
    #weapon, shirt, ring
    class Items(object):
        def __init__(self, agility, intellect, constitution, strength)
            self.agi = agility
            self.int = intellect
            self.con = constitution
            self.str = strength
    
    #weapon, shirt, ring
    class Equipped(dict):
        
    
    worn = Equipped('Weapon': none, 'Shirt': none, 'Ring': none)
    
    class Player(object):
        def __init__(self, experience, level, agility, intellect, constitution, strength, money, skillPoints):
            self.exp = experience
            self.lvl = level
            self.agi = agility
            self.int = intellect
            self.con = constitution
            self.str = strength
            self.money = money
            self.skill = skillPoints
            
        @property
        def mainStat(self):
            if fightType == 'ranged':
                return self.agi
            elif fightType == 'melee':
                return self.str
            elif fightType == 'magic':
                return self.int
        
        @property
        def dodge(self):
            return ((self.agi + worn.agi) * 0.5) + ((self.int + worn.int) * 0.2) + worn.dodge
        
        @property
        def minDamage(self):
            return (self.mainStat * 0.6) + worn.damage
        
        @property
        def maxDamage(self):
            return (self.mainStat * 1.1) + worn.damage
        
        @property
        def mDef(self):
            return ((self.con + worn.con) * 0.3) + ((self.int + worn.int) * 0.5) + worn.mDef
        
        @property
        def pDef(self):
            return ((self.con + worn.con) * 0.3) + ((self.str + worn.str) * 0.5) + worn.pDef
        
        @property
        def toHit(self):
            return (self.mainStat * 0.2) + (((self.agi + worn.agi) + (self.str + worn.str) + (self.int + worn.int)) / 6) + worn.toHit
        
        @property
        def crit(self):
            return  ((self.agi + worn.agi) * 0.5) + worn.crit
        
        @property
        def hp(self):
            return ((self.con + worn.con) * 10) + worn.hp
        
        @property
        def mana(self):
            return ((self.int + worn.int) * 3) + worn.mana
            
        #checks to see if can level up
        def lvlUp(self):
            expNeeded = 1000 * (0.9 + (self.lvl * 0.1))
            if self.exp >= expNeeded:
                self.exp =- expNeeded
                self.lvl =+ 1


# The game starts here.
label start:
    a "Welcome to the games!"

    a "How do you like to fight?"
    
    menu:

        "Hands on! Rawr!":

            jump melee

        "...from far away":

            jump ranged

        "With magic!":

            jump magic
            
label melee:
    $ fightType = 'melee'
    $ pc = Player(0, 1, 10, 10, 10, 15, 0, 0)
    a "Here have an axe."
    ##Code to give random axe
    jump main
    
label ranged:
    $ fightType = 'ranged'
    $ pc = Player(0, 1, 15, 10, 10, 10, 0, 0)
    a "Here have a bow."
    ##random bow
    jump main
    
label magic:
    $ fightType = 'magic'
    $ pc = Player(0, 1, 10, 15, 10, 10, 0, 0)
    a "Here have a spell book."
    ##random spell book
    jump main
    
label main:
    menu:
        "Fight!":
            jump fight
        "Stats":
            jump stats
        "Equipment":
            jump equipment
        "Pack":
            jump pack
        "Quit":
            "Bye bye"
            $ renpy.quit()
        
label fight:
    a "We're not ready for you yet."
    jump main
    
label stats:
    $ ui.text("Level: %d Experience: %d Health: %d Mana: %d Agility: %d Strength: %d Intelligence: %d Constitution: %d" %(pc.lvl, pc.exp, pc.hp, pc.mana, pc.agi, pc.str, pc.int, pc.con))
    pause
    jump main
    
label equipment:
    a "Can't access this yet."
    jump main
    
label pack:
    a "It's okay you aren't carrying anything anyway."
    jump main