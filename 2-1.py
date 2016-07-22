from LinkedList import LinkedList
def removeDups(head):
    if not head or not head.next:
        return head
    prev, curr = head, head.next
    mapping = {head.val: 1}
    while curr:
        if mapping.get(curr.val,0) == 1:
            prev.next = curr.next
            curr = curr.next
        elif mapping.get(curr.val, 0) == 0: # first time
            mapping[curr.val] = 1
            prev = curr
            curr = curr.next
        else:
            raise ValueError("mapping value > 1")

def solution():
    print "2-1 Remove dups. Pls enter linked list values, split by single space."
    raw_values = raw_input("values >> ")
    values = [float(val) for val in raw_values.strip().split()]
    l1 = LinkedList(values)
    l1.tranverse()
    removeDups(l1.head)
    l1.tranverse()

if __name__ == "__main__":
    solution()
