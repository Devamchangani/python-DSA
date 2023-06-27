#User function Template for python3

class Solution:
    def union(self, head1,head2):
        vec = []
        mp = {}
        it = head1
        while it:
            if it.data not in mp:
                vec.append(it.data)
            mp[it.data] = mp.get(it.data,0) + 1
            it = it.next
        it = head2
        while it:
            if it.data not in mp:
                vec.append(it.data)
            mp[it.data] = mp.get(it.data, 0) + 1
            it = it.next
        vec.sort()
        head = Node(vec[0])
        tail = head
        for i in range(1, len(vec)):
            newnode = Node(vec[i])
            tail.next = newnode
            tail = newnode
        return head



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    for _ in range(int(input(""))):
        
        n1 = int(input("Enter a first LL Total no: "))
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        n2 = int(input("Enter a second LL Total no: "))
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        ob = Solution()
        printList(ob.union(ll1.head,ll2.head))
        print()

# } Driver Code Ends