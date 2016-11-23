"""
Part 1: Discussion Questions

RECURSION

1. In your own words, what is recursion?
> Recursion is having function call itself.

2. Why is it necessary to have a base case?
> It's important to have a base case so Python knows when to stop...
recursing? recursioning? Without a base case, the likely scenario is that
one will encounter "RuntimeError: maximum recursion depth exceeded". For
example:

No, don't do this:

    def add_myself_forever(a):

        print a
        add_myself_forever(a + a)

Better:

    def add_myself(a):

        if a < 5: # finite stopping point (aka base case)
            add_myself(a + 1)
            print a

GRAPHS

1. What is a graph?
> A graph is a data structure; it's very similar to a tree, but has some
distinct differences.

2. How is a graph different from a tree?
> Graphs are different from trees in two main ways: First, graphs can have
loops ("cycles") in them, whereas trees do not. Additionally, trees have
hierarchy built into the structure, but graphs do not. (The closest thing to
hierarchy in graphs would probably be graphs with directed relationships.)

3. Give an example of something that would be good to model with a graph.
> Social networks are great to model with graphs (LinkedIn, Facebook, Twitter,
Instagram, and so on). Each node is a person, and the edge is their connection
to each other. If someone follows or is friends with someone else directly,
they are adjacent to them. A list of one's followers or friends is their
adjacency list.
"""

# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """
    if i == len(my_list): # base case
        return

    print my_list[i]
    print_item(my_list, i + 1)


# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """

    print tree.data
    for child in tree.children:
        print_all_tree_data(child)


# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """

    if not my_list: # base case; my_list is empty
        return 0

    return 1 + list_length(my_list[1:])


# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
        >>> four = Node(4)
        >>> five = Node(5)
        >>> two.add_child(four)
        >>> two.add_child(five)
        >>> num_nodes(one)
        5
        >>> six = Node(6)
        >>> three.add_child(six)
        >>> num_nodes(one)
        6
    """

    if not tree.children:
        return

    return 1 + len(tree.children) + num_nodes(tree.children[0])



#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
