class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
n1=Node(3)
n2=Node(2)
n3=Node(5)
n4=Node(8)
n5=Node(9)


n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

head=n1
curr=head

while curr:
    print(curr.data,end='->')
    curr=curr.next
print("None")    


print("deletion of 3rd node")
curr=head
for i in range(1):
    curr=curr.next
curr.next=curr.next.next    

curr=head

while curr:
    print(curr.data,end='->')
    curr=curr.next
print("None")  
  
  
  
  helklo

