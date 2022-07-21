from unittest.mock import *
from unittest import TestCase
from unittest import main
from mock_and_magic_mock_classes import SomeClass
import unittest


class test_SomeClass_public_interface(TestCase):

	@patch.object(SomeClass, 'hidden_method')
	def test_public_method(self, mock_method):

		# Set up canned response
		mock_method.return_value = 10

		# Create object to be tested
		test_object = SomeClass()
		result = test_object.public_method(5)
		
		self.assertEqual(15, result, 'return value from public_method incorrect')


# You can also use the @patch() decorator to mock a function from a module.
# For example, given some external module with a function api_call, we can
# mock that function out using the @patch() decorator:
#
# @patch('external_module.api_call')
#     def test_some_func(self, mock_api_call):


if __name__ == '__main__':
    unittest.main()
