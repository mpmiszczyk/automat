from tkinter import *
from tkinter import ttk


root = Tk( )

content = ttk.Frame( root )
frame = ttk.Frame( content, borderwidth=5, relief="sunken", width=200, height=100 )
name_label = ttk.Label( content, text="Name" )
name = ttk.Entry( content )

one_var = BooleanVar( )
two_var = BooleanVar( )
three_var = BooleanVar( )
one_var.set( True )
two_var.set( False )
three_var.set( True )

one = ttk.Checkbutton( content, text="One", variable=one_var, onvalue=True )
two = ttk.Checkbutton( content, text="Two", variable=two_var, onvalue=True )
three = ttk.Checkbutton( content, text="Three", variable=three_var, onvalue=True )
ok = ttk.Button( content, text="Okay" )
cancel = ttk.Button( content, text="Cancel" )

content.grid( column=0, row=0 )
frame.grid( column=0, row=0, columnspan=3, rowspan=2 )
name_label.grid( column=3, row=0, columnspan=2 )
name.grid( column=3, row=1, columnspan=2 )
one.grid( column=0, row=3 )
two.grid( column=1, row=3 )
three.grid( column=2, row=3 )
ok.grid( column=3, row=3 )
cancel.grid( column=4, row=3 )

root.mainloop( )
