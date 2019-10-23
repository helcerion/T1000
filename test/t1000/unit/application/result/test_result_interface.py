import unittest
from unittest.mock import Mock

from src.t1000.application.result.result_interface import ResultInterface

class ResultInterfaceTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_implements_without_implement_get_method(self):
        result_no_get = ResultNoGet(Mock(), Mock())
        with self.assertRaises(Exception, ) as result_interface_exception:
            result_no_get.get()

        self.assertEqual(str(result_interface_exception.exception), \
            'You need to implement get function from ResultNoGet.')

class ResultNoGet(ResultInterface):
    pass