from LinkedList import LinkedList

def partition(ll, value):
    start = ll.head
    while start.next is not None:
        if start.next.value >= value:
            start = start.next
        else:
            ll.add_to_beginning(start.next.value)
            start.next = start.next.next


ll = LinkedList().generate(20, 1,100)
print(ll)

value = ll.head.value
partition(ll, value)
print(ll)
