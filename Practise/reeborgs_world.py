#Challenge Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

#Solution to Hurdle 1 : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for hurdles in range(6):
    jump_hurdle()

-------------------------------------------------------
#2. Solving the reeborg Hurdle 1 using the while loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#for hurdles in range(6):
 #   jump_hurdle()

no_of_hurdles = 6
while no_of_hurdles > 0:
    jump_hurdle()
    no_of_hurdles -= 1

--------------------------------------------------
#3. Solving reeborg Hurdle 2 using the while loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#for hurdles in range(6):
 #   jump_hurdle()

while at_goal() != True:
    jump_hurdle()



-------------------------------------------------------------------
Hurdle 3: each time the flag is placed at random position and using if, while loop, move(), turn_left(), front_is_clear(), wall_in_front(), at_goal(), and their negation.


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() == False:
    if wall_in_front():
        jump()
    else:
        move()
       
--------------------------------------------------------------------------
HUrdle 4: Solution 1

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump():
    if wall_in_front() and wall_on_right():
        turn_left()
    if wall_in_front() and not wall_on_right():
        turn_right()
    if wall_in_front():
        turn_left()
    if wall_on_right():
        move()
    if not wall_on_right():
        turn_right()
    if front_is_clear() and not wall_on_right():
        move()
    if not wall_on_right():
        turn_right()
        move()
    
while at_goal() == False:
    jump()
    
    
-------------------------------------------------------------------------------
Alternative Solution to Hurdle 4:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()    
      
while at_goal() == False:
    if wall_in_front():
        jump()
    else:
        move()

--------------------------------------
Reeborg: Maze Challenge(As per solution given in the video)
def turn_right():
    turn_left()
    turn_left()
    turn_left()
           
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
---------------------------------------
Reeborg: My Solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()
           
while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
    elif not front_is_clear():
        turn_left()
    elif front_is_clear() and right_is_clear():
        turn_right()
