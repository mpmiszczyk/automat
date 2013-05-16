from tkinter import *


root = Tk( )


def task ():
   print( "automata" )
   root.after( 500, task )  # reschedule event in half seconds


root.after( 2000, task )
root.mainloop( )