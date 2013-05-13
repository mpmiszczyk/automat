from unittest import TestCase
from CelluralAutoma import Rule, create_rules_from


class TestRule( TestCase ):
   def test_creating_an_rule (self):
      rule = Rule( 10 )


   def test_resolving_returns_a_cell (self):
      trueNeighbour = [True, True, True]

      rule = Rule( 0 )

      self.assertEqual( rule.resolve( trueNeighbour ), False )


   def test_creating_rules_for_zero_number (self):
      rules = create_rules_from( 0 )
