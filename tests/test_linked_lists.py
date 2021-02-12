"""Linked lists tests."""

# Testing
import unittest

# Data structures
from linked_lists import DoubleLinkList, LinkedList


class TestLinkedList(unittest.TestCase):
    """Linked list test case."""

    def setUp(self):
        self.link_list = LinkedList()
        self.double_link_list = DoubleLinkList()

    def test_insert_values(self):
        """Test insert multiple values."""
        ll = self.link_list
        ll.insert_values(['cat', 'dog', 'snakes'])
        self.assertEqual(ll.get_length(), 3)


    def test_insert_value(self):
        """Test insert 1 value at begining."""
        ll = self.link_list
        ll.insert_at_begining('omar')
        ll.insert_at_begining('dario')
        self.assertEqual(ll.head.data, 'dario')

    def test_inser_value_at_end(self):
        """Test insert element at the end and get last node"""
        ll = self.link_list
        ll.insert_values(['cat', 'dog', 'snakes'])
        ll.insert_at_end('bear')
        self.assertEqual(ll.get_last_node().data, 'bear')


    def test_insert_value_by_index(self):
        """Test insert elements by index and get element by index"""
        ll = self.link_list
        ll.insert_values(['cat', 'dog', 'snakes'])
        ll.insert_at('jose', 1)
        self.assertEqual(ll.get_by_index(1), 'jose')


    def test_get_element_by_value(self):
        """test get element by value."""
        ll = self.link_list
        ll.insert_values(['cat', 'dog', 'snakes'])
        self.assertIsNotNone(ll.get_by_value('cat'))


    def test_remove_element_by_value(self):
        """test remove elements by value."""
        ll = self.link_list
        ll.insert_values(['cat', 'dog', 'snakes'])
        ll.remove_by_value('cat')
        self.assertIsNone(ll.get_by_value('cat'))


    def test_remove_element_by_index(self):
        """test remove elements by index."""
        ll = self.link_list
        ll.insert_values(['cat', 'dog', 'snakes'])
        ll.remove_at(0)
        self.assertNotEqual(ll.get_by_index(0), 'cat')


    def test_link(self):
        """Test the link between elements."""
        ll = self.link_list
        ll.insert_values(['cat', 'dog', 'snakes'])
        self.assertEqual(ll.head.next.data, 'dog')


    def test_double_link(self):
        """Test double link. for double link all tests
        are the same except for this one"""
        ll = self.double_link_list
        ll.insert_values(['cat', 'dog', 'snakes'])
        node = ll.get_by_value('dog')
        self.assertEqual(node.prev.data, 'cat')
        self.assertEqual(node.next.data, 'snakes')


if __name__ == "__main__":
    unittest.main() 