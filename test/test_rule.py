from unittest import TestCase
from CellularAutoma import Rule, create_rules_from, cells_to_number, number_to_cells


class TestRule( TestCase ):
   def test_creating_an_rule (self):
      rule = Rule( 10 )


   def test_resolving_returns_a_cell (self):
      trueNeighbour = [True, True, True]

      rule = Rule( 0 )

      self.assertEqual( rule.resolve( trueNeighbour ), False )


   def test_rule_for_more_complex_example (self):
      rule = Rule( 22 )

      neighbours = [True, True, True]
      self.assertEqual( False, rule.resolve( neighbours ) )

      neighbours = [True, False, False]
      self.assertEqual( True, rule.resolve( neighbours ) )

      neighbours = [False, True, False]
      self.assertEqual( True, rule.resolve( neighbours ) )

      neighbours = [False, True, True]
      self.assertEqual( False, rule.resolve( neighbours ) )

      neighbours = [True, True, False]
      self.assertEqual( False, rule.resolve( neighbours ) )


   def test_creating_rules_gives_eight_elements_tuple (self):
      rules = create_rules_from( 0 )

      self.assertEqual( 8, len( rules ) )


   def test_zero_creates_all_false_rule (self):
      rule = create_rules_from( 0 )

      for i in range( 8 ):
         self.assertFalse( rule[i] )


   def test_one_creates_one_true_rule (self):
      rule = create_rules_from( 1 )

      for i in range( 8 ):
         if i == 0:
            self.assertTrue( rule[i] )
         else:
            self.assertFalse( rule[i] )


   def test_creating_rule_for_more_complicated_example (self):
      rule = create_rules_from( 90 )

      for i in range( 8 ):
         if i in [1, 3, 4, 6]:
            self.assertTrue( rule[i] )
         else:
            self.assertFalse( rule[i] )


   def test_changing_cells_to_number_from_zero (self):
      all_cells = [[False, False, False],
                   [False, False, True],
                   [False, True, False],
                   [False, True, True],
                   [True, False, False],
                   [True, False, True],
                   [True, True, False],
                   [True, True, True]]

      for i in range( 8 ):
         self.assertEqual( i, cells_to_number( all_cells[i] ) )


   def test_changing_cells_to_number_from_zero (self):
      all_cells = [[False, False, False],
                   [False, False, True],
                   [False, True, False],
                   [False, True, True],
                   [True, False, False],
                   [True, False, True],
                   [True, True, False],
                   [True, True, True]]

      for i in range( 8 ):
         self.assertEqual( all_cells[i], number_to_cells( i ) )



