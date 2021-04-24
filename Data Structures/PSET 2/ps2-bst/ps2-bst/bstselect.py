import bstsize

class BST(bstsize.BST):
    """
    Adds select method to BST, starting with code from bstsize.   
    """
    
    def select(self, index):
        """
        Takes a 1-based index, and returns the element at that index,
        or None if the index is out-of-bounds. Starting at the root,
        the tree is searched by examining the size of the left-child
        tree, which gives the number of elements smaller than the
        current node.
        """
        node = self.root
        while node is not None:
            leftSize = bstsize.size(node.left) + 1  # size of the left subtree
                                                    # add 1 to account for our 1 based index
            if index == leftSize:   # if our index matches the size of the subtree containing
                return node         # elements smaller than our current node we have found the element
            if index < leftSize:    # if our index is smaller than the size of the subtree
                node = node.left    # containing smaller elements, we traverse left since our element
            else:                   # must be among those smaller indices
                index = (index - leftSize)  # if our index is greater than leftSize we traverse
                node = node.right           # right but remove leftSize from our index to look
        return node                         # at the right subtree as its very own array
