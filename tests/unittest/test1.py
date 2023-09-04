import unittest, helper

class TestTodos(unittest.TestCase):

    def testAdd(self):
        helper.delete()
        helper.add("shopping")
        self.assertEqual(helper.todos[0].title, "shopping")
        self.assertFalse(helper.todos[0].isCompleted)

    def testUpdate(self):
        helper.update(0)
        self.assertTrue(helper.todos[0].isCompleted)

    def testBBB(self):
        helper.add("book")
        self.assertEqual(helper.todos[1].title, "bbbook")

# Folgendes eingeben, um Tests auszuführen:
# py -m unittest tests/test1.py