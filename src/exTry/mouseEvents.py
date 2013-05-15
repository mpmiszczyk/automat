from tkinter import Tk, ttk


root = Tk( )

label = ttk.Label( root, text="Starting ... " )
label.grid( )
label.bind( '<Enter>', lambda e: label.configure( text="Mouse moved inside" ) )
label.bind( '<Leave>', lambda e: label.configure( text="Mouse moved outside" ) )
label.bind( '<1>', lambda e: label.configure( text="Clicked left mouse button" ) )
label.bind( '<Double-1>', lambda e: label.configure( text="Double clicked left button" ) )
label.bind( '<B3-Motion>', lambda e: label.configure( text="Right button dragged to %d %d" % (e.x, e.y) ) )

root.mainloop( )