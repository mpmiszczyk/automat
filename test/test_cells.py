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

      _ = cells[10]
      self.assertEqual( cells.size( ), 5 )


   def test_able_to_set_values_outside_size (self):
      cells = Cells( 5 )

      self.assertEqual( cells.size( ), 5 )

      some = Some( )
      cells[10] = some

      self.assertEqual( cells.size( ), 11 )
      self.assertIs( cells[10], some )


class TestGettingNeighbors( TestCase ):
   def setUp (self):
      self.cells = Cells( 5 )

      for i in range( 0, 5 ):
         self.cells[i] = Some( )


   def test_should_be_able_to_get_neighbours (self):
      neighbours = self.cells.neighbors_of( 1 )

      self.assertEqual( len( neighbours ), 3 )


   def test_should_be_able_to_get_right_neighbours (self):
      neighbours = self.cells.neighbors_of( 1 )

      self.assertEqual( neighbours[0], self.cells[0] )
      self.assertEqual( neighbours[1], self.cells[1] )
      self.assertEqual( neighbours[2], self.cells[2] )


   def test_should_be_able_to_get_right_neighbours (self):
      neighbours = self.cells.neighbors_of( 2 )

      self.assertEqual( neighbours[0], self.cells[1] )
      self.assertEqual( neighbours[1], self.cells[2] )
      self.assertEqual( neighbours[2], self.cells[3] )


   def test_handling_neighbours_of_first_element (self):
      neighbours = self.cells.neighbors_of( 0 )

      self.assertEqual( neighbours[0], self.cells[-1] )
      self.assertEqual( neighbours[1], self.cells[0] )
      self.assertEqual( neighbours[2], self.cells[1] )



