from LinkedList import LinkedList, LinkedListNode

def intersection(ll_1, ll_2):
    p1, p2 = ll_1.head, ll_2.head
    nodes = set()
    while p1:
        nodes.add(p1)
        p1 = p1.next
    while p2:
        if p2 in nodes:
            return p2
        else:
            p2 = p2.next
    return False


ll_1 = LinkedList([1,2,3])
ll_2 = LinkedList([1,2])

intersect = LinkedListNode(4)
ll_1.tail.next = intersect
ll_1.tail = ll_1.tail.next
ll_2.tail.next = intersect
ll_2.tail = ll_2.tail.next
ll_1.add_multiple([5,6,7])

print(ll_1)
print(ll_2)
print(intersection(ll_1, ll_2))
# print(ll_1.head.next.next.next == ll_2.head.next.next)