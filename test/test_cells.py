from unittest import TestCase
from CelluralAutoma import Cells


class Some( object ):
   pass


class TestCells( TestCase ):
   def test_default_initialization (self):
      cells = Cells( )

      self.assertEqual( cells.size( ), 100 )


   def test_create_shorter_cells (self):
      cells = Cells( 5 )

      self.assertEqual( cells.size( ), 5 )


   def test_cells_outside_of_size_are_false (self):
      cells = Cells( 5 )

      self.assertEqual( cells[10], False )


   def test_cells_outside_of_size_do_not_change_cells_size (self):
      cells = Cells( 5 )

      cells[10]
      self.assertEqual( cells.size( ), 5 )


   def test_able_to_set_values_outside_size (self):
      cells = Cells( 5 )

      self.assertEqual( cells.size( ), 5 )

      some = Some( )
      cells[10] = some

      self.assertEqual( cells.size( ), 11 )
      self.assertIs( cells[10], some )


