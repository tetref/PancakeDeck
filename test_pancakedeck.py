# test_pancakedeck.py
"""
Tests for PancakeDeck module.
"""

import unittest
from pancakedeck import PancakeDeck

class TestPancakeDeck(unittest.TestCase):
    """Test cases for PancakeDeck class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PancakeDeck()
        self.assertIsInstance(instance, PancakeDeck)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PancakeDeck()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
