import unittest
import music_reproductor
from unittest.mock import *
from unittest import TestCase
from unittest import main
import json
import unittest


def some_func():# Calls out to external API - which we want to mock
	response = music_reproductor.api_call()
	return response


class test_some_func_calling_api(TestCase):
    
	@patch('music_reproductor.api_call')
	def test_some_func(self, mock_api_call):

		# Sets up mock version of api_call
		mock_api_call.return_value = MagicMock(status_code=200, response=json.dumps({'key':'value'}))
		
        # Calls some_func() that calls the (mock) api_call() function
		result = some_func()

		# Check that the result returned from some_func() is what was expected
		self.assertEqual(result.status_code, 200, "returned status code is not 200")
		self.assertEqual(result.response, '{"key": "value"}', "response JSON incorrect")


if __name__ == '__main__':
    unittest.main()
