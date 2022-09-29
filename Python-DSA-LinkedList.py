class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
                    
    
    def insert_values(self, data_values):
        self.head = None
        for data in data_values:
            self.insert_at_end(data)
    
    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr= itr.next
        print(llstr,'NONE')
        
    def get_length(self):
        count =0;
        itr = self.head
        while itr:
            count+=1;
            itr = itr.next
        return count
    
    def remove_at(self,idx):
        if idx < 0 or idx >= self.get_length():
            raise Exception("Invalid Index")
        
        if idx == 0:
            self.head = self.head.next
        
        count = 0
        itr = self.head
        
        while itr:
            count+=1
            if(count == idx):
                itr.next = itr.next.next
                break
            itr= itr.next
    
    def insert_at(self,idx,data):
        if idx < 0 or idx >= self.get_length():
            raise Exception("Invalid Index")
        
        if idx == 0:
            self.insert_at_begining(data)
        
        count = 0
        itr = self.head
        while itr:
            count+=1
            if(count == idx):
                tmp = Node(data,itr.next)
                itr.next=tmp
                break;
            itr=itr.next
            
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([3,4,56,6,123,4,123,3])
    ll.print()
    print(ll.get_length())
    ll.remove_at(3)
    ll.insert_at(2,1)
    ll.print()
