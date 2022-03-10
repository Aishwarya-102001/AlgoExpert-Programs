
#** Algorithm of Question ***********
#** Time = O(N) --> as we traverse through the entire linked list once
#** Space = O(1) --> as we are modifying the linked list in place 
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
        
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next
        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
    return linkedList
