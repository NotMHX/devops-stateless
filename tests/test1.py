import unittest, helper

class TestTodos(unittest.TestCase):

    def testAdd(self):
        helper.delete()
        helper.add("new")
        self.assertEqual(helper.todos[0].title, "new")
        self.assertFalse(helper.todos[0].isCompleted)

    def testUpdate(self):
        helper.update(0)
        self.assertTrue(helper.todos[0].isCompleted)

    def testBBB(self):
        helper.add("book")
        self.assertEqual(helper.todos[1].title, "bbbook")

# Enter this in the command prompt to run tests:
# py -m unittest tests/test1.py