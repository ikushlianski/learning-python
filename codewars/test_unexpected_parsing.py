import unittest
from unexpected_parsing import get_status


class TestMyModule(unittest.TestCase):

    def test_status_busy(self):
        """
        Test the busy status
        """
        is_busy = True
        result = get_status(is_busy)
        self.assertEqual(result, {"status": "busy"})

    def test_status_available(self):
        """
        Test the available status
        """
        is_busy = False
        result = get_status(is_busy)
        self.assertEqual(result, {"status": "available"})
