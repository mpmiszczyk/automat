from unittest import TestCase
from unittest.case import skip
from Calculator import calculate_next_state
from CelluralAutoma import Cells, Rule
# from mock import MagicMock


class TestCellularCalculation( TestCase ):
   @skip( "to be implemented" )
   def test_creating_interface (self):
      cells = Cells( )
      rule = Rule( )

      # for each cell in cells
      # pass cell naigbours to rule
      # rule returns one cell stage
      #

      new_cells = calculate_next_state( cells, rule )

      self.fail( "?no lower logic to test?" )


