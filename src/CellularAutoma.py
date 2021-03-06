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


def number_to_cells ( number):
   cell_values = [False, True]
   i = 0

   for first in cell_values:
      for second in cell_values:
         for third in cell_values:
            if number == i:
               return [first, second, third]
            i += 1

   return [False, False, False]


class Rule( ):
   def __init__ (self, number):
      self.set_number( number )


   def resolve (self, cells):
      number = cells_to_number( cells )
      return self._rules[number]


   def set_number (self, number):
      self._number = number
      self._rules = create_rules_from( number )


   def state_for (self, i):
      return self._rules[i]


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


def new_random_cells (size):
   cells = Cells( size )
   for i in range( size ):
      cells[i] = not bool( random.randint( 0, 3 ) )

   return cells


def new_cells_with_one_true (size):
   cells = Cells( size )
   cells[size // 2] = True
   return cells


class Automata( ):
   def __init__ (self, cells, rule, rows=100, columns=100):
      self.rows = rows
      self.columns = columns

      self.rule = rule
      self.cells = []
      self.add( cells )
      self._rule_obserwers = []


   def iterate_cells (self):
      self.add( calculate_next_state( self.cells[-1], self.rule ) )


   def add (self, cells):
      if len( cells ) != self.columns:
         cells.set_size( self.columns )

      while len( self.cells ) >= self.rows:
         self.cells.pop( 0 )

      self.cells.append( cells )


   def new_random_rule (self, args):
      self.new_number_rule( random.randint( 0, 255 ) )


   def new_number_rule (self, number):
      number = max( 0, number )
      number = min( number, 255 )

      self.rule = Rule( number )
      self.update_rule_obserwers( )


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


   def new_random_cells (self, args):
      self.add( new_random_cells( self.columns ) )


   def new_one_cell (self, args):
      self.add( new_cells_with_one_true( self.columns ) )


   def add_rule_obserwer (self, spin_rule_number):
      self._rule_obserwers.append( spin_rule_number )


   def update_rule_obserwers (self):
      for obserwer in self._rule_obserwers:
         obserwer.set( self.rule._number )


   def change_single_rule (self, number):

      rules = self.rule._rules.copy( )

      rules[number] = not rules[number]

      new_rule_number = 0
      for i in range( len( rules ) ):
         if rules[i]:
            new_rule_number += 2 ** i

      self.new_number_rule( new_rule_number )


   def state_for_cells (self, prev_cells):
      return self.rule.resolve( prev_cells )


   def rule_state (self, i):
      return self.rule.state_for( i )


if __name__ == "__main__":
   cells = Cells( 100 )
   cells[50] = True

   random_int = random.randint( 0, 100 )
   rule = Rule( random_int )

   for _ in range( 100 ):
      print( cells )
      cells = calculate_next_state( cells, rule )

   print( "Rule nr: " + str( random_int ) )


