from LinkedList import LinkedList


def remove_dups(ll):
    seen = set()
    seen.add(ll.head.value)
    p = ll.head

    while p.next is not None:
        if p.next.value in seen:
            p.next = p.next.next
        else:
            seen.add(p.next.value)
            p = p.next

def remove_dups_follow_up(ll):
    p1 = p2 = ll.head

    while p1 is not None:
        if p2.next.value == p1.value:
            p2.next = p2.next.next
        else:
            p2 = p2.next
        if p2.next is None:
            p1 = p2 = p1.next


ll = LinkedList().generate(n=40)
print(ll)
remove_dups(ll)
print(ll)

print()

ll = LinkedList().generate(n=40)
print(ll)
remove_dups_follow_up(ll)
print(ll)
