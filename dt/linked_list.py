class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def insert_at_beginning(self, data):
        node = Node(data, self.head) # next = self.head
        self.head = node


    def printList(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        liststr = ''

        while itr:
            liststr += str(itr.data) + ' --> '
            itr = itr.next

        print(liststr)


    def insert_at_tail(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_tail(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            return Exception("Invalid index")

        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_at(self, index, data):
        if index<0 or index > self.get_length():
            return Exception("Invalid index")

        elif index==0:
            node = Node(data, self.head.next)
            self.head.next = node

        else:
            itr = self.head
            count = 0
            while itr:
                print(itr.data)

                if count == index-1:
                    node = Node(data, itr.next)
                    itr.next = node
                itr = itr.next
                count+=1

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_tail(99)
    ll.insert_at(2, 3)
    ll.insert_at(1, 1)
    ll.printList()