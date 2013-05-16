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
      if place < min( len( self.cells ), self._size ):
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
      return self._size


   # def size (self):
   #    return self._size

   def set_size (self, new_size):
      self._size = new_size


   def neighbors_of (self, key):
      if key == 0:
         return [self.cells[-1],
                 self.cells[0],
                 self.cells[1]]

      if key == len( self ) - 1:
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
   newCells = Cells( len( cells ) )
   for i in range( len( cells ) ):
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


class Automata( ):
   def __init__ (self, cells, rule, rows=100, colums=100):
      self.rows = rows
      self.columns = colums

      self.rule = rule
      self.cells = []
      self.add( cells )


   def iterate_cells (self):
      self.add( calculate_next_state( self.cells[-1], self.rule ) )


   def add (self, cells):
      if len( cells ) != self.columns:
         cells.set_size( self.columns )

      while len( self.cells ) >= self.rows:
         self.cells.pop( 0 )

      self.cells.append( cells )


   def new_random_rule (self, args):
      number = random.randint( 0, 255 )
      self.rule = Rule( number )
      print( number )


   def new_number_rule (self, number):
      number = max( 0, number )
      number = min( number, 255 )

      self.rule = Rule( number )


   def increase_column_size (self, args):
      self.columns += 1


   def decrease_column_size (self, args):
      self.columns -= 1


   def set_column_size ( self, size):
      self.columns = size


   def decrease_row_size (self, args):
      self.rows -= 1


   def increase_row_size (self, args):
      self.rows += 1


   def set_row_size ( self, size):
      self.rows = size


if __name__ == "__main__":
   cells = Cells( 100 )
   cells[50] = True

   random_int = random.randint( 0, 100 )
   rule = Rule( random_int )

   for _ in range( 100 ):
      print( cells )
      cells = calculate_next_state( cells, rule )

   print( "Rule nr: " + str( random_int ) )


