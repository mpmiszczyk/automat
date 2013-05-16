from tkinter import *
from tkinter import ttk
from CelluralAutoma import cells_from_string


root = Tk( )
root.columnconfigure( 0, weight=1 )
root.rowconfigure( 0, weight=1 )

main_frame = ttk.Frame( root )
main_frame.grid( column=0, row=0, sticky=(N, W, E, S) )

canvas = Canvas( main_frame )
canvas.grid( column=0, row=0, sticky=(N, W, E, S) )

rectangle_color = 'red'

cells = cells_from_string( "____#__#__#______###__##_#" )


def draw (cells, canvas):
   """

   :param cells: instance of :class:'CelluralAutoma.Cells'
   :param canvas: instance of :class:'tkinter.Canvas'
   """
   size = 20
   for i in range( len( cells ) ):
      if cells[i]:
         start = i * size
         canvas.create_rectangle( ( start, 0, start + size, size),
                                  fill=rectangle_color,
                                  outline=rectangle_color )
         #TODO add iner padding


draw( cells, canvas )


def task ():
   print( "automata" )
   root.after( 500, task )  # reschedule event in half seconds


root.after( 2000, task )
root.mainloop( )