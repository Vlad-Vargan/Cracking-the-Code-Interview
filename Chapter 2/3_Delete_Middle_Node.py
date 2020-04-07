from LinkedList import LinkedList

def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


ll = LinkedList([1,2,3,4])
middle = ll.add(5)
ll.add_multiple([6,7,8,9])
print(ll)
delete_middle_node(middle)
print(ll)