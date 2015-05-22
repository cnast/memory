# implementation of card game - Memory

# Copy and paste code into Codeskulptor http://www.codeskulptor.org/ to play or click http://www.codeskulptor.org/#user38_ps9tYXCxCAyEvPa.py

# Game play: try to make a matching pair by turning over two cards at a time
# Counter tracks number of tries to match all the cards

import simplegui
import random

# define global variables
combolst = range(0,8) + range(0,8)

# helper function to initialize globals
def new_game():
    global turns, exposed, state, combolst
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns)) #label in frame

    exposed = [False, False, False, False, 
           False, False, False, False, 
           False, False, False, False, 
           False, False, False, False]
    
    random.shuffle(combolst)
     
# define event handlers
def mouseclick(pos):
    global exposed, turns, state
    global first_card_index, second_card_index
    
    # if a card is clicked, expose it
    current = pos[0] // 50
    
    if exposed[current]:
       return
    exposed[current] = True

    # add game state logic here
    if state == 0:
        state = 1
        # save current card index
        first_card_index = current
    elif state == 1:
        second_card_index = current
        state = 2
        # increment counter for turns
        turns += 1
        label.set_text("Turns = " + str(turns)) # updates label in frame
        
    else:
        state = 1
        # test if cards match
        if combolst[first_card_index] != combolst[second_card_index] :
            exposed[first_card_index] = False
            exposed[second_card_index] = False
        first_card_index = current

# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(0, 16):
        # draw 16 rectangles
        canvas.draw_polygon([(i * 50, 0), 
                             (i * 50 + 50, 0), 
                             (i * 50 + 50, 100), 
                             (i * 50, 100)], 1, 'Black', 'Grey')
        # if the card is exposed, draw its value on the card face
        if exposed[i] == True : 
            canvas.draw_text(str(combolst[i]), (i * 50 + 15, 60), 40, 'White')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

