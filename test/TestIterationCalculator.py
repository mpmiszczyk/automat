import unittest
from Calculator import calculate_next_state
from CelluralAutoma import Cells, Rule


class TestCellularCalculation( unittest.TestCase ):
   def test_creating_interface (self):
      cells = Cells( )
      rule = Rule( )

      new_cells = calculate_next_state( cells, rule )


if __name__ == '__main__':
   unittest.main( )
