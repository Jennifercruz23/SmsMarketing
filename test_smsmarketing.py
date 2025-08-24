# test_smsmarketing.py
"""
Tests for SmsMarketing module.
"""

import unittest
from smsmarketing import SmsMarketing

class TestSmsMarketing(unittest.TestCase):
    """Test cases for SmsMarketing class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SmsMarketing()
        self.assertIsInstance(instance, SmsMarketing)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SmsMarketing()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
