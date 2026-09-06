# test_digitaldrift.py
"""
Tests for DigitalDrift module.
"""

import unittest
from digitaldrift import DigitalDrift

class TestDigitalDrift(unittest.TestCase):
    """Test cases for DigitalDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigitalDrift()
        self.assertIsInstance(instance, DigitalDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigitalDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
