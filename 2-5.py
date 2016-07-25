from LinkedList import LinkedList
def sumLists(head1, head2):
    l3 = LinkedList()
    if not head1 and not head2:
        return l3.head
    if not head1 and head2:
        return head2
    if not head2 and head1:
        return head1

    # both not empty
    ptr1 = head1
    ptr2 = head2
    temp = 0
    while ptr1 and ptr2:
        l3.append((ptr1.val + ptr2.val) % 10 + temp)
        temp = (ptr1.val + ptr2.val) // 10
        ptr1, ptr2 = ptr1.next, ptr2.next
    if not ptr1 and not ptr2:
        return l3.head
    if ptr1:
        ptr = ptr1
    else:
        ptr = ptr2
    l3.append(ptr.val + temp)
    ptr = ptr.next
    while ptr:
        l3.append(ptr.val)
        ptr = ptr.next
    return l3

def solution():
    print "2-5 sum lists."
    l1 = LinkedList([8,6,4,2])
    l2 = LinkedList([4,5,7,9,2,4,6,8])
    l1.tranverse()
    l2.tranverse()
    l3 = sumLists(l1.head, l2.head)
    l3.tranverse()

if __name__ == "__main__":
    solution()
