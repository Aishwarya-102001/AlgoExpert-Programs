
#************************ RECURSIVE METHOD ****************************
#**Time --> O(n) --> as we have to traverse through all the nodes till end recursively (n--> total number of elements in binary tree)
#**Space --> O(h) --> as we have to store the stack calls untill the maximum height of tree i.e till end of tree (h--> height of tree)
        
def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

##### code to create binary tree