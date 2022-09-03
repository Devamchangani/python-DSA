from dataclasses import dataclass
from itertools import count
from platform import node
from secrets import choice


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)


    def insert_at_middel(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
        

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print(self):
        itr = self.head
        llstr = ''
    
        while itr:   
            suffix = ''
            if itr.next:
                suffix = '-->'
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

if __name__ == '__main__':
    root = Linkedlist()
    # ===============================first-insert * last-insert * middle-insert * remove =====================================

    # root.insert_at_begining(5)
    # root.insert_at_begining(10)
    # root.insert_at_begining(15)
    # root.insert_at_end(254)
    # root.insert_at_middel(3, 263)
    # root.insert_at_middel(1, 999)
    # root.print()
    # root.remove_at(3)
    # root.remove_at(1)
    # root.print()
    # print(root.get_length())

# =================================== Insert a list ==========================================

    # root.insert_values(["banana", "grapes", "mango", "orange", "apple"])
    # root.insert_at_middel(1, "blueberry")
    # root.print()


    while True:
        print("************************************* SINGLY LINKED LIST *************************************")
        print("1. Insert value at begining")
        print("2. Insert value at end ")
        print("3. Insert Value at middle")
        print("4. Remove value")
        print("5. length of list")
        print("6. Exit")
        choice = int(input("Enter Your choise: "))
        if choice == 1:
                num = 1
                a = int(input("enter your lenght of list : "))
                
                while(num <= a):
                    b = int(input(f"Enter your {num} value : "))
                    root.insert_at_begining(b)
                    num += 1
                root.print()

        elif choice == 2:
                num = 1
                a = int(input("enter your lenght of list : "))
                
                while(num <= a):
                    b = int(input(f"Enter your {num} value : "))
                    root.insert_at_end(b)
                    num += 1
                root.print()
          
        elif choice == 3:
                a = int(input("Enter a position : "))
                b = int(input("Enter a value : "))
                root.insert_at_middel(a, b)
                root.print()
        elif choice == 4:
                a = int(input(" Enter your position :"))
                # b = int(input("Enter your delete value : "))
                root.remove_at(a)
                root.print()
        elif choice == 5:
                print(root.get_length())
        elif choice == 6:
                print("Thanks! Hope you are enjoyed Linked list")
                break
