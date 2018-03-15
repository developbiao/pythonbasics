import unittest
class TestMysql(unittest.TestCase):
    def setUp(self):
        print('setup...')
    def tearDown(self):
        print('tearDown...')

    def test_connect(self):
        self.assertEqual(7, 7)
