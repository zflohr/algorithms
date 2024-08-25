"""
Perfect binary tree:
                                     1
                       ______________|______________
                      |                             |
                      2                             3
              ________|_______               _______|________
             |                |             |                |
             4                5             6                7
          ___|___          ___|___       ___|___          ___|___
         |       |        |       |     |       |        |       |
         8       9        10      11    12      13       14      15
        _|_     _|_      _|_     _|_   _|_     _|_      _|_     _|_
       |   |   |   |    |   |   |   | |   |   |   |    |   |   |   |
       16  17  18  19   20  21  22 23 24  25  26  27   28  29  30  31
"""

from traversals import Node, pre_order_traversal, post_order_traversal

def main() -> None:
    """Print the nodes of a perfect binary tree."""
    tree = Node(1,
                Node(2,
                     Node(4,
                          Node(8, Node(16), Node(17)),
                          Node(9, Node(18), Node(19))),
                     Node(5,
                          Node(10, Node(20), Node(21)),
                          Node(11, Node(22), Node(23)))),
                Node(3,
                     Node(6,
                          Node(12, Node(24), Node(25)),
                          Node(13, Node(26), Node(27))),
                     Node(7,
                          Node(14, Node(28), Node(29)),
                          Node(15, Node(30), Node(31)))))
    print('pre-order traversal:')
    pre_order_traversal(tree)
    print('\npost-order traversal:')
    post_order_traversal(tree)

if __name__ == '__main__':
    main()
