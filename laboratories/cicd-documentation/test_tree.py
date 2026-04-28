import unittest
from tree import Tree
from node import Node

class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(8)
        self.tree.add(1)
        self.tree.add(4)

    def test_find_existing_node(self):
        found_node = self.tree.find(4)
        
        self.assertIsNotNone(found_node, "Nodul ar trebui sa fie gasit, deci nu trebuie sa fie None.")
        self.assertEqual(found_node.data, 4, "Datele nodului gasit ar trebui sa fie 4.")

    def test_find_non_existing_node(self):
        found_node = self.tree.find(10)
        
        self.assertIsNone(found_node, "Nodul nu exista, deci _find ar trebui sa returneze None.")

if __name__ == '__main__':
    unittest.main()