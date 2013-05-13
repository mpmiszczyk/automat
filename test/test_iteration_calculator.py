from unittest import TestCase
from CelluralAutoma import Cells, Rule, calculate_next_state
from mock import Mock
from random import randint


class TestCellularCalculation( TestCase ):
   def setUp (self):
      self.automa_size = randint( 3, 14 )
      self.cells = Cells( self.automa_size )
      self.rule = Mock( spec=Rule )


   def test_new_cells_have_same_size_as_the_old_ones (self):
      self.new_cells = calculate_next_state( self.cells, self.rule )

      self.assertEqual( self.new_cells.size( ), self.cells.size( ) )


   def test_new_value_depends_on_value_returned_by_rule_resolve (self):
      self.rule.resolve.return_value = True

      self.new_cells = calculate_next_state( self.cells, self.rule )

      self.assertEqual( self.automa_size, self.rule.resolve.call_count )
      for cell in self.new_cells:
         self.assertEqual( cell, True )



         # def test_few_iterations_of_cells(self):
