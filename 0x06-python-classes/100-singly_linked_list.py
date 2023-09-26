#!/usr/bin/python3

"""Singly linked list module"""


class Node:
    """Node class"""

    def __get_data(self):
        """data getter"""
        return (self.__data)

    def __set_data(self, data):
        """data setter"""
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

    data = property(__get_data, __set_data)

    def __get_next(self):
        """next node getter"""
        return (self.__next)

    def __set_next(self,  next_node):
        """next node setter"""
        if type(next_node) is Node or next_node is None:
            self.__next = next_node
        else:
            raise TypeError("next_node must be a Node object")

    next_node = property(__get_next, __set_next)

    def __init__(self, data, next_node=None):
        """constuctor of the class"""
        self.__set_data(data)
        self.__set_next(next_node)


class SinglyLinkedList:
    """Singly lincked list class"""

    def __init__(self):
        """constructor of the class"""
        self.__head = None

    def __str__(self):
        """string representation"""
        r = ""
        current = self.__head

        while (current):
            r += str(current.data)
            r += "\n"
            current = current.next

        r = r[:-1]
        return (r)

    def sorted_insert(self, value):
        """insert to the list"""
        current = self.__head

        if (current is None) or (value < current.data):
            node = Node(value)
            node.next = self.__head
            self.__head = node
            return

        while (current and current.next and value > current.next.data):
            current = current.next

        node = Node(value)
        node.next = current.next
        current.next = node
