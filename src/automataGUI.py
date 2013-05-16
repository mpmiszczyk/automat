# from tkinter import *
from tkinter import ttk, Tk, N, W, E, S, Canvas, ALL
from CellularAutoma import cells_from_string, Rule, Automata


root = Tk( )
root.columnconfigure( 0, weight=1 )
root.rowconfigure( 0, weight=1 )

main_frame = ttk.Frame( root )
main_frame.grid( column=0, row=0, sticky=(N, W, E, S) )

canvas = Canvas( main_frame )
canvas.grid( column=0, row=0, sticky=(N, W, E, S) )

rectangle_color = 'red'

# TODO random initialize
automata = Automata( cells_from_string( "____#__#__#______###__##_#" ),
                     Rule( 90 ) )


def draw (cells, canvas):
   """

   :param cells: instance of :class:'CellularAutoma.Cells'
   :param canvas: instance of :class:'tkinter.Canvas'
   """
   cell_size = 20
   canvas.delete( ALL )
   for i in range( len( cells ) ):
      if cells[i]:
         start = i * cell_size
         canvas.create_rectangle( ( start, 0, start + cell_size, cell_size),
                                  fill=rectangle_color,
                                  outline=rectangle_color,
                                  activefill='black' )   # TODO add inner padding


def task ():
   automata.iterate_cells( )
   draw( automata.cells, canvas )
   if bind_state:
      root.after( 100, task )


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
