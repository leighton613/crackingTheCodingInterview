from LinkedList import LinkedList
def KthToLast_iter(head, k):
    """
    Iterative solution
    """
    slow = fast = head
    while fast:
        if k == 0:
            break
        fast = fast.next
        k -= 1
    else:
        return None

    while fast:
        fast = fast.next
        slow = slow.next
    return slow.val

def KthToLast_recu(head, k):
    """
    Recursive solution
    """
    if not head:
        return 0
    i = KthToLast_recu(head.next, k) + 1
    if i == k:
        print head.val
    return i

def solution():
    print "2-2 return k-th to last, pls enter linked list value with space to split."
    raw_values = raw_input("values >> ")
    values = [float(i) for i in raw_values.strip().split()]
    k = int(raw_input("k >> "))
    l1 = LinkedList(values)
    l1.tranverse()
    KthToLast_recu(l1.head, k)
    
if __name__ == "__main__":
    solution()
