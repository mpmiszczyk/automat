import tkinter
from tkinter import ttk, N, W, E, S


top = tkinter.Tk( )
top.title( "feet to meters" )

main_frame = ttk.Frame( top, padding="3 3 12 12" )
main_frame.grid( column=0, row=0, sticky=(N, W, E, S) )
main_frame.columnconfigure( 0, weight=1 )
main_frame.rowconfigure( 0, weight=1 )

feet = tkinter.StringVar( )

feet_entry = ttk.Entry( main_frame, width=7, textvariable=feet )
feet_entry.grid( column=2, row=1, sticky=(W, E) )

meters = tkinter.StringVar( )
ttk.Label( main_frame, textvariable=meters ).grid( column=2, row=2, sticky=W )


def calculate (*args):
   try:
      value = float( feet.get( ) )
      meters.set( (0.3048 * value * 10000.0 + 0.5) / 10000.0 )
   except ValueError:
      pass


ttk.Button( main_frame, text="Calculate", command=calculate ).grid( column=2, row=3, sticky=(W, E) )

ttk.Label( main_frame, text="feet" ).grid( column=3, row=1, sticky=W )
ttk.Label( main_frame, text="is equivalent to" ).grid( column=1, row=2, sticky=E )
ttk.Label( main_frame, text="meters" ).grid( column=3, row=2, sticky=W )

for child in main_frame.winfo_children( ): child.grid_configure( padx=5, pady=5 )

feet_entry.focus( )
top.bind( '<Return>', calculate )

top.mainloop( )