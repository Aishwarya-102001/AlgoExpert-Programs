
#************************ RECURSIVE METHOD ****************************
#********** AVERAGE CASE :------
#**Time --> O(log(n)) --> as we can ultimately eliminate half the subtree in BST (n--> total number of elements in array)
#**Space --> O(log(n)) --> as we can ultimately eliminate half the subtree in BST

#********** WORST CASE :------
#**Time --> O(n) --> if we consider and traverse at most all the nodes(n--> total number of elements in array)
#**Space --> O(n)

# def findClosestValueInBst(tree,target):
#     return findClosestValueInBstHelper(tree, target, float("inf"))

# def findClosestValueInBstHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     if target < tree.value:
#         return findClosestValueInBstHelper(tree.left, target, closest)
#     elif target > tree.value:
#         return findClosestValueInBstHelper(tree.right, target, closest)
#     else:
#         return closest
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# root = BST(10)
# root.left = BST(5)
# root.left.left = BST(2)
# root.left.left.left = BST(1)
# root.left.right = BST(5)
# root.right = BST(15)
# root.right.left = BST(13)
# root.right.left.right = BST(14)
# root.right.right = BST(22)

# expected = 13
# print("Closest value expected:", expected)

# print ("Closest value found:", findClosestValueInBst(root, 12))

#************************ ITERATIVE MTETHOD ****************************
#********** AVERAGE CASE :------
#**Time --> O(log(n)) --> as we can ultimately eliminate half the subtree in BST (n--> total number of elements in array)
#**Space --> O(1) --> as we don't use any additional space as in recursive call stack

#********** WORST CASE :------
#**Time --> O(n) --> if we consider and traverse at most all the nodes(n--> total number of elements in array)
#**Space --> O(1) -->as we don't use any additional space as in recursive call stack

def findClosestValueInBst(tree,target):
        return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

expected = 13
print("Closest value expected:", expected)

print ("Closest value found:", findClosestValueInBst(root, 12))
