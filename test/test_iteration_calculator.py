from unittest import TestCase
from CelluralAutoma import Cells, Rule, calculate_next_state
from mock import Mock


class TestCellularCalculation( TestCase ):
   def test_creating_interface (self):
      cells = Cells( )
      rule = Rule( )

      rule.resolve = Mock( )
      rule.resolve.return_value( True )

      # for each cell in cells
      # pass cell naigbours to rule
      # rule returns one cell stage
      #

      new_cells = calculate_next_state( cells, rule )

      for cell in new_cells:
         self.assertEqual( cell, True )



