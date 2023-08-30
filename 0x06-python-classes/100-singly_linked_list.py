#!/usr/bin/python3
"""A class called 'Node'of a singly linked list"""


class Node:
    """A node in singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data : The value of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linkedlist"""

    def __str__(self):
        """Print singly list"""
        ret = ""
        ptrnode = self.__head

        while ptrnode is not None:
            ret += str(ptrnode.data)
            if ptrnode.next_node is not None:
                ret += "\n"
            ptrnode = ptrnode.next_node

        return ret

    def __init__(self):
        """Initialize a new singly list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new node to list
        Args:
            value (Node): The new Node to insert.
        """
        ptrnode = self.__head

        while ptrnode is not None:
            if ptrnode.data > value:
                break
            ptrprev = ptrnode
            ptrnode = ptrnode.next_node

        new = Node(value, ptrnode)
        if ptrnode == self.__head:
            self.__head = new
        else:
            ptrprev.next_node = new
