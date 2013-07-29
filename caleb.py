from sys import exit

def library():
    print "This is Falkland's Grand Library."
    print "There are several books you've been meaning to pick up here."
    print "How many do you take?"
    
    next = raw_input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Well you didn't type a number, so you've been killed.")

        if how_much < 5:
            print "That's a reasonable number of books."
            exit()
        else:
            dead("You carried too many and fainted of exhaustion")

def wash_room():
    print "You are in the matron's washroom."
    dead("The washroom is still under construction...")

def dead(why):
    print why, "Thanks for playing!"
    print  "If you enjoyed yourself consider donating bitcoin to this address: 18kKvHyye6cmQ6yUjUtHZvmZrhvmvnzkxo"
    exit(0)
    
def start():
    print "Welcome to PROTO Experiment 1:"
    print ""
    print ""
    print ""
    print ""
    print "Things as They Are; or,"
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    print ""
    print "                                    THE ADVENTURES OF...                                                       "
    print "_______ _______        _______ ______                 _  _  _ _____               _____ _______ _______ _______"
    print "|       |_____| |      |______ |_____]                |  |  |   |   |      |        |   |_____| |  |  | |______"
    print "|_____  |     | |_____ |______ |_____]                |__|__| __|__ |_____ |_____ __|__ |     | |  |  | ______|"
    print ""
    print ""
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    print "                                                  A Game by Anderson Evans based on the novel by William Godwin"
    print ""
    print ""
    print "                                                  My  life has for several years been a theatre of calamity.  I"
    print "                                                  have  been  a mark for the vigilance of tyranny, and I  could"
    print "                                                  not escape.  My fairest prospects have been blasted. My enemy"
    print "                                                  has shown himself inaccessible to entreaties,  and untired in"
    print "                                                  persecution. My fame, as well as my happiness, has become his"    
    print "                                                  victim.                                       -Caleb Williams"    
    print ""                                                                                                                
    print "This game is based on the 1794 novel by William Godwin."
    print "Your name is Caleb Williams, you work on the large estate of Ferdinando Fakland.  When you began your work here Fakland seemed like the best of men, however a twisted temper has begun to show at odd intervals."
    print "Today you will ask Old Collins why this might be..."
    print ""
    print "There is a door to your right and a door to your left."
    print "Which do you take?"
    print "(Type HELP for options)"
    
    next = raw_input("> ")
    
    if next == "left":
        library()
    elif next == "right":
        wash_room()
    else:
        dead("That wasn't an option  You're dead.")

start()
