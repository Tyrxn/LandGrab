
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 10485384
#    Student name: Tyran Wong-Tung
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  LAND GRAB
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "process_moves".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various rectangular icons, using data stored in a
#  list to determine which icons to place and where.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *

# Define constant values for setting up the drawing canvas
cell_width = 120 # pixels (default is 120)
cell_height = 90 # pixels (default is 90)
grid_size = 7 # width and height of the grid (default is 7)
x_margin = cell_width * 2.4 # pixels, the size of the margin left/right of the board
y_margin = cell_height // 2.1 # pixels, the size of the margin below/above the board
canvas_height = grid_size * cell_height + y_margin * 2
canvas_width = grid_size * cell_width + x_margin * 2

# Validity checks on grid size
assert cell_width >= 100, 'Cells must be at least 100 pixels wide'
assert cell_height >= 75, 'Cells must be at least 75 pixels high'
assert grid_size >= 5, 'Grid must be at least 5x5'
assert grid_size % 2 == 1, 'Grid size must be odd'
assert cell_width / cell_height >= 4 / 3, 'Cells must be much wider than high'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You may NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(show_instructions = True, # show Part B instructions
                          label_locations = True, # label axes and home coord
                          bg_colour = 'light grey', # background colour
                          line_colour = 'grey'): # line colour for grid
    
    # Set up the drawing canvas with enough space for the grid
    setup(canvas_width, canvas_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coordinate of the grid
    left_edge = -(grid_size * cell_width) // 2 
    bottom_edge = -(grid_size * cell_height) // 2

    # Draw the horizontal grid lines
    setheading(0) # face east
    for line_no in range(0, grid_size + 1):
        penup()
        goto(left_edge, bottom_edge + line_no * cell_height)
        pendown()
        forward(grid_size * cell_width)
        
    # Draw the vertical grid lines
    setheading(90) # face north
    for line_no in range(0, grid_size + 1):
        penup()
        goto(left_edge + line_no * cell_width, bottom_edge)
        pendown()
        forward(grid_size * cell_height)

    # Optionally label the axes and centre point
    if label_locations:

        # Mark the centre of the board (coordinate [0, 0])
        penup()
        home()
        dot(30)
        pencolor(bg_colour)
        dot(20)
        pencolor(line_colour)
        dot(10)

        # Define the font and position for the axis labels
        small_font = ('Arial', (18 * cell_width) // 100, 'normal')
        y_offset = (32 * cell_height) // 100 # pixels

        # Draw each of the labels on the x axis
        penup()
        for x_label in range(0, grid_size):
            goto(left_edge + (x_label * cell_width) + (cell_width // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10 # pixels
        for y_label in range(0, grid_size):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_height) + (cell_height // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

    # Optionally write the instructions
    if show_instructions:
        # Font for the instructions
        big_font = ('Arial', (24 * cell_width) // 100, 'normal')
        # Text to the right of the grid
        penup()
        goto((grid_size * cell_width) // 2+ 25, -cell_height // 3)
        setheading(90)
        forward(100)
        write('First competitor\nto reach home:', align = 'left', font = big_font)
        setheading(270)
        forward(100)

        
        
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    # Ensure any drawing still in progress is displayed
    update()
    tracer(True)
    # Optionally hide the cursor
    if hide_cursor:
        hideturtle()
    # Release the drawing canvas
    done()
    
#
#--------------------------------------------------------------------#

#-----Test Data for Use During Code Development----------------------#
#
# The data sets in this section are provided to help you develop and
# test your code.  You can use them as the argument to the
# "process_moves" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_moves" function appearing below.
# Your program must work correctly for any data set that can be
# generated by calling "random_moves()" with no argument.
#
# Each of the data sets is a list of moves, each specifying which
# competitor is attempting to move and in which direction.  The
# general form of each move is
#
#     [competitor_identity, direction]
#
# where the competitor identities range from 'Competitor A' to
# 'Competitor D' and the directions are 'Up', 'Down', 'Left' and
# 'Right'.
#
# Note that all the data sets below assume the second argument
# to "random_moves" has its default value.
#

# The following data set makes no moves at all and can be used
# when developing the code to draw the competitors in their
# starting positions.
fixed_data_set_00 = [['Competitor A', 'Down'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Down']]

# The following data sets each move one of the competitors
# several times but do not attempt to go outside the margins
# of the grid or overwrite previous moves
fixed_data_set_01 = [['Competitor A', 'Right'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Left'],
                     ['Competitor A', 'Up']]
fixed_data_set_02 = [['Competitor B', 'Left'],
                     ['Competitor B', 'Left'],
                     ['Competitor B', 'Down'],
                     ['Competitor B', 'Down'],
                     ['Competitor B', 'Right'],
                     ['Competitor B', 'Up']]
fixed_data_set_03 = [['Competitor C', 'Up'],
                     ['Competitor C', 'Up'],
                     ['Competitor C', 'Right'],
                     ['Competitor C', 'Right'],
                     ['Competitor C', 'Down'],
                     ['Competitor C', 'Down'],
                     ['Competitor C', 'Left']]
fixed_data_set_04 = [['Competitor D', 'Left'],
                     ['Competitor D', 'Left'],
                     ['Competitor D', 'Left'],
                     ['Competitor D', 'Up'],
                     ['Competitor D', 'Up'],
                     ['Competitor D', 'Up']]

# The following data set moves all four competitors and
# will cause them all to go outside the grid unless such
# moves are prevented by your code
fixed_data_set_05 = [['Competitor A', 'Right'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Right'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Right'],
                     ['Competitor C', 'Right'],
                     ['Competitor C', 'Right'],
                     ['Competitor C', 'Right'],
                     ['Competitor C', 'Up'],
                     ['Competitor C', 'Right'],
                     ['Competitor C', 'Up'],
                     ['Competitor C', 'Up'],
                     ['Competitor C', 'Left']]

# We can also control the random moves by providing a "seed"
# value N to the random number generator by using
# "random_moves(N)" as the argument to function "process_moves".
# You can copy the following function calls into the main
# program to force the program to produce a fixed sequence of
# moves while debugging your code.

# The following seeds all produce moves in which each
# competitor captures a small number of squares in their
# own corner, but do not interfere with one another.
#
#   random_moves(39) - Only one round occurs
#   random_moves(58) - Only two rounds
#   random_moves(12)
#   random_moves(27)
#   random_moves(38)
#   random_moves(41)

# The following seeds all produce moves in which two or
# more competitors overlap one another's territory.
#
#   random_moves(20) - Competitors C and D touch but don't overlap
#   random_moves(23) - Competitors A and B overlap
#   random_moves(15) - Competitors A and D overlap
#   random_moves(29) - Competitors B and D overlap slightly
#   random_moves(18) - Competitors B, C and D overlap
#   random_moves(31) - A and C overlap slightly, B and D touch but don't overlap
#   random_moves(36) - Competitor D overlaps Competitor C
#
# We haven't yet found a seed that causes a player to
# be completely eliminated - can you find one?

# The following seeds all produce very long sequences of
# moves which result in most of the grid being filled.
#
#   random_moves(19)
#   random_moves(75)
#   random_moves(43) - Competitor D reaches opposite corner
#   random_moves(87) - C occupies A's corner and A occupies B's corner
#   random_moves(90) - Only 4 squares left unoccupied
#
# We haven't yet found a seed that causes every cell
# to be occupied - can you find one?

# The following seeds produce data sets which have a special
# meaning in the second part of the assignment. Their
# significance will be explained in the Part B instructions.
#
#   random_moves(21)
#   random_moves(26)
#   random_moves(24)
#   random_moves(35)
#
#   random_moves(52)
#   random_moves(51)
#   random_moves(47)
#   random_moves(46)
#
#   random_moves(53)
#   random_moves(62)
#   random_moves(81)
#   random_moves(48)
#
#   random_moves(54)
#   random_moves(98)

# If you want to create your own test data sets put them here.
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.

# The following function creates a random data set as a list
# of moves.  Your program must work for any data set that
# can be returned by this function.  The results returned by
# calling "random_moves()" will be used as the argument to your
# "process_moves" function during marking.  For convenience during
# code development and marking this function also prints each move
# to the shell window.
#
# NB: As a matter of style your code should not print anything else
# to the shell.  Make sure any debugging calls to the "print"
# function are disabled before you submit your solution.
#
# The function makes no attempt to avoid moves that will go
# outside the grid.  It is your responsibility to detect and
# ignore such moves.
#
def random_moves(the_seed = None, max_rounds = 35):
    # Welcoming message
    print('\nWelcome to Land Grab!')
    print('Here are the randomly-generated moves:')
    # Set up the random number generator
    seed(the_seed)
    # Randomise the order in which competitors move
    competitors = ['Competitor A', 'Competitor B', 'Competitor C', 'Competitor D',]
    shuffle(competitors)
    # Decide how many rounds of moves to make
    num_rounds = randint(0, max_rounds)
    # For each round generate a random move for each competitor
    # and save and print it
    moves = []
    for round_no in range(num_rounds):
        print()
        for competitor in competitors:
            # Create a random move
            move = [competitor, choice(['Left', 'Right', 'Up', 'Down'])]
            # Print it to the shell and remember it
            print(move)
            moves.append(move)
    # Print a final message and return the list of moves
    print('\nThere were', len(competitors) * num_rounds,
          'moves generated in', num_rounds,
          ('round' if num_rounds == 1 else 'rounds'))
    return moves

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "process_moves"

########################################################################

#   Setup


tracer(False) # This is used to speed up the process


#   To place all competitors in their respective starting points
#   the "new" positions for each competitor are defined.
new_A_position = ((-cell_width*(grid_size/(2+(1/3))), (cell_height*(grid_size/(2+(1/3))))))
new_B_position = ((cell_width*(grid_size/(2+(1/3))), (cell_height*(grid_size/(2+(1/3))))))
new_C_position = ((-cell_width*(grid_size/(2+(1/3))), (-cell_height*(grid_size/(2+(1/3))))))
new_D_position = (((cell_width*(grid_size/(2+(1/3))), (-cell_height*(grid_size/(2+(1/3)))))))


#   This variable is used to determine which competitor
#   will reach the middle square first. 
first_middle = False


#   The following code is used to name each competitor and
#   to give the simulation a title.


pu()
#   The position of where the label will go is determined.
goto(new_A_position)
setheading(270)
forward(cell_height/4)
setheading(180)
forward(250)
#   Then the label is written
write('Competitor A \nThe Water Tribe', font =('Arial', 15))

#   This is repeated for each of the four competitors. 
goto(new_B_position)
setheading(270)
forward(cell_height/4)
setheading(0)
forward(100)
write('Competitor B \nThe Earth Kingdom', font =('Arial', 15))

goto(new_C_position)
setheading(270)
forward(cell_height/4)
setheading(180)
forward(250)
write('Competitor C \nThe Air Nomads', font =('Arial', 15))

goto(new_D_position)
setheading(270)
forward(cell_height/4)
setheading(0)
forward(100)
write('Competitor D \nThe Fire Nation', font =('Arial', 15))

#   The title is then labelled
goto(0,0)
setheading(90)
forward(cell_height*4)
setheading(270)
forward(40)
setheading(180)
forward(80)
write('The Four Nations', font =('Arial', 15))

####################################################################

#   Movement

#   Movement is defined below. These functions are defined by what
#   actions the turtle must take after receiving direction.


def move_left():
#   Pen is lifted in the air before moving.
    pu()
#   Turtle is set to the direction of the function (left).
    setheading(180)
#   Turtle moves forward to the next cell.
    forward(cell_width)
#   If the x-co-ordinate is out of the defined grid size
#   then the turtle will move back to the original cell.
    if xcor() < (-cell_width*grid_size/2):
        backward(cell_width)
#   The turtle is set back to the original direction.
    setheading(90)
#   Pen is placed down. 
    pd()

#   This is then repeated for all four directions, with
#   boundaries being set for each movement. 
    
def move_right():
    pu()
    setheading(0)
    forward(cell_width)
    if xcor() > (cell_width*grid_size/2):
        backward(cell_width)
    setheading(90)
    pd()
    
    
def move_down():
    pu()
    setheading(270)
    forward(cell_height)
    if ycor() < (-cell_height*grid_size/2):
        backward(cell_height)
    setheading(90)
    pd()
        

def move_up():
    pu()
    setheading(90)
    forward(cell_height)
    if ycor() > (cell_height*grid_size/2):
        backward(cell_height)
    pd()
    
    
################################################################
    
#   Drawing the competitors.

#   The following functions were defined to shorten the code
#   used to draw each competitor


def colour_background(colour):
#   This function creates a rectangle that covers
#   the entire cell in the colour specified. 
    pu()
    right(270)
    forward(45)
    right(270)
    forward(60)
    pd()
    color(colour)
    fillcolor(colour)
    begin_fill()
    right(180)
    forward(120)
    right(90)
    forward(90)
    right(90)
    forward(120)
    right(90)
    forward(90)
    end_fill()
    pu()
    right(90)
    forward(60)
    right(90)
    forward(45)
    right(180)
    

def draw_first_circle(colour):
#   This function draws a circle in the middle
#   of the cell in the colour specified. 
    right(90)
    forward(45)
    right(270)
    pd()
    color('black')
    fillcolor(colour)
    begin_fill()
    circle(45)
    end_fill()
    pu()


def draw_competitor_A():
#   This function draws one of the four competitors.

#   The turtle heads to the last defined position
#   to begin drawing.
    pu()
    goto(new_A_position)
    setheading(0)
#   The cell is then coloured in using the
#   function created previously. 
    colour_background('navy')
#   A circle is drawn in the middle of this cell.
    draw_first_circle('slate gray')
#   A second circle is drawn within the first circle. 
    color('black')
    fillcolor('midnight blue')
    pd()
    begin_fill()
    circle(32)
    end_fill()
#   A wavy line is then drawn within the second
#   circle. 
    fillcolor('steel blue')
    begin_fill()
    circle(16,180)
    circle(-16,180)
    forward(5)
    right(180)
    circle(16,180)
    circle(-16,180)
    backward(5)
    end_fill()
    pu()
#   The turtle then returns to the original
#   position ready to draw the next move. 
    right(90)
    forward(45)
    right(90)
    backward(10)
    

def draw_competitor_B():
#   This function draws the second of the four competitors

#   Once again, the turtle heads to the last
#   defined position to begin drawing. 
    pu()
    goto(new_B_position)
    setheading(0)
    colour_background('dark goldenrod')
    color('gold')
    draw_first_circle('gold')
#   After colouring the cell and drawing the
#   first circle, this time a second circle
#   is drawn directly inside the first. 
    pu()
    fillcolor('dark green')
    left(90)
    forward(45)
    left(90)
    forward(45)
    left(180)
    forward(10)
    setheading(0)
    pd()
    begin_fill()
    circle(35)
    end_fill()
    pu()
#   After the second circle is drawn,
#   a square is drawn in the middle. 
    color('black')
    fillcolor('dark goldenrod')
    setheading(90)
    forward(33)
    right(90)
    begin_fill()
    forward(8.75)
    pd()
    right(90)
    forward(8.75)
    right(90)
    forward(17.5)
    right(90)
    forward(17.5)
    right(90)
    forward(17.5)
    right(90)
    forward(17.5)
#   The turtle then returns back to the
#   original position. 
    pu()
    end_fill()
    setheading(90)
    forward(11)
    left(90)
    forward(9)
    setheading(90)
    

def draw_competitor_C():
#   This function draws the third of the four competitors

#   Once again, the turtle heads to the last
#   defined position to begin drawing. 
    pu()
    goto(new_C_position)
    setheading(0)
#   The cell is coloured in and a circle is drawn
#   in the middle of the cell. 
    colour_background('cornflower blue')
    draw_first_circle('light slate blue')
    color('black')
    pu()
    forward(cell_height/2)
    left(90)
    forward(45)
    setheading(0)
    fillcolor('royal blue')
    begin_fill()
    pd()
#   A spiral is then drawn inside the existing
#   circle. 
    circle(-30, 180)
    circle(-15, 180)
    circle(-10, 90)
    setheading(90)
    circle(17,180)
    circle(35,90)
    circle(33,90)
    setheading(90)
    circle(40,90)
    end_fill()
    pu()
#   The turtle then heads back to the original
#   position. 
    setheading(180)
    forward(4)
    setheading(270)
    forward(43)
    setheading(90)
    
def draw_competitor_D():
#   This function draws the fourth of the four competitors

#   Once again, the turtle heads to the last
#   defined position to begin drawing. 
    pu()
    goto(new_D_position)
    setheading(0)
#   The cell is coloured in and a circle is
#   drawn in the middle of the cell. 
    colour_background('black')
    draw_first_circle('firebrick')
#   The shape of a flame is then drawn. 
    left(90)
    forward(45)
    right(90)
    forward(40)
    fillcolor('black')
    begin_fill()
    pd()
    setheading(255)
    forward(30)
    circle(10, 90)
    setheading(-215)
    forward(15)
    circle(-10,90)
    forward(10)
    setheading(230)
    forward(20)
    circle(20,80)
    setheading(280)
    circle(30,20)
    circle(25,150)
    setheading(90)
    circle(50,20)
    circle(50,20)
    forward(25)
    end_fill()
    pu()
#   The turtle then heads back to the original
#   position. 
    setheading(270)
    forward(42.5)


def absolute_draw_A():
#   These functions are used to draw the
#   competitors, however, do not use co-ordinates
#   and can be called in all spaces of the grid.

#   Therefore, the following functions are used
#   to draw the first competitor to reach the middle
#   cell.

    global first_middle
    first_middle = True
    pu()
    setheading(0)
    colour_background('navy')
    draw_first_circle('slate gray')
    color('black')
    fillcolor('midnight blue')
    pd()
    begin_fill()
    circle(32)
    end_fill()
    fillcolor('steel blue')
    begin_fill()
    circle(16,180)
    circle(-16,180)
    forward(5)
    right(180)
    circle(16,180)
    circle(-16,180)
    backward(5)
    end_fill()
    pu()
    right(90)
    forward(45)
    right(90)
    backward(10)
    
    
def absolute_draw_B():
#   These functions are used to draw the
#   competitors, however, do not use co-ordinates
#   and can be called in all spaces of the grid.

#   Therefore, the following functions are used
#   to draw the first competitor to reach the middle
#   cell.

    global first_middle
    first_middle = True
    pu()
    setheading(0)
    colour_background('dark goldenrod')
    color('gold')
    draw_first_circle('gold')
    pu()
    fillcolor('dark green')
    left(90)
    forward(45)
    left(90)
    forward(45)
    left(180)
    forward(10)
    setheading(0)
    pd()
    begin_fill()
    circle(35)
    end_fill()
    pu()
    color('black')
    fillcolor('dark goldenrod')
    setheading(90)
    forward(33)
    right(90)
    begin_fill()
    forward(8.75)
    pd()
    right(90)
    forward(8.75)
    right(90)
    forward(17.5)
    right(90)
    forward(17.5)
    right(90)
    forward(17.5)
    right(90)
    forward(17.5)
    pu()
    end_fill()
    setheading(90)
    forward(11)
    left(90)
    forward(9)
    setheading(90)
    
    

def absolute_draw_C():
#   These functions are used to draw the
#   competitors, however, do not use co-ordinates
#   and can be called in all spaces of the grid.

#   Therefore, the following functions are used
#   to draw the first competitor to reach the middle
#   cell.

    global first_middle
    first_middle = True
    pu()
    setheading(0)
    colour_background('cornflower blue')
    draw_first_circle('light slate blue')
    color('black')
    pu()
    forward(cell_height/2)
    left(90)
    forward(45)
    setheading(0)
    fillcolor('royal blue')
    begin_fill()
    pd()
    circle(-30, 180)
    circle(-15, 180)
    circle(-10, 90)
    setheading(90)
    circle(17,180)
    circle(35,90)
    circle(33,90)
    setheading(90)
    circle(40,90)
    end_fill()
    pu()
    setheading(180)
    forward(4)
    setheading(270)
    forward(43)
    setheading(90)
    

def absolute_draw_D():
#   These functions are used to draw the
#   competitors, however, do not use co-ordinates
#   and can be called in all spaces of the grid.

#   Therefore, the following functions are used
#   to draw the first competitor to reach the middle
#   cell.

    global first_middle
    first_middle = True
    pu()
    setheading(0)
    colour_background('black')
    draw_first_circle('firebrick')
    left(90)
    forward(45)
    right(90)
    forward(40)
    fillcolor('black')
    begin_fill()
    pd()
    setheading(255)
    forward(30)
    circle(10, 90)
    setheading(-215)
    forward(15)
    circle(-10,90)
    forward(10)
    setheading(230)
    forward(20)
    circle(20,80)
    setheading(280)
    circle(30,20)
    circle(25,150)
    setheading(90)
    circle(50,20)
    circle(50,20)
    forward(25)
    end_fill()
    pu()
    setheading(270)
    forward(42.5)
    
####################################################
#   Move processing

#   The draw functions are used to draw each competitor
#   in their starting positions. They call upon the
#   positions that were presented previously.

#   The variable presenting their new positions are used
#   to continuously update where the next competitor
#   should be drawn. 

draw_competitor_A()
new_A_position = list((xcor(), ycor())) 
draw_competitor_B()
new_B_position = list((xcor(), ycor()))
draw_competitor_C()
new_C_position = list((xcor(), ycor()))
draw_competitor_D()
new_D_position = list((xcor(), ycor()))

#   The function process moves will be used to interpret
#   the given dataset into movements that can be used.

def process_moves(dataset):
#   The global variables are used to update the positions
#   of each competitor outside of this function.
    global new_A_position
    global new_B_position
    global new_C_position
    global new_D_position
    global first_middle
    
#   A data counter is used to iterate each component
#   that is provided in the data set.

    data_counter = 0

#   A for loop will allow the dataset to be read.
    for move in dataset:
    #   If the first value in the dataset reads Competitor A,
    #   then this if statement will call the draw Competitor A
    #   function. 
        if dataset[data_counter][0] == 'Competitor A':
            #   If the second value in the dataset reads
            #   Right, then the if statement will call upon
            #   the move right function. 
            if dataset[data_counter][1] == ('Right'):
               goto(new_A_position)
               move_right()
               #    After moving into the new position,
               #    this position is recorded and saved
               #    for the next movement.             
               new_A_position = list((xcor(), ycor()))
                     
               
            elif dataset[data_counter][1] == ('Left'):
            #      This is repeated for the left direction. 
                   goto(new_A_position)
                   move_left()
                   new_A_position = list((xcor(), ycor()))
                   
                   
            elif dataset[data_counter][1] == ('Up'):
            #      This is repeated for the up direction. 
                   goto(new_A_position)
                   move_up()
                   new_A_position = list((xcor(), ycor()))
                   
                  
            elif dataset[data_counter][1] == ('Down'):
            #      This is repeated for the down direction. 
                   goto(new_A_position)
                   move_down()
                   new_A_position = list((xcor(), ycor()))
                   
            #   If the new position that this competitor moves into
            #   happens to be within the bounds of the middle cell,
            #   while no other competitor has taken over the middle cell
            #   before this, then the turtle will move outside the grid
            #   and draw this competitor.
            if (new_A_position)[0] < (cell_width/2) and (new_A_position)[0] > (-cell_width/2) and (new_A_position)[1] < (cell_height/2) and (new_A_position)[1] > (-cell_height/2) and first_middle == False:                
                   pu()
                   goto(550, -30)
                   absolute_draw_A()                   

        #   Finally, the competitor is drawn. 
            draw_competitor_A()
            
        if dataset[data_counter][0] == 'Competitor B':
        #   This is repeated for Competitor B
            if dataset[data_counter][1] == ('Right'):
                goto(new_B_position)
                move_right()
                new_B_position = list((xcor(), ycor()))
                
            elif dataset[data_counter][1] == ('Left'):
                goto(new_B_position)
                move_left()
                new_B_position = list((xcor(), ycor()))
                
            elif dataset[data_counter][1] == ('Up'):
                goto(new_B_position)
                move_up()
                new_B_position = list((xcor(), ycor()))
                
            elif dataset[data_counter][1] == ('Down'):
                goto(new_B_position)
                new_B_position = list((xcor(), ycor()))
                
            if (new_B_position)[0] < (cell_width/2) and (new_B_position)[0] > (-cell_width/2) and (new_B_position)[1] < (cell_height/2) and (new_B_position)[1] > (-cell_height/2) and first_middle == False:
                pu()
                goto(550, -30)
                absolute_draw_B()   
                
            draw_competitor_B()
            
        if dataset[data_counter][0] == 'Competitor C':
        #   This is repeated for Competitor C
            if dataset[data_counter][1] == ('Right'):
                goto(new_C_position)
                move_right()
                new_C_position = list((xcor(), ycor()))
                
            elif dataset[data_counter][1] == ('Left'):
                goto(new_C_position)
                move_left()
                new_C_position = list((xcor(), ycor()))
                
            elif dataset[data_counter][1] == ('Up'):
                goto(new_C_position)
                move_up()
                new_C_position = list((xcor(), ycor()))
                
            elif dataset[data_counter][1] == ('Down'):
                goto(new_C_position)
                move_down()
                new_C_position = list((xcor(), ycor()))
                
            if (new_C_position)[0] < (cell_width/2) and (new_C_position)[0] > (-cell_width/2) and (new_C_position)[1] < (cell_height/2) and (new_C_position)[1] > (-cell_height/2) and first_middle == False:
                pu()
                goto(550, -30)
                absolute_draw_C()
            
            draw_competitor_C()
        
        if dataset[data_counter][0] == 'Competitor D':
        #   This is repeated for Competitor D
            if dataset[data_counter][1] == ('Right'):
                goto(new_D_position)
                move_right()
                new_D_position = list((xcor(), ycor()))
                
                
            elif dataset[data_counter][1] == ('Left'):
                goto(new_D_position)
                move_left()
                new_D_position = list((xcor(), ycor()))
                
                
            elif dataset[data_counter][1] == ('Up'):
                goto(new_D_position)
                move_up()
                new_D_position = list((xcor(), ycor()))
                
                
            elif dataset[data_counter][1] == ('Down'):
                goto(new_D_position)
                move_down()
                new_D_position = list((xcor(), ycor()))
                                
            if (new_D_position)[0] < (cell_width/2) and (new_D_position)[0] > (-cell_width/2) and (new_D_position)[1] < (cell_height/2) and (new_D_position)[1] > (-cell_height/2) and first_middle == False:
                pu()
                goto(550, -30)
                absolute_draw_D()
            draw_competitor_D()
    #   The data counter is updated each time this for loop re-iterates
    #   to move on to the next list in the dataset. 
        data_counter = data_counter + 1
    #   The following code presents that after all lists in the dataset
    #   has been iterated, if none have made it to the middle cell,
    #   then display this on the right of the grid. 
    if first_middle == False:
        goto(430, -30)
        write('No competitors reached home', font = ('Arial', 15))
        hideturtle()
      
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution, and calls your solution.  Do not change
# any of this code except as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, choose
# ***** whether or not to label the axes, etc, by providing
# ***** arguments to this function call
create_drawing_canvas()


# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen


# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** theme and its competitors
title('ATLA: Four Nations')



### Call the student's function to process the moves
### ***** While developing your program you can call the
### ***** "random_moves" function with a fixed seed for the random
### ***** number generator, but your final solution must work with
### ***** "random_moves()" as the argument to "process_moves", i.e.,
### ***** for any data set that can be returned by calling
### ***** "random_moves" with no seed.
process_moves(random_moves()) # <-- this will be used for assessment

### Alternative function call to help debug your code
### ***** The following function call can be used instead of
### ***** the one above while debugging your code, but will
### ***** not be used for assessment. Comment out the call
### ***** above and uncomment the one below if you want to
### ***** call your "process_moves" function with one of the
### ***** "fixed" data sets above, so that you know in advance
### ***** what the moves are.
#process_moves(fixed_data_set_05) # <-- not used for assessment

   

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid.
#release_drawing_canvas()

#
#--------------------------------------------------------------------#
