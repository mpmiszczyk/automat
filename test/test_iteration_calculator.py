from unittest import TestCase
from CellularAutoma import Cells, Rule, calculate_next_state, cells_from_string
from mock import Mock
from random import randint
from test_cells import Some


class TestCellularCalculation( TestCase ):
   def setUp (self):
      self.automa_size = randint( 3, 14 )
      self.cells = Cells( self.automa_size )
      self.rule = Mock( spec=Rule )


   def test_new_cells_have_same_size_as_the_old_ones (self):
      self.new_cells = calculate_next_state( self.cells, self.rule )

      self.assertEqual( len( self.new_cells ), len( self.cells ) )


   def test_new_value_depends_on_value_returned_by_rule_resolve (self):
      same = Some( )
      self.rule.resolve.return_value = same

      self.new_cells = calculate_next_state( self.cells, self.rule )

      self.assertEqual( self.automa_size, self.rule.resolve.call_count )
      for cell in self.new_cells:
         self.assertEqual( cell, same )


   def test_few_iterations_of_cells_rule_90_Sierpinski (self):
      cells = cells_from_string( "________#________" )
      rule = Rule( 90 )

      newCells = calculate_next_state( cells, rule )
      self.assertEqual( "_______#_#_______", str( newCells ) )
      newCells = calculate_next_state( newCells, rule )
      self.assertEqual( "______#___#______", str( newCells ) )
      newCells = calculate_next_state( newCells, rule )
      self.assertEqual( "_____#_#_#_#_____", str( newCells ) )
      newCells = calculate_next_state( newCells, rule )
      self.assertEqual( "____#_______#____", str( newCells ) )
      newCells = calculate_next_state( newCells, rule )
      self.assertEqual( "___#_#_____#_#___", str( newCells ) )
      newCells = calculate_next_state( newCells, rule )
      self.assertEqual( "__#___#___#___#__", str( newCells ) )
      newCells = calculate_next_state( newCells, rule )
      self.assertEqual( "_#_#_#_#_#_#_#_#_", str( newCells ) )
