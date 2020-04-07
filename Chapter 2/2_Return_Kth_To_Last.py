from LinkedList import LinkedList

def return_kth_to_last(ll, kth):
    needed = len(ll) - kth
    p = ll.head
    for _ in range(needed):
        p = p.next
    return p.value


ll = LinkedList().generate(12, 0, 100)
print(ll)
print(return_kth_to_last(ll, 2))