from unittest.mock import *
from unittest import TestCase
from unittest import main
from mock_and_magic_mock_classes import SomeClass
import unittest


class test_SomeClass_public_interface(TestCase):

	def test_public_method(self):
		test_object = SomeClass()

		# Set up canned response on mock method
		test_object.hidden_method = MagicMock(name = 'hidden_method')
		test_object.hidden_method.return_value = 10

	    # Test the object
		result = test_object.public_method(5)

		self.assertEqual(15, result, 'return value from public_method incorrect')


if __name__ == '__main__':
    unittest.main()
