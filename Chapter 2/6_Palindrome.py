from LinkedList import LinkedList

def is_palindome(ll):
    ls = []
    p = ll.head
    while p:
        ls.append(p.value)
        p = p.next
    ls2 = ls[::]
    ls.reverse()
    return ls2 == ls

ll = LinkedList([1,2,3,4,3,2,1])
print(is_palindome(ll), " = True")

ll = LinkedList([1,2,3,4,5,5,3])
print(is_palindome(ll), " = False")
