
#************************ RECURSIVE METHOD ****************************
#**Time --> O(n) --> as we call the functions at every leaf node recursively (n--> total number of elements in binary tree)
#**Space --> O(n) --> as it uses totally (n/2) recursive calls in stack..... O(n/2) ~> O(n)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
            if i >= len(values):
                return
            queue = [self]
            while len(queue) > 0:
                current = queue.pop(0)
                if current.left is None:
                    current.left = BinaryTree(values[i])
                    break
                queue.append(current.left)
                if current.right is None:
                    current.right = BinaryTree(values[i])
                    break
                queue.append(current.right)
            self.insert(values, i + 1)
            return self

#**ORIGINAL CODE SOLUTION**
def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)

tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
print (branchSums(tree))