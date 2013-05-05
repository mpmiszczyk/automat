from unittest import TestCase
from CelluralAutoma import Cells, Rule, calculate_next_state
from mock import Mock
from random import randint


class TestCellularCalculation( TestCase ):
   def setUp (self):
      self.cells = Cells( randint( 3, 14 ) )
      self.rule = Rule( )


   def test_new_cells_have_same_size_as_the_old_ones (self):
      self.rule.resolve = Mock( )

      self.new_cells = calculate_next_state( self.cells, self.rule )

      self.assertEqual( self.new_cells.size( ), self.cells.size( ) )


   def test_new_value_depends_on_value_returned_by_rule_resolve (self):
      self.rule.resolve = Mock( return_value=True )

      # for each cell in cells
      # pass cell naigbours to rule
      # rule returns one cell stage

      self.new_cells = calculate_next_state( self.cells, self.rule )

      for cell in self.new_cells:
         self.assertEqual( cell, True )



