from LinkedList import LinkedList, LinkedListNode

def loop_detection(ll):
    p = ll.head
    nodes = set()
    while p:
        if p in nodes:
            return p
        else:
            nodes.add(p)
            p = p.next
    return False


ll = LinkedList([1,2,3])

loop_node = LinkedListNode(4)
ll.tail.next = loop_node
ll.tail = ll.tail.next

ll.add_multiple([5,6,7])
ll.tail.next = loop_node
ll.tail = ll.tail.next

print(loop_detection(ll))
# print(ll_1.head.next.next.next == ll_2.head.next.next)