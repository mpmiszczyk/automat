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


   def append_empty_cells_to (self, key):
      oldSize = self._size
      self._size = key + 1
      for i in range( oldSize - 1, self._size - 1 ):
         self.cells.append( False )


   def __iter__ (self):
      return self.cells.__iter__( )


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
   return {}


class Rule( ):
   def __init__ (self, number):
      self.set_number( number )


   def resolve (self, cells):
      for previous, output in self._rules:
         if cells == previous:
            return output
      return False


   def set_number (self, number):
      self._number = number
      self._rules = create_rules_from( number )


def calculate_next_state (cells, rule):
   newCells = Cells( cells.size( ) )
   for i in range( 0, cells.size( ) ):
      newCells[i] = rule.resolve( cells.neighbors_of( i ) )

   return newCells