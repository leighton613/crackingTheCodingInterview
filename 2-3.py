from LinkedList import LinkedList
def deleteMiddleNode(node):
    """
    node: is guaranteed to be in the middle
    """
    nxt = node.next # guaranteed to exist
    while nxt.next:
        node.val = nxt.val
        node = node.next
        nxt = nxt.next
    node.val = nxt.val
    node.next = None

def solution():
    print "2-3 delete middle node, pls enter linked list values. Enter for default"
    raw_values = raw_input("values >> ")
    if raw_values.strip() == "":
        values = [1,2,3,4,5,6,7,8,9,10]
    else:
        values = [float(i) for i in raw_values.strip().split()]
    l1 = LinkedList(values)
    l1.tranverse()
    print "Please enter 1 < c < 10 as the middle node number:"
    c = int(raw_input("c >> "))
    c_node = l1.returnKthNode(c)
    deleteMiddleNode(c_node)
    l1.tranverse()

if __name__ == "__main__":
    solution()
