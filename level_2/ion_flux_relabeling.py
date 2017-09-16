"""
Ion Flux Relabeling
===================

Oh no! Commander Lambda's latest experiment to improve the efficiency of her LAMBCHOP doomsday device has backfired spectacularly. She had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. She's having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly - quickly enough, perhaps, to earn a promotion!

Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label them, she performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:

   7
 3   6
1 2 4 5

Write a function answer(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter.  For example, answer(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth.  The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) h = 3
    (int list) q = [7, 3, 5, 1]
Output:
    (int list) [-1, 7, 6, 3]

Inputs:
    (int) h = 5
    (int list) q = [19, 14, 28]
Output:
    (int list) [21, 15, 29]

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""
import collections


def answer(h, q):

    def get_max_label(height):
        return 2 ** height - 1

    q_s = sorted([el for el in q if el < get_max_label(h)], reverse=True)
    mapping = collections.defaultdict(lambda: -1)

    class Node(object):

        left_child = None
        right_child = None
        label = None

        def __init__(self, label, parent):
            self.label = label
            if label in q_s:
                q_s.remove(label)
                mapping[label] = parent.get_label() if parent else -1

        def get_label(self):
            return self.label

        def set_left_child(self, node):
            self.left_child = node
            return node.get_label() - 1

        def set_right_child(self, node):
            self.right_child = node
            return node.get_label() - 1

    def build_and_traverse_tree(node, height, label):
        if height > 0:  # stop if we are on the bottom
            label_right = label - 1
            label_left = label_right - get_max_label(height)
            node.set_right_child(Node(label_right, node))
            node.set_left_child(Node(label_left, node))
            if len(q_s) == 0:  # we're finished
                return
            if label_left < q_s[0] < label_right:
                build_and_traverse_tree(node.right_child, height - 1, label_right)
            if label_left - get_max_label(height) < q_s[0] < label_left:
                build_and_traverse_tree(node.left_child, height - 1, label_left)
            return
        else:  # we're on the bottom, so just go back up
            return

    root_node = Node(get_max_label(h), None)
    build_and_traverse_tree(root_node, h - 1, root_node.get_label())
    result = []
    for el in q:
        result += [mapping[el]]
    return result
