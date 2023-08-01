class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        vec = []
        it = head

# USING A IF ELSE CONDITIONS CREATE 0'S,  1'S,  2'S FORMAT LIST 
        # while it:
        #     if it.data == 0:
        #         vec.insert(0,it.data)
        #     elif it.data == 2:
        #         vec.append(2)
        #     elif it.data == 1:
        #         if len(vec) == 0:
        #             vec.append(1)
        #         else:
        #             for i in range(len(vec)):
        #                 if(vec[i] == 0):
        #                     continue
        #                 else:
        #                     vec.insert(i,it.data)
        #                     break
        #     else:
        #         continue
        #     it = it.next


# USIN DIRECT SORT FUNCTION
        while it:
            vec.append(it.data)
            it = it.next
        vec.sort()
        print(vec)


# INSERT LIST IN LL
        head = Node(vec[0])
        tail = head
        for i in range(1, len(vec)):
            newnode = Node(vec[i])
            tail.next = newnode
            tail = newnode

        return head



# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        
# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print()

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        printList(Solution().segregate(a.head))
# } Driver Code Ends