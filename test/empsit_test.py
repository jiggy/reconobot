import unittest
import empsit

class empsit_test(unittest.TestCase):
    def setUp(self):
        print "setting up"

    def test_empsit(self):
        data = empsit.get_empsit_data()
        self.assertIsNotNone(data)
        self.assertTrue(data.has_key('Participation rate'), "Participation rate not in data")
        print data
        title = empsit.generate_headline(data)
        self.assertIsNotNone(title)
        print title
