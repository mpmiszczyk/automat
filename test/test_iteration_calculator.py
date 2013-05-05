from unittest import TestCase
from CelluralAutoma import Cells, Rule, calculate_next_state
from mock import Mock
from random import randint


class TestCellularCalculation( TestCase ):
   def test_new_cells_have_same_size_as_the_old_ones (self):
      cells = Cells( randint( 3, 14 ) )
      rule = Rule( )

      rule.resolve = Mock( )
      rule.resolve.return_value = True

      new_cells = calculate_next_state( cells, rule )

      self.assertEqual( new_cells.size( ), cells.size( ) )


   def test_new_value_depends_on_value_returned_by_rule_resolve (self):
      cells = Cells( )
      rule = Rule( )

      rule.resolve = Mock( )
      rule.resolve.return_value = True

      # for each cell in cells
      # pass cell naigbours to rule
      # rule returns one cell stage
      #

      new_cells = calculate_next_state( cells, rule )

      for cell in new_cells:
         self.assertEqual( cell, True )



