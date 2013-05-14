import tkinter
from tkinter import ttk, N, W, E, S


top = tkinter.Tk( )
top.title( "feet to meters" )

main_frame = ttk.Frame( top, padding="3 3 12 12" )
main_frame.grid( column=0, row=0, sticky=(N, W, E, S) )
main_frame.columnconfigure( 0, weight=1 )
main_frame.rowconfigure( 0, weight=1 )

feet = tkinter.StringVar( )
meters = tkinter.StringVar( )

feet_entry = ttk.Entry( main_frame, width=7, textvariable=feet )
feet_entry.grid( column=2, row=1, sticky=(W, E) )

top.mainloop( )