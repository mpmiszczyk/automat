"""
lifecartoon.py, made with help from http://en.wikipedia.org/wiki/Conway's_Game_of_Life
"""
from tkinter import *

from numpy import zeros


window = Tk( )
canvas = Canvas( window, width=800, height=800 )
canvas.pack( )


def aliveneighbourcounter (y, x):      # counts the number of alive neighbours (wraps around canvas edges)
   ancounter = 0
   if y == 0:
      yminus1 = len( grid ) - 1
   else:
      yminus1 = y - 1
   if y == len( grid ) - 1:
      yplus1 = 0
   else:
      yplus1 = y + 1
   if x == 0:
      xminus1 = len( grid ) - 1
   else:
      xminus1 = x - 1
   if x == len( grid ) - 1:
      xplus1 = 0
   else:
      xplus1 = x + 1
   if grid[yminus1][xminus1] == 1: ancounter += 1
   if grid[y][xminus1] == 1: ancounter += 1
   if grid[yminus1][x] == 1: ancounter += 1
   if grid[y][xplus1] == 1: ancounter += 1
   if grid[yplus1][x] == 1: ancounter += 1
   if grid[yplus1][xplus1] == 1: ancounter += 1
   if grid[yplus1][xminus1] == 1: ancounter += 1
   if grid[yminus1][xplus1] == 1: ancounter += 1
   return ancounter


def kill (grid):            # kills if the number of alive neighbours is other than 2 or 3
   gridkilled = zeros( [40, 40] )
   for y in range( len( grid ) ):
      for x in range( len( grid ) ):
         gridkilled[y][x] = grid[y][x]
         if grid[y][x] == 1:
            ancounter = aliveneighbourcounter( y, x )
            if ancounter < 2 or ancounter > 3:
               gridkilled[y][x] = 0
   return gridkilled


def cometolife (grid):         # brings to life if there are exactly 3 alive neighbours
   gridcametolife = zeros( [40, 40] )
   for y in range( len( grid ) ):
      for x in range( len( grid ) ):
         if grid[y][x] == 0:
            ancounter = aliveneighbourcounter( y, x )
            if ancounter == 3:
               gridcametolife[y][x] = 1
   return gridcametolife


def drawbox ():            # draws a blue box for 'alive', a green box for 'dead'
   for y in range( len( grid ) ):
      for x in range( len( grid ) ):
         if grid[y][x] == 1:
            canvas.create_rectangle( 20 * x, 20 * y, 20 * x + 20, 20 * y + 20, fill="#220C65", outline="#DFF2A6",
                                     width=1 )
         elif grid[y][x] == 0:
            canvas.create_rectangle( 20 * x, 20 * y, 20 * x + 20, 20 * y + 20, fill="#A4AD90", outline="#DFF2A6",
                                     width=1 )


# set up the initial state of the system (0 means 'dead', 1 means 'alive'):
grid = zeros( [40, 40] )
grid[35][37] = grid[35][38] = grid[35][39] = 1                  # blinker
grid[7][3] = grid[7][4] = grid[7][5] = grid[8][4] = grid[8][5] = grid[8][6] = 1      #toad
grid[20][20] = grid[21][20] = grid[22][20] = grid[22][21] = grid[21][22] = 1      # glider
# grid[30][30] = grid[31][30] = grid[32][30] = grid[33][30] = grid[30][31] = grid[30][32] = grid[31][33] = grid[34][31] = grid[34][33] = 1 #lwss

# animation loop:
while 1 == 1:
   gridkilled = kill( grid )
   gridcametolife = cometolife( grid )
   for y in range( len( grid ) ):
      for x in range( len( grid ) ):
         if gridkilled[y][x] == gridcametolife[y][x] == 1:
            grid[y][x] = 1
         else:
            grid[y][x] = gridkilled[y][x] + gridcametolife[y][x]
   drawbox( )
   canvas.after( 30 )
   canvas.update( )

window.mainloop( ) # not really needed for animation; but it keeps errors schowing up when stoppin app