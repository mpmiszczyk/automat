# from tkinter import *
from tkinter import ttk, Tk, N, W, E, S, Canvas, ALL
from CelluralAutoma import cells_from_string, Rule, calculate_next_state


root = Tk( )
root.columnconfigure( 0, weight=1 )
root.rowconfigure( 0, weight=1 )

main_frame = ttk.Frame( root )
main_frame.grid( column=0, row=0, sticky=(N, W, E, S) )

canvas = Canvas( main_frame )
canvas.grid( column=0, row=0, sticky=(N, W, E, S) )

rectangle_color = 'red'

cells = cells_from_string( "____#__#__#______###__##_#" )
rule = Rule( 90 )


def draw (cells, canvas):
   """

   :param cells: instance of :class:'CelluralAutoma.Cells'
   :param canvas: instance of :class:'tkinter.Canvas'
   """
   size = 20
   canvas.delete( ALL )
   for i in range( len( cells ) ):
      if cells[i]:
         start = i * size
         canvas.create_rectangle( ( start, 0, start + size, size),
                                  fill=rectangle_color,
                                  outline=rectangle_color,
                                  activefill='black' )
         #TODO add iner padding


def iterate_cells ():
   global cells
   draw( cells, canvas )
   cells = calculate_next_state( cells, rule )


def task ():
   iterate_cells( )
   if bind_state:
      root.after( 333, task )  # reschedule event in half seconds


bind_state = True


def start_stop (args):
   global bind_state
   if bind_state:
      bind_state = False
   else:
      bind_state = True
      root.after( 5, task )


root.bind( "<space>", start_stop )
root.after( 5, task )
root.mainloop( )
