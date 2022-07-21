import people
from unittest.mock import *
from unittest import TestCase


class MyTest(TestCase):

    @patch('people.Person')
    def test_one(self, MockPerson):

        self.assertIs(people.Person, MockPerson)
        instance = MockPerson.return_value
        instance.age = 24
        instance.name = 'Adam'

        self.assertEqual(24, instance.age, 'age incorrect')
        self.assertEqual('Adam', instance.name, 'name incorrect')

# If the attribute itself needs to be a mock object then all that is required is to
# assign a MagicMock (or Mock) object to that attribute:
#
# instance.address = MagicMock(name='Address')

# Mocking Constants
# It is very easy to mock out a constant; this can be done using the @patch()
# decorator and proving the name of the constant and the new value to use. This value
# can be a literal value such as 42 or ‘Hello’ or it can be a mock object itself (such as
# a MagicMock object). For example:
#
# @patch('mymodule.MAX_COUNT', 10)
# def test_something(self):
# Test can now use mymodule.MAX_COUNT
# 
# If the attribute itself needs to be a mock object then all that is required is to
# assign a MagicMock (or Mock) object to that attribute:
# instance.address = MagicMock(name='Address') 

# Mocking Properties
# @patch('mymoule.Car.wheels', new_callable=mock.PropertyMock)
# def test_some_property(self, mock_wheels):
#     mock_wheels.return_value = 6
# Rest of test method

# Raising Exceptions with Mocks
# A very useful attribute that can be specified when a mock object is created is the
# side_effect. If you set this to an exception class or instance then the exception
# will be raised when the mock is called, for example:
# mock = Mock(side_effect=Exception('Boom!'))
# mock()