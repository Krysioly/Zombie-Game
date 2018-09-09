"""
A Choose your Adventure Game
ZOMBIES
Here you will make decisions that will affect whether you will live in this post apocalyptic world or become a walking dead
"""
### Drawings ###

import turtle
#   title
def zombie():
    """Draws the word ZOMBIE"""
    turtle.speed(10)
    # z
    turtle.pencolor("green")
    turtle.pensize(15)
    turtle.penup()
    turtle.goto(-275, 100)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(155)
    turtle.left(135)
    turtle.forward(100)
    # O
    turtle.pencolor("grey")
    turtle.pensize(15)
    turtle.penup()
    turtle.goto(-110, -25)
    turtle.pendown()
    turtle.circle(50)
    # M
    turtle.pencolor("green")
    turtle.pensize(15)
    turtle.penup()
    turtle.goto(-35, -15)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(100)
    # B
    turtle.pencolor("green")
    turtle.pensize(15)
    turtle.penup()
    turtle.goto(70, -35)
    turtle.pendown()
    turtle.backward(130)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(75)
    turtle.forward(70)
    turtle.left(155)
    turtle.forward(70)
    turtle.right(75)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(35)
    turtle.forward(25)
    # I
    turtle.pencolor("brown")
    turtle.pensize(15)
    turtle.penup()
    turtle.goto(170, -25)
    turtle.pendown()
    turtle.right(60)
    turtle.forward(75)
    turtle.penup()
    turtle.goto(170, 80)
    turtle.pendown()
    turtle.forward(5)
    # E
    turtle.pencolor("green")
    turtle.pensize(15)
    turtle.penup()
    turtle.goto( 200, -30)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(75)
    turtle.backward(75)
    turtle.left(90)
    turtle.forward(130)
    turtle.right(90)
    turtle.forward(75)
    turtle.backward(75)
    turtle.right(90)
    turtle.forward(65)
    turtle.left(90)
    turtle.forward(50)
#   shoes
def shoe_curve():
    """Curves around the outside of the shoes"""
    turtle.forward(50)
    turtle.left(30)
    turtle.forward(50)
    turtle.left(30)
    turtle.forward(50)
    turtle.left(30)
def shoe_outline():
    """Outline of the shoes/ both tennis and flip flop"""
    shoe_curve()
    turtle.forward(200)
    shoe_curve()
    shoe_curve()
    turtle.forward(200)
    shoe_curve()
def small_curve():
    """The inside curve for the foot hole"""
    turtle.forward(30)
    turtle.right(30)
    turtle.forward(30)
    turtle.right(30)
    turtle.forward(30)
    turtle.right(30)
def lace_ties():
    """The loops for the tie on the laces"""
    turtle.forward(55)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(60)
def strap_location():
    """Where the strap starts"""
    turtle.penup()
    turtle.goto(110, 90)
    turtle.pendown()
def shoe_tennis():
    """Tennis shoe with the foot hole, laces and tie laces"""
    turtle.speed(10)
    turtle.pensize(10)
    turtle.color("blue")
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()
    shoe_outline()
    #inside shoe
    turtle.penup()
    turtle.goto(-235, -80)
    turtle.pendown()
    turtle.forward(115)
    turtle.right(90)
    small_curve()
    small_curve()
    turtle.forward(30)
    #laces
    turtle.color("green")
    turtle.penup()
    turtle.goto(-235, 0)
    turtle.pendown()
    turtle.right(85)
    turtle.forward(115)
    turtle.left(160)
    turtle.forward(115)
    turtle.right(160)
    turtle.forward(115)
    turtle.left(160)
    turtle.forward(115)
    turtle.right(169)
    turtle.forward(115)
    turtle.right(169)
    turtle.forward(115)
    turtle.left(160)
    turtle.forward(115)
    turtle.right(160)
    turtle.forward(115)
    turtle.left(160)
    turtle.forward(115)
    #lace_ties
    turtle.penup()
    turtle.goto(-175, -45)
    turtle.pendown()
    lace_ties()
    turtle.right(30)
    lace_ties()
def shoe_flipflop():
    """Flip flow with toe straps"""
    turtle.speed(10)
    turtle.pensize(10)
    turtle.color("red")
    turtle.penup()
    turtle.goto(70, -200)
    turtle.pendown()
    turtle.right(17)
    shoe_outline()
    #strap
    turtle.pensize(20)
    strap_location()
    turtle.right(45)
    turtle.forward(115)
    strap_location()
    turtle.right(105)
    turtle.forward(115)
    strap_location()
    turtle.right(100)
    turtle.forward(15)
#   barn and ax
def barn_ax():
    """A barn with an ax laying against it"""
    turtle.speed(10)
    turtle.pensize(10)
    turtle.color("red")
    turtle.penup()
    turtle.goto(-150, -150)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(200)
    turtle.right(35)
    turtle.forward(100)
    turtle.right(35)
    turtle.forward(100)
    turtle.right(40)
    turtle.forward(100)
    turtle.right(35)
    turtle.forward(100)
    turtle.right(35)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(300)
    #barn door
    turtle.right(180)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(150)
    #cross beams
    turtle.pensize(7)
    turtle.right(155)
    turtle.forward(167)
    turtle.right(117)
    turtle.forward(70)
    turtle.right(115)
    turtle.forward(167)
    turtle.left(117)
    turtle.forward(75)
    turtle.left(64)
    turtle.forward(167)
    turtle.left(115)
    turtle.forward(75)
    turtle.left(118)
    turtle.forward(167)
    #window
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.right(26)
    turtle.forward(55)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(55)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(55)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(27.5)
    turtle.right(90)
    turtle.forward(100)
    #ax
    turtle.pensize(10)
    turtle.color("brown")
    turtle.penup()
    turtle.goto(125, -152)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(75)
    turtle.pensize(20)
    turtle.color("grey")
    turtle.right(90)
    turtle.forward(10)
#  police station
def jailman():
    """A jail cell with a man inside"""
    turtle.speed(10)
    #man
    turtle.pensize(10)
    turtle.color("black")
    turtle.penup()
    turtle.goto(-20, -10)
    turtle.pendown()
    #head
    m=0
    angle=360/8
    while m<9:
        turtle.forward(15)
        turtle.left(angle)
        m=m+1
    #body
    turtle.left(180)
    turtle.forward(7)
    turtle.left(47)
    turtle.forward(90)
    #legs
    turtle.left(45)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    #body
    turtle.left(45)
    turtle.forward(35)
    #arms
    turtle.right(50)
    turtle.forward(40)
    turtle.right(180)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    #jail
    turtle.pensize(10)
    turtle.color("grey")
    turtle.penup()
    turtle.goto(-150,-150)
    turtle.pendown()
    turtle.right(132.5)
    i=0
    while i<4:
        turtle.forward(275)
        turtle.left(90)
        i=i+1
    b=0
    while b<2:
        turtle.forward(55)
        turtle.left(90)
        turtle.forward(275)
        turtle.right(90)
        turtle.forward(55)
        turtle.right(90)
        turtle.forward(275)
        turtle.left(90)
        b=b+1
#  city 
def window(x,y):
    """Small filled in yellow squares"""
    turtle.pencolor("yellow")
    turtle.pensize(5)
    turtle.fillcolor("yellow")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    i=0
    while i<4:
        turtle.forward(30)
        turtle.left(90)
        i=i+1
    turtle.end_fill()
def city_skyline():
    """City buildings with windows on them"""
    turtle.speed(10)
    turtle.pensize(5)
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-250, -150)
    turtle.pendown()
    #first building
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)  
    turtle.forward(100)
    #second building
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)    
    turtle.forward(150) 
    turtle.right(90)   
    turtle.forward(225) 
    #third building
    turtle.left(90)
    turtle.forward(75)
    #fourth building 
    turtle.left(90)
    turtle.forward(150) 
    turtle.right(90)   
    turtle.forward(100) 
    turtle.right(90)    
    turtle.forward(100) 
    #fifth building
    turtle.left(90)     
    turtle.forward(100) 
    turtle.right(90)   
    turtle.forward(175) 
    #end building 
    turtle.right(90)
    turtle.forward(525) 
    turtle.right(90)
    turtle.forward(75) 
    turtle.end_fill()
    #windows
    window(-180, -110)
    window(-180, -170)
    #building2 row1
    window(-100, -170)
    window(-100, -105)
    window(-100, -45)
    window(-100, 15)
    window(-100, 75)
    #building2 row2
    window(-20, 75)
    window(-20, 15)
    window(-20, -45)
    window(-20, -105)
    window(-20, -170)
    #building3
    window(55, -145)  
    #building4
    window(145, -170) 
    window(145, -105)
    window(145, -45)
    window(145, 15) 
    #buidling5
    window(235, -180)
    window(235, -125)
    window(235, -70)
def survivors():
    turtle.speed(10)
    turtle.pensize(5)
    turtle.pencolor("black")
    #hall floor
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.right(140)
    turtle.forward(350)
    turtle.left(140)
    turtle.forward(650)
    turtle.left(130)
    turtle.forward(295)
    turtle.left(50)
    turtle.forward(195)
    turtle.end_fill()
    #hall wall
    turtle.fillcolor("grey")
    turtle.begin_fill()
    turtle.left(40)
    turtle.forward(350)
    turtle.right(130)
    turtle.forward(350)
    turtle.right(50)
    turtle.forward(349)
    turtle.right(130)
    turtle.forward(350)
    turtle.end_fill()
    #doorway
    turtle.fillcolor("tan")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(195)
    turtle.left(90)
    turtle.forward(350)
    turtle.left(90)
    turtle.forward(195)
    turtle.end_fill()
    #hall wall
    turtle.backward(195)
    turtle.fillcolor("grey")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(350)
    turtle.left(40)
    turtle.forward(298)
    turtle.left(140)
    turtle.forward(400)
    turtle.left(47)
    turtle.forward(270)
    turtle.end_fill()
    #door
    turtle.penup()
    turtle.goto(-10, 0)
    turtle.pendown()
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.right(47)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.end_fill()
    #spray paint
    turtle.penup()
    turtle.goto(-300, 20)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.write("survivors here", font=("comic sans", 25, "italic"))
    #eye slot
    turtle.penup()
    turtle.goto(25, 150)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.forward(11)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(11)
    turtle.left(90)
    turtle.forward(30)
    turtle.end_fill()
    #door knob
    turtle.penup()
    turtle.goto(70, 80)
    turtle.pendown()
    turtle.pencolor("silver")
    turtle.pensize(10)
    turtle.forward(1)

### Story & Inputs ###

def ask_shoes():
    """The first desicion that will come into effect later when heading to city."""
    #ask shoes put on
    print(" ")
    print("You wake up after a restless night of sleep. You really have to stop watching horror movies right before bed. You mindlessly stumble to the kitchen to start the coffee pot then back to your room to get ready.")
    print("You feel like you had the strangest dream but you can't quite recall it. You're dressed now but you need to put on shoes still.")
    turtle.reset()
    shoe_tennis()
    shoe_flipflop()
    print("*/*\*")
    print("Will you put on [t]ennis shoes or [f]lip flops?")
    #make shoes variable
    shoes = input("[t] / [f]: ")
    #make sure input is valid
    while shoes!= "t" and shoes!= "f":
        print("That's not a choice, try again...")
        shoes= input("[t]ennis shoes / [f]lip flops: ")
        print(" ")
    print(" ")
    print("Great choice! Now let's get going!")
    #return shoes
    return shoes
def working():
    """Ask to keep working and if you do you die"""
    #get to work and start to notice something is weird 
    print("You get to work and realize there is no one there...")
    print("Now that you think about it, there wasn't anyone out on your way to work. Where is everyone?")
    #choose to check it out or not 
    print("Do you get to [w]ork so your boss doesn't get mad or [l]ook around to find someone?")  
    #make at_work variable
    at_work = input("[w] / [l]: ")
    print(" ")
    while at_work!="w" and at_work!="l":
        print("That's not a choice, try again...")
        at_work = input("[w]ork / [l]ook: ")
        print(" ")
    #if get back to work you die, GAME OVER
    if at_work == "w":
        print("I wouldn't want to upset my boss either. You get started on your work but don't realize that there is a ZOMBIE hiding in your cubicle! It's too late you are attacked, I guess you aren't ready for a zombie apocalypse. Try again when you feel ready!")
        turtle.reset()
        turtle.write("*GAME OVER*", align="left", font=("Arial", 70, "bold"))
        print("*/*\*")
        print(" ")
        print("*GAME OVER*")
        print(" ")
    #if you check it out you realize your all alone
    if at_work == "l":
            print("You decide this is just to weird and go to check out where everyone has gone to. You come across the break room and hear the tv is on.") 
            #check out the news and find out whats going on, zombies
            print("You stop to watch tv and realize that it is tuned to the news and they are saying that there is a zombie virus outbreak! You thought that was just stories for books and movies but it's true!")  
    return at_work
def panic():
    """A question to help slow down the text, will loop until ready to keep going"""
    #ask if player is ready to keep going
    print("Don't panic, you have watched enough movies to know what you need to do.")
    move_on = input("Are you ready to survive? [y]es or [n]o ")
    print(" ")
    #make sure input is valid
    while move_on == "n":
        move_on= input("Well we can't just let the zombies eat us, ready to get going? [y]es or [n]o ")
        print(" ")
def farmhouse_ax():
    """Get ax then into house get supplies will come into effect later"""
    #head outside, everything locked
    print("You are going to need to find a way to protect yourself. You leave work and walk down the street but you quickly realize that all the stores are locked up tight!")
    print(" ")
    #go to barn
    print("You remember that in the woods just outside of town, there was an old barn you use to play in. You can even picture the ax sitting next to the barn door.")
    #get the ax
    print("You head off for the woods, following what's left of the trail out to the old barn. You find the ax exactly where you imagined it. Now you have a weapon but what to do next.")
    print(" ")
    #go into the farm house or back to town?
    print("You now have a weapon but you realize you might need some extra supplies. You head towards the old farm house to check it out. You manage to pry the door open, you are welcomed in by a big puff of dust and cobwebs. Your eyes adjust to the dark and you head in. You move from room to room searching for anything that might be useful. You find a first aid kit in the bathroom and some cans of food in the kitchen. You throw them all in a duffel bag you found in the house.")
def staircase():
    """Decide to leave or go upstairs, if upstairs then die"""
    print("You start to head back to the door but see the staircase to upstairs, do you check for more?")
    #if head to town, leave
    print("Go [u]pstairs or [l]eave?")
    #choose upstairs or leave 
    upstairs= input("[u] / [l]")
    print(" ")
    #make sure input is valid
    while upstairs!="u" and upstairs!="l":
        print("That's not a choice, try again...")
        upstairs = input("[u]pstairs / [l]eave: ")
        print(" ")
    #if you go upstairs you encounter a zombie and lose- GAME OVER
    if upstairs== "u":
        print("You slowly test the stairs to make sure they can still hold your weight. They creak but don't break so you make your way upstairs. You check the first couple rooms and they don't have anything that looks helpful.")
        print("You head down the hall and check out another room but as soon as you open the door you see a zombie standing in the middle of the room, staring at the wall. He turns at the sound of the door and before you get the chance to register what's going on he's on top of you. You try and swing your ax but it's to late. Maybe you'll have better luck next time.")
        turtle.reset()
        turtle.write("*GAME OVER*", align="left", font=("Arial", 70, "bold"))
        print("*/*\*")
        print(" ")
        print("*GAME OVER*")   
    if upstairs == "l":
        print("You have found a lot of great stuff. You leave and head back to town.")  
    return upstairs
def police_station():
    """If you let out the prisoner then get guns, it will effect later if you live"""
    #enter police station, see drunk in cell
    print("You've made your way back to town and head for the police station. Inside you don't see any one, no receptionist or cops. However when you look into the cell in the corner you see the local town drunk, sleeping on the bunk.")
    #wake up drunk, he wants out, do you let him?
    print("You wake up town drunk, he said the police officer left this morning and never came back. He wants to know what's going on.")
    print("You tell him that the news says there's a zombie outbreak. The town drunk wants to be let out, and mentions the keys are sitting on the cops desk.")
    #drawing
    turtle.reset()
    jailman()
    print("*/*\*")
    print("Do you let him [o]ut or leave him [i]n?")
    #make drunk variable
    drunk = input("[o] /[i]: ")
    print(" ")
    #make sure input is valid
    while drunk!="o" and drunk!="i":
        print("That's not a choice, try again...")
        drunk = input("[o]ut / [i]n: ")
        print(" ")
    #if you let him out he shows you the guns and he takes some for himself and runs off.
    if drunk == "o":
        print("You let him out and he immediately goes to the desk and pulls out a key and heads to a cabinet. When he opens it you see all the guns stored inside.")
        print('He takes some for himself and yells "Good luck!" as he runs out the door. You grab some guns for yourself and head out of the station.')
    #if you leave him, leave the police office and head back outside
    if drunk == "i":
        print("You don't trust him so you leave him there and head out of the station.")
    print(" ")
    return drunk
def littlegirl():
    """Help girl decision will effect later"""
    #you head to town and find little girl who needs help
    print("You are walking through the woods on your way to the city and find a young girl crying against a tree. You slowly approach her making sure she isn't already a zombie. You notice she has a huge gash on her leg.")
    #do you help her
    print("Do you [h]elp her or [k]eep moving on?")
    #make helping_girl variable
    helping_girl= input("[h] / [k]: ")
    print(" ")
    #make sure input is valid
    while helping_girl!="h" and helping_girl!="k":
        print("That's not a choice, try again...")
        helping_girl = input("[h]elp her / [k]eep moving: ")
        print(" ")
    if helping_girl == "h":
        print("You couldn't possibly leave this helpless little girl. Thankfully you have found a first aid kit back in the farm house. So you bandage her as best you can and get moving again.")
    #if you leave her then move on
    if helping_girl == "k":
        print("You feel bad but you can't do anything to help the little girl. You know she will just weigh you down so you keep moving north to the city.")
    print(" ")
    #return helping_girl
    return helping_girl
def long_road(shoes):
    """Shoes decide whether you live or die"""
    #head to city
    print("You realize you must leave town and find out how far this outbreak has gone. You decide you must go to the city that is 20 miles north of your town.")
    print(" ")
    #if you wore tennis shoes you make it
    if shoes == "t":
        print("You keep on your journey to the big city. You are so happy you chose to wear tennis shoes today. It's a long walk but you think to yourself, you've been needing the exercise.")
        print(" ")
    #if you wore flip flops, you get swarmed and die- GAME OVER
    if shoes == "f":
        print("You keep on your journey to the big city. It's a long walk and you really wish you didn't wear flip flops today.")
        print("You keep walking but you start to hear some noises all around you. Suddenly you see the first zombie, you get scared and try to run but trip in your flip flops.")
        print("You try to get up but the zombie is already on you. More zombies keep coming and you can't fight them all. To bad you had gotten so far, better luck next time.")
        turtle.reset()
        turtle.write("*GAME OVER*", align="left", font=("Arial", 70, "bold"))
        print("*/*\*")
        print(" ")
        print("*GAME OVER*")
def city():
    """Decisions dont effect later, just to slow the text"""
    #in the city
    print("You look around the city and it's clear that the city has been infected. There's a strange stillness and silence to the city. It's an eerie feeling that makes you more vulnerable than before.")
    turtle.reset()
    city_skyline()
    print("*/*\*")
    #decide to search or hide
    print("Do you start [s]earching or find a place to [h]ide?")
    search = input("[s] / [h]: ")
    print(" ")
    #make sure input is valid
    while search!= "s" and search!= "h":
        print("That's not a choice, try again...")
        search = input("[s]earch / [h]ide: ")
        print(" ")
    #if search then find nothing
    if search== "s":
        print("You look around the ruined city, there's got to be something useful around. You find a few items but nothing special.")
    #if hide then find nowhere
    if search== "h":
        print("You look for a place to hide but everywhere feels to open. You keep your eyes peeled for a good spot.")
def car_alarm(drunk):
    """If you let out prisoner then its effected here"""
    #bump a car and set off an alarm 
    print("As you weave through abandoned cars and accidently bump into one. It sets the alarm off and the sound echos through the streets.") 
    print(" ") 
    #if you picked up a gun, fight and find hideout
    if drunk== "o":
        print("Zombies start pouring out of the shadows. Thankfully you have guns and are able to pick them off one by one. During the shoot out you noticed that there was a message spray painted on the side of a building. Upon closer inspection you see it reads 'SURVIVORS HERE' and you are so relieved!")
        print(" ")
    #if you only have an ax your overwhelmed- GAME OVER
    if drunk== "i":
        print("Zombies start pouring out of the shadows. You swing your ax and start taking out some zombies. Though it doesn't take long for them to swarm around you and you just can't swing anymore. Better luck next time!")
        turtle.reset()
        turtle.write("*GAME OVER*", align="left", font=("Arial", 70, "bold"))
        print("*/*\*")
        print(" ")
        print("*GAME OVER*")
def get_to_hideout():
    """Decisions dont matter, just to slow down text"""
    #you find the survivor hideout
    print("As you approach the building you see the wood planks nailed the door. Try as you might you can't pull them off. You move to the side of the building and find a boarded window with enough of a hole you can squeeze in. Inside you see spray paint again.")
    print("'SURVIVORS TOP FLOOR' you see in the corner an [e]levator and a door to the [s]taircase, which to take?")
    get_in = input("[e] / [s]: ")
    print(" ")
    #make sure input is valid
    while get_in!= "e" and get_in!= "s":
        print("That's not a choice, try again...")
        search = input("[e]levator / [s]tairs: ")
        print(" ")
    #if elevator then get a funny situation
    if get_in== "e":
        print("You press the elevator button and wait for the doors to open. When it finally arrives you get inside and wait for the doors to close. Over the speakers you hear a jazzy, instrumental version of the song 'Staying Alive' you chuckle as the door dings and opens.")
        print(" ")
    #if stairs then boring walk up
    if get_in== "s":
        print("You don't want to risk the elevator, what if it's broken. You open the stairwell door and enter. The sound of the door closing echoes loud, and after that the only noise you hear is your footsteps as you slowly climb flight after flight up the stairs.")
        print(" ")
def inside_hideout(helping_girl):
    """If you helped the girl move on, if you didnt then die"""
    #you have made it to the survivor hideout 
    turtle.reset()
    survivors()
    print("*/*\*")
    #if you have the girl, they are worried she is infected
    print("You make it to the top floor. You find a barricaded hallway with a rigged doorbell at the end. When you press it a small metal panel moves to show a set of eyes.")
    print(" ")
    #if you picked up first aid, they will let you in
    if helping_girl== "h":
        print("The eyes look at you and the little girl, they scan over the bandage on her leg and then narrow in on you. After what feels like forever, the panel shuts and you see what looks like the whole wall start to move.")
        print(" ")
    #if you didnt give her first aid, they wont let you in and you die in the streets with little girl- GAME OVER
    if helping_girl== "k":
        print('The eyes stare at you. After what feels like forever, a sound emits from behind the door, "You must leave! You will infect us all! I can not let you in!" Suddenly the panel shuts and all is silent again.')
        print(" ")
        print("Stunned and disappointed, you head out and walk for miles but never find another sign of life beyond the walking dead. You round a corner and run into a big group zombies, you try to fight them off but there are just to many. Better luck next time.")
        turtle.reset()
        turtle.write("*GAME OVER*", align="left", font=("Arial", 70, "bold"))
        print("*/*\*")
        print(" ")
        print("*GAME OVER*")
def the_end(name):
    """Slow the text and give the end of game message"""
    #your in the hideout
    print("You think to yourself, this might be a trap. Do you risk going in?")
    risk= input("[y]es / [n]o: ")
    print(" ")
    #make sure input is valid
    while risk!= "y" and risk!= "n":
        print("That's not a choice, try again...")
        risk = input("[y]es / [n]o: ")
        print(" ")
    if risk == "n":
        print("Well you almost die a few times today, anyone who isn't a zombie is worth taking a risk on.")
    print("You are impressed that they have made such an impressive hideout. They are fully stocked and you finally feel like you can relax.")
    #girl is safe
    print("The little girl is taken to the infirmary and you are reassured that she has the help she needs")
    #your safe you can relax, congrats
    print("You finally feel safe and you know that you can survive with these others. Congrats {}!".format(name))
    turtle.reset()
    turtle.write("*YOU WIN*", align="left", font=("Arial", 70, "bold"))
    #you win
    print("*YOU WIN*")

### The Game Function ###

def play_game():
    """Start the game and loop with a continue question"""
    #welcome to "ZOMBIES"
    #start introductions and how to input answers
    print("Welcome to ZOMBIES, a choose your own adventure game!")
    print("You will be given a series of choices but beware some choices can end badly!")
    #explain how to answer questions
    print("To answer questions just type the first letter (lowercase) of the word of your choice :]")
    print("If you see */*\* then there is a drawing to check out")
    print(" ")
    zombie()
    print("*/*\*")
    #ask name
    name= input("To start let's pick your name: ")
    name= name.title()
    print("Hello {}!".format(name))
    print(" ")
    continue_game = True
    #make loop for if want to continue
    while continue_game == True:
        shoes = ask_shoes() 
        at_work= working()
        #if at_work==w GAMEOVER
        if at_work== "l":
            panic()
            farmhouse_ax()
            turtle.reset()
            barn_ax()
            print("*/*\*")
            upstairs = staircase()
            # if upstairs==u GAMEOVER
            if upstairs== "l":
                drunk= police_station()
                helping_girl= littlegirl()
                long_road(shoes)
                #if shoes==f GAMEOVER
                if shoes == "t":
                    city()
                    car_alarm(drunk)
                    #if drunk==i GAMEOVER
                    if drunk== "o":
                        get_to_hideout()
                        inside_hideout(helping_girl)    # if helpgirl==k GAMEOVER
                        if helping_girl== "h":
                            the_end(name)
        #ask if you want to continue
        print(" ")
        print("Would you like to play again?")
        continue_game= input("[y]es or [n]o")
        print(" ")
        #if continue then true makes it loop
        if continue_game == "y":
            continue_game = True
        #if not continue then false breaks the loop
        if continue_game == "n":
            continue_game = False

play_game()
