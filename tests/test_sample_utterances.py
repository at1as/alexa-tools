from   os import path
import sys
import unittest

class TestStringMethods(unittest.TestCase):

  def test_balanced_parenthesis_throws_unbalanced(self):
    with self.assertRaises(Exception):
      sampleUtteranceBuilder.balanced_parenthesis('hello<world>hello<')
    
    with self.assertRaises(Exception):
      sampleUtteranceBuilder.balanced_parenthesis('hello<world>hello>')
    
    with self.assertRaises(Exception):
      sampleUtteranceBuilder.balanced_parenthesis('helloworld>hello')
    
    with self.assertRaises(Exception):
      sampleUtteranceBuilder.balanced_parenthesis('hello<worldhello')

  def test_balanced_parenthesis_balanced(self):
    self.assertEqual(sampleUtteranceBuilder.balanced_parenthesis('hello<world>hello'), None)


  def test_extract_choices(self):
    self.assertEqual(sampleUtteranceBuilder.extract_choices('Hello <World|Mars|Venus>'), ['World|Mars|Venus'])
  
  def test_extract_choices_trailing(self):
    self.assertEqual(sampleUtteranceBuilder.extract_choices('Hello <World|Mars|Venus|>'), ['World|Mars|Venus|'])
  
  def test_extract_choices_multiple(self):
    self.assertEqual(sampleUtteranceBuilder.extract_choices('Hello <World|Mars|Venus> Goodbye <Jupiter|Neptune>'), ['World|Mars|Venus', 'Jupiter|Neptune'])

  
  def test_remove_choices(self):
    self.assertEqual(sampleUtteranceBuilder.remove_choices('Hello <World|Mars|Venus> Goodbye'), 'Hello <> Goodbye')
  
  def test_remove_choices_trailing(self):
    self.assertEqual(sampleUtteranceBuilder.remove_choices('Hello <World|Mars|> Goodbye'), 'Hello <> Goodbye')
  
  def test_remove_choices_multiple(self):
    self.assertEqual(sampleUtteranceBuilder.remove_choices('Hello <World|Mars|Venus> Goodbye <Jupiter|Neptune>'), 'Hello <> Goodbye <>')

  
  def test_split_choices(self):
    self.assertEqual(sampleUtteranceBuilder.split_choices(['World|Mars|Venus']), [['World', 'Mars', 'Venus']])
  
  def test_split_choices_trailing(self):
    self.assertEqual(sampleUtteranceBuilder.split_choices(['World|Mars|Venus|']), [['World', 'Mars', 'Venus', '']])

  def test_split_choices_multiple(self):
    self.assertEqual(sampleUtteranceBuilder.split_choices(['World|Mars|Venus', 'Titan|Europa']), [['World', 'Mars', 'Venus'], ['Titan', 'Europa']])


if __name__ == '__main__':
  if __package__ == None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    import sampleUtteranceBuilder

  unittest.main()

