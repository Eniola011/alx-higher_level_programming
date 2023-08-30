#!/usr/bin/python3
"""A class called 'Node'of a singly linked list"""


class Node:
    def __init__(self, data, next_node=None):
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
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tempnode = self.__head
            while (tempnode.next_node is not None and
                    tempnode.next_node.data < value):
                tempnode = tempnode.next_node
            new_node.next_node = tempnode.next_node
            tempnode.next_node = new_node

    def __str__(self):
        val = []
        temp = self.__head
        while temp is not None:
            val.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(val))
