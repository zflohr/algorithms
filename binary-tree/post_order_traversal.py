class Node:
    """A node of a perfect binary tree.

    Public attributes:
        data: The value at a node.
        left: A reference to a node's left subtree.
        right: A reference to a node's right subtree.
    """

    def __init__(self, data: int | None = None, left: 'Node | None' = None,
                 right: 'Node | None' = None) -> None:
        """Initialize a node.

        Args:
            data: The value at a node.
            left: A reference to a node's left subtree.
            right: A reference to a node's right subtree.
        """
        self.data = data
        self.left = left
        self.right = right

def print_post_order_traversal(node: Node) -> None:
    """Print node values in a post-order traversal of a binary tree.

    Args:
        node: A node of a perfect binary tree.
    """
    if not node:
        return
    print_post_order_traversal(node.left)
    print_post_order_traversal(node.right)
    print(node.data)
