class LinkedList(object):
    class _Node(object):
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self, values=None):
        self.head = None
        if values:
            while values:
                self.insertFront(values.pop())

    def insertFront(self, val):
        node = self._Node(val)
        temp = self.head
        self.head = node
        node.next = temp

    def deleteFront(self):
        if not self.head:
            raise ValueError("Empty LinkedList")
        self.head = self.head.next

    def returnKthNode(self,k):
        """
        return K-th node, none if exceed.
        """
        ptr = self.head
        while ptr:
            if k == 1:
                return ptr
            ptr = ptr.next
            k -= 1
        return None

    def tranverse(self):
        """
        tranverse and print a linkedlist
        """
        ptr = self.head
        value = []
        while ptr:
            value.append(ptr.val)
            ptr = ptr.next
        print value
