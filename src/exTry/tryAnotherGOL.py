from tkinter import *
from time import sleep
from Environment import *


class GameOfLife( object ):
   def __init__ (self, master, envDim):
      self.unitSize = 10
      self.dimension = envDim * self.unitSize
      self.environment = Environment( envDim )
      self.environment.seedBoard( )
      self.started = False

      frame = Frame( master )
      frame.pack( )
      Button( frame, text="Go", command=self.go_call ).pack( side=LEFT )
      Button( frame, text="Clear", command=self.reset_call ).pack( side=LEFT )
      Button( frame, text="Close", command=frame.quit ).pack( side=RIGHT )
      canvas = self.drawCanvas( master, self.dimension )


def drawCanvas (self, master, dimension):
   self.canvas = Canvas( master, width=self.dimension, height=self.dimension )
   self.canvas.pack( )
   return self.canvas


def go_call (self):
   print
   "<< Go Call >>"
   if self.environment.started == False:
      self.environment.seedBoard( )

   self.drawState( self.environment )
   self.environment.nextBoard( )
   self.started = True
   while True:
      self.environment.nextBoard( )
      self.canvas.delete( ALL )
      self.drawState( self.environment )
      self.canvas.update_idletasks( )
      sleep( 4 )


def reset_call (self):
   print
   "<< Reset Call >>"
   self.canvas.delete( ALL )
   self.environment = Environment( self.environment.dim )


def drawState (self, environment):
   size = self.unitSize
   for x in range( environment.dim ):
      for y in range( environment.dim ):
         if environment.matrix[x][y].alive == True:
            xs = x * size
            ys = y * size
            self.canvas.create_rectangle( xs, ys, xs + size, ys + size, fill='black' )


envDim = 70
root = Tk( )
gol = GameOfLife( root, envDim )
root.mainloop( )