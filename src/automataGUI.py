# from tkinter import *
from tkinter import ttk, Tk, Canvas, ALL
from CellularAutoma import cells_from_string, Rule, Automata


TIME_STEP = 100

root = Tk( )

main_frame = ttk.Frame( root )
# main_frame.grid( column=0, row=0, sticky=(N, W, E, S) )
# main_frame.columnconfigure( 0, weight=1 )
# main_frame.rowconfigure( 0, weight=1 )
main_frame.pack( side='right', expand=1 )

canvas = Canvas( main_frame )
# canvas.grid( column=0, row=0, sticky=(N, W, E, S) )
canvas.pack( expand=1 )

rectangle_color = 'red'

# TODO random initialize
automata = Automata( cells_from_string( "____#__#__#______###__##_#" ),
                     Rule( 90 ),
                     rows=50 )


def draw (cells, canvas):
   """

   :param cells: instance of :class:'CellularAutoma.Cells'
   :param canvas: instance of :class:'tkinter.Canvas'
   """
   cell_size = 5
   canvas.delete( ALL )
   for row_number in range( len( cells ) ):
      for cell_number in range( len( cells[row_number] ) ):
         if cells[row_number][cell_number]:
            row_offset = row_number * cell_size
            column_offset = cell_number * cell_size
            canvas.create_rectangle( ( column_offset,
                                       row_offset,
                                       column_offset + cell_size,
                                       row_offset + cell_size),
                                     fill=rectangle_color,
                                     outline=rectangle_color )   # TODO add inner padding


def task ():
   automata.iterate_cells( )
   draw( automata.cells, canvas )
   if bind_state:
      root.after( TIME_STEP, task )


bind_state = True


def start_stop (args):
   global bind_state
   if bind_state:
      bind_state = False
   else:
      bind_state = True
      root.after( TIME_STEP, task )


root.bind( "<space>", start_stop )
root.bind( "<Control-r>", automata.new_random_rule )

root.after( TIME_STEP, task )
root.mainloop( )
