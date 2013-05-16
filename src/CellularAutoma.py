import random


class Cells( ):
   def __init__ (self, size=100):
      self._size = size
      self.fill_with_empty_cells( )


   def fill_with_empty_cells (self):
      self.cells = []
      for i in range( 0, self._size ):
         self.cells.append( False )


   def __getitem__ (self, place):
      if place < self._size:
         return self.cells[place]

      else:
         return False


   def __setitem__ (self, key, value):
      if key >= self._size:
         self.append_empty_cells_to( key )

      self.cells[key] = value


   def __str__ (self):
      string = ""
      for cell in self.cells:
         if cell:
            string += "#"
         else:
            string += "_"

      return string


   def append_empty_cells_to (self, key):
      oldSize = self._size
      self._size = key + 1
      for i in range( oldSize - 1, self._size - 1 ):
         self.cells.append( False )


   def __iter__ (self):
      return self.cells.__iter__( )


   def __len__ (self):
      return len( self.cells )


   def size (self):
      return self._size


   def neighbors_of (self, key):
      if key == 0:
         return [self.cells[-1],
                 self.cells[0],
                 self.cells[1]]

      if key == self.size( ) - 1:
         return [self.cells[-2],
                 self.cells[-1],
                 self.cells[0]]

      return self.cells[key - 1: key + 2]


def create_rules_from (number):
   rules = dict( )

   representation = bin( number )[2:]

   for i in range( 8 ):
      if i < len( representation ):
         rules[i] = ( "1" == representation[-1 - i])
      else:
         rules[i] = False

   return rules


def cells_to_number (cells):
   cell_values = [False, True]
   i = 0

   for first in cell_values:
      for second in cell_values:
         for third in cell_values:
            if cells == [first, second, third]:
               return i
            i += 1
   return 0


class Rule( ):
   def __init__ (self, number):
      self.set_number( number )


   def resolve (self, cells):
      number = cells_to_number( cells )
      return self._rules[number]


   def set_number (self, number):
      self._number = number
      self._rules = create_rules_from( number )


def calculate_next_state (cells, rule):
   newCells = Cells( cells.size( ) )
   for i in range( cells.size( ) ):
      newCells[i] = rule.resolve( cells.neighbors_of( i ) )

   return newCells


def cells_from_int_array ( array):
   cells = Cells( len( array ) )

   for i in range( len( array ) ):
      cells[i] = bool( array[i] )

   return cells


def cells_from_string ( string):
   cells = Cells( len( string ) )

   for i in range( len( string ) ):
      cells[i] = ( string[i] == "#" )

   return cells


if __name__ == "__main__":
   cells = Cells( 100 )
   cells[50] = True

   random_int = random.randint( 0, 100 )
   rule = Rule( random_int )

   for _ in range( 100 ):
      print( cells )
      cells = calculate_next_state( cells, rule )

   print( "Rule nr: " + str( random_int ) )




