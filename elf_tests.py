"""
 You are an Elfin warrior:
Life: 80	Strength: 76	Speed: 85	Gold: 0

You are in a dungeon and come to a fork. You can go right or left.

If you go left you come to a room with a pot of 200 gold and a magic bracelet which increases your Strength by 10. Then you must go back to the fork and choose again.
   
If you go right, you are attacked by a Gorgon: 
Life: 50	Strength: 85	Speed: 10	Gold: 500	

You can choose to fight or flee:
 Flee: 
If your speed is greater than the Gorgon’s, you retreat back to the fork
If not, you lose 50 life and choose again

Fight:
If your Strength is greater, and your Life is greater: you win collect the gold and move on
Your strength is less and your life is more or strength is more, life is less: you lose 20 life points and choose again
Your strength is less and your life is less: you lose 50 life points and choose again

If your life goes below 0 you die.

test where user wins:
go left
go right
fight
Win!

test where user dies:
go right
fight
lose 20 life
go right
fight
lose 20 life
go right
fight
lose 50 life
die!

test where user neither wins or dies
right
flee
right
flee
left
right flee

"""

import sys
import math

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    print("tests for turn clockwise")
    #test(turn_clockwise("N") == "E")


elf = {"li":80,"str":76,"sp":85,"g":0}
gorgon = {"li":50,"str":85,"sp":10,"g":500}
goldpot = 200
bracelet = 10


def fork():
    """ the fork """
    choice = input("You are at a fork. Do you go right or left?")
    if choice == "left":
        goldroom()
    elif choice == "right":
        gorgonroom()
    else:
        print("Please enter 'right' or 'left'")
        fork()

def goldroom():
    global goldpot
    global bracelet
    elf["g"] += goldpot
    elf["str"] += bracelet
    
    
    print("You have gianed",goldpot,"in gold. and now you go back to the fork.")
    goldpot = 0
    bracelet = 0
    fork()
    
def gorgonroom():
    """gorgon"""
    choice = input("you are attacked by a Gorgon, do you fight or flee?")
    if choice == "flee":
        if elf["sp"] > gorgon["sp"]:
            print("You have fled the goron")
            fork()
        else:
            print("the gorgon got you! you lose 50 life!")
            elf["li"] -= 50
            gorgonroom()
    elif choice == "fight":
        if elf["str"] > gorgon["str"] and elf["li"] > gorgon["li"]:
            print("you win! collect 500 gold and move on")
            elf["g"] += gorgon["g"]
        elif (elf["str"] > gorgon["str"] and elf["li"] < gorgon["li"]) or (elf["str"] < gorgon["str"] and elf["li"] > gorgon["li"] ):
             print("you lose 20 life!")
             elf["li"] -= 20
             if checkdeath(elf["li"]):
                 return
             gorgonroom()
        else:
            print("you lose 50 life!")
            elf["li"] -= 50
            if checkdeath(elf["li"]):
                return
            gorgonroom()
    else:
        print("please enter 'fight' or 'flee'")
        gorgonroom()
    
    
def checkdeath(life):
    if life <= 0:
        print("you are dead. Game over.")
        return True
    else:
        "you are injured and have "+str(life)+" left"
        return False
  
    
    
    
    
fork()    
    