import unittest

from Phonebook import Phonebook

class Phonebooktest(unittest.TestCase):
    def setUp(self):
        self.phonebook = Phonebook()
    def tearDown(self):
        pass
    def test_lookup_by_name(self):
        self.phonebook.add("BOB","12345")
        number = self.phonebook.lookup("BOB")
        self.assertEqual("12345",number)
    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")
            
