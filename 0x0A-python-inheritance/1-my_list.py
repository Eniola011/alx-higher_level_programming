#!/usr/bin/python3
"""

MyList Module

"""


class MyList(list):
    """ A class that inherits from list
    Args:
        list: list
    """

    def print_sorted(self):
        """ Public Instance Method:
            Prints the list, but sorted (ascending sort)
        """

        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
