"""
Perfect binary tree:
                       1
               ________|________
              |                 |
              2                 3
          ____|____         ____|____
         |         |       |         |
         4         5       6         7
       __|__     __|__   __|__     __|__
      |     |   |     | |     |   |     |
      8     9   10   11 12   13   14    15
"""

from traversals import Node, post_order_traversal

def main() -> None:
    """Print the nodes of a perfect binary tree."""
    tree = Node(1,
                Node(2,
                     Node(4, Node(8), Node(9)),
                     Node(5, Node(10), Node(11))),
                Node(3,
                     Node(6, Node(12), Node(13)),
                     Node(7, Node(14), Node(15))))
    post_order_traversal(tree)

if __name__ == '__main__':
    main()
