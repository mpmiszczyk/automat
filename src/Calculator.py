from CelluralAutoma import Cells


def calculate_next_state (cells, rule):
   newCells = Cells( )
   for i in range( 0, cells.size( ) ):
      newCells[i] = rule.resolve( cells.neighboursOf( i ) )

   return newCells
