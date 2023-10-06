"""
  reverse alternate nodes and append at the end
  The input list will have at least one element
  Node is defined as
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def rearrange(self, head):
        # Code here
        if not head or not head.next:
            return head
    
        original_head = head
        extracted_head = head.next
        original_current = original_head
        extracted_current = extracted_head
    
        # Extract alternative nodes
        while original_current and extracted_current:
            original_current.next = extracted_current.next
            original_current = original_current.next
            if original_current:
                extracted_current.next = original_current.next
                extracted_current = extracted_current.next
    
        # Reverse the extracted list
        prev = None
        curr = extracted_head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        extracted_head = prev
    
        # Append the extracted list to the original list
        original_current = original_head
        while original_current and original_current.next:
            original_current = original_current.next
        original_current.next = extracted_head
    
        return original_head
    
    
#{ 
 # Driver Code Starts
# Node Class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class contains node object
class LinkedList:
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Code execution starts here
if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
            
        Solution().rearrange(llist.head)
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa
#     } Driver Code Ends 