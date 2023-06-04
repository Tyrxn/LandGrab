# LandGrab

## Overview

LandGrab is a Python-based project that makes use of the `turtle` module to generate a graphical simulation of a game. The simulation features four "competitors" (A, B, C, and D) who aim to reach the center of a grid first. These competitors are moved through a sequence of commands such as 'Up', 'Down', 'Left', 'Right' and their positions are represented on the grid.

## How to Run

To run the LandGrab project:

1. Ensure Python is installed on your machine.
2. Download and install the `turtle` module if it isn't already.
3. Download the LandGrab Python script.
4. Open a terminal/command prompt.
5. Navigate to the directory where the script is located using `cd /path/to/script`.
6. Run the script by typing `python LandGrab.py`.

## Project Structure

This project consists of functions to set up the game, define the grid's properties, draw the grid, move the competitors, and create random moves.

Key functions include:

- `create_drawing_canvas()`: sets up the canvas and draws the background for the overall image.
- `release_drawing_canvas()`: ends the program and releases the drawing canvas to the operating system.
- `random_moves()`: generates random movements for each of the four competitors.
- `move_left()`, `move_right()`, `move_up()`, `move_down()`: These functions are responsible for moving a competitor in a specific direction.

## Notes

- If the competitors move outside the grid, they are returned to their original position within the grid.
- The first competitor to reach the middle of the grid (coordinate [0, 0]) is declared the winner.
