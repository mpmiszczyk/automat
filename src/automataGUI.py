# from tkinter import *
from tkinter import ttk, Tk, Canvas, ALL, N, W, E, S, HORIZONTAL
from CellularAutoma import cells_from_string, Rule, Automata


TIME_STEP = 100

root = Tk( )
# root.grid(baseHeight=100, baseWidth=100, widthInc=500, heightInc=500 )

main_frame = ttk.Frame( root )
main_frame.grid( column=0, row=0, sticky=(N, W, E, S) )
main_frame.columnconfigure( 0, weight=1 )
main_frame.rowconfigure( 0, weight=1 )
# main_frame.pack( side='right', expand=1 )

canvas = Canvas( main_frame )  #TODO: maybe options like ( .. , width=10000, height=10000)
canvas.grid( column=0, row=0, sticky=(N, W, E, S) )
# canvas.pack( expand=1 )

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

root.bind( "<Control-e>", automata.new_random_cells )
root.bind( "<Control-w>", automata.new_one_cell )

root.bind( "<Control-p>", automata.increase_column_size )
root.bind( "<Control-o>", automata.decrease_column_size )
root.bind( "<Control-j>", automata.increase_row_size )
root.bind( "<Control-u>", automata.decrease_row_size )

options_notebook = ttk.Notebook( main_frame )
options_notebook.grid( column=0, row=1, sticky=(N, E, W, S) )

rule_frame = ttk.Frame( options_notebook )
rule_frame.grid( )
options_notebook.add( rule_frame, text="Zasada" )

p = ttk.Panedwindow( rule_frame, orient=HORIZONTAL )
p.grid( )

for i in range( 8 ):
   frame_label = str( i + 1 )
   frame = ttk.Labelframe( p, text=frame_label, width=100, height=100 )
   p.add( frame )

cells_frame = ttk.Frame( options_notebook )
options_notebook.add( cells_frame, text="Komórki" )

root.after( TIME_STEP, task )
root.mainloop( )
