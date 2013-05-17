# from tkinter import *
from tkinter import ttk, Tk, Canvas, ALL, N, W, E, S, HORIZONTAL
import tkinter
from CellularAutoma import cells_from_string, Rule, Automata, number_to_cells


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


def draw (cells, canvas, cell_size=5):
   """

   :param cells: instance of :class:'CellularAutoma.Cells'
   :param canvas: instance of :class:'tkinter.Canvas'
   """
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
   draw( automata.cells, canvas, cell_size=5 )
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

output_states = []

for i in range( 8 ):
   frame_label = str( i + 1 )
   frame = ttk.Labelframe( p, text=frame_label, width=100, height=100 )
   frame.grid( )

   #TODO teraz trzeba wyrysować pojedyńcze źródła zasad (z cyferki)
   label = ttk.Label( frame, text="Sąsiedzi przed:" )
   label.grid( )
   before_iteration = Canvas( frame, width=60, height=20, background="white" )
   prev_cells = number_to_cells( i )
   draw( [prev_cells], before_iteration, cell_size=20 )
   before_iteration.grid( )

   #TODO i później dodać jeszcze klikalny wyznacznik zasady
   second_label = ttk.Label( frame, text="Komórka po:" )
   second_label.grid( )
   after_iteration = Canvas( frame, width=30, height=30 )

   if automata.state_for_cells( prev_cells ):
      color = "red"
   else:
      color = "pink"

   rectangle_id = after_iteration.create_rectangle( (0, 0, 30, 30), fill=color, outline=color )

   output_states.append( {'canvas': after_iteration, 'rec_id': rectangle_id} )


   def local_bind ( number):
      return lambda x: automata.change_single_rule( number )


   after_iteration.tag_bind( rectangle_id, "<Button-1>", local_bind( i ) )

   after_iteration.grid( )
   p.add( frame )


def update_rule ( *args):
   automata.new_number_rule( spin_rule_number.get( ) )


def update_outputs_of_rule (*args):
   for i in range( len( output_states ) ):
      if automata.rule_state( i ):
         color = "red"
      else:
         color = "pink"
      rec_id = output_states[i]['rec_id']
      canvas = output_states[i]['canvas']

      canvas.itemconfigure( rec_id, fill=color, outline=color )


spin_rule_number = tkinter.IntVar( value=automata.rule._number )
automata.add_rule_obserwer( spin_rule_number )
spin_rule_number.trace( "w", update_outputs_of_rule )  # needs to be before update_rule!!!
spin_rule_number.trace( "w", update_rule )

spin = tkinter.Spinbox( p, from_=0, to=255, textvariable=spin_rule_number )
p.add( spin )

cells_frame = ttk.Frame( options_notebook )

root.after( TIME_STEP, task )
root.mainloop( )
