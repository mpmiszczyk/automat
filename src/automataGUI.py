from tkinter import *
from tkinter import ttk


root = Tk( )
root.columnconfigure( 0, weight=1 )
root.rowconfigure( 0, weight=1 )

main_frame = ttk.Frame( root )
main_frame.grid( column=0, row=0, sticky=(N, W, E, S) )

canvas = Canvas( main_frame )
canvas.grid( column=0, row=0, sticky=(N, W, E, S) )

rectangle_color = 'red'
canvas.create_rectangle( (1, 1, 40, 40), fill=rectangle_color, outline=rectangle_color )


def task ():
   print( "automata" )
   root.after( 500, task )  # reschedule event in half seconds


root.after( 2000, task )
root.mainloop( )