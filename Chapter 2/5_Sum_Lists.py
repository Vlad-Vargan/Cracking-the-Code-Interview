from LinkedList import LinkedList

"""EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. 
Output: 2 -> 1 -> 9. That is, 912."""

def sum_lists(ll_1, ll_2):
    ll = LinkedList()
    p1, p2 = ll_1.head, ll_2.head
    residue = False
    while p1 or p2:
        if p1 and p2:
            first_sum = p1.value + p2.value + residue
            ll.add(first_sum % 10)
            residue = first_sum//10
        elif p1:
            ll.add(p1.value+residue)
            p1 = p1.next
            continue
        elif p2:
            ll.add(p2.value+residue)
            p2 = p2.next
            continue
        p1, p2 = p1.next, p2.next
        if p1 is None and p2 is None:
            if residue:
                ll.add(1)
    return ll

def sum_lists_follow_up(ll_1, ll_2):
    ll = LinkedList()
    sum_1, sum_2 = 0, 0
    p1, p2 = ll_1.head, ll_2.head

    while p1 or p2:
        if p1:
            sum_1 += p1.value
            p1 = p1.next
            if p1:
                sum_1 *= 10
        if p2:
            sum_2 += p2.value
            p2 = p2.next
            if p2:
                sum_2 *= 10
    sum_0 = sum_1 + sum_2
    while sum_0 > 10:
        ll.add_to_beginning(sum_0 % 10)
        sum_0 = sum_0//10
    ll.add_to_beginning(sum_0)
    return ll



ll_1 = LinkedList([7,1,6])
ll_2 = LinkedList([5,9,2])

print(ll_1)
print(ll_2)
print(sum_lists(ll_1, ll_2))
print()
print(ll_1)
print(ll_2)
print(sum_lists_follow_up(ll_1, ll_2))