from LinkedList import LinkedList
def partition(head, value):
    """
    similar to partition in quick sort
    """
    ptr = head
    while ptr:
        if ptr.val == value:
            head.val, ptr.val = ptr.val, head.val
            break
        ptr = ptr.next
    else:
        raise ValueError("No node with value existed")

    i, j = head, head.next
    while j:
        if j.val < head.val:
            i = i.next
            i.val, j.val = j.val, i.val
        j = j.next
    i.val, head.val = head.val, i.val

def solution():
    print "2-4 Partition."
    raw_values = raw_input("values >> ")
    if raw_values.strip() == "":
        values = [3,5,8,5,10,2,1]
    else:
        values = [float(i) for i in raw_values.strip().split()]
    l1 = LinkedList(values)
    l1.tranverse()
    val = float(raw_input("select a value >> "))
    partition(l1.head, val)
    l1.tranverse()

if __name__ == "__main__":
    solution()
