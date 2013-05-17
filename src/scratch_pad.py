from tkinter import Canvas


canvas = Canvas( )

color = "black"


def setColor (newcolor):
   global color
   color = newcolor


def addLine (event):
   global lastx, lasty
   canvas.create_line( (lastx, lasty, event.x, event.y), fill=color )
   lastx, lasty = event.x, event.y


id = canvas.create_rectangle( (10, 10, 30, 30), fill="red" )
canvas.tag_bind( id, "<Button-1>", lambda x: setColor( "red" ) )
id = canvas.create_rectangle( (10, 35, 30, 55), fill="blue" )
canvas.tag_bind( id, "<Button-1>", lambda x: setColor( "blue" ) )
id = canvas.create_rectangle( (10, 60, 30, 80), fill="black" )
canvas.tag_bind( id, "<Button-1>", lambda x: setColor( "black" ) )


def setColor (newcolor):
   global color
   color = newcolor
   canvas.dtag( 'all', 'paletteSelected' )
   canvas.itemconfigure( 'palette', outline='white' )
   canvas.addtag( 'paletteSelected', 'withtag', 'palette%s' % color )
   canvas.itemconfigure( 'paletteSelected', outline='#999999' )


id = canvas.create_rectangle( (10, 10, 30, 30), fill="red", tags=('palette', 'palettered') )
id = canvas.create_rectangle( (10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue') )
id = canvas.create_rectangle( (10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected') )

setColor( 'black' )
canvas.itemconfigure( 'palette', width=5 )

