class LinkedList:
    def __init__(self, head):
        self.head = head

    def insert(self, node):
        node.next = self.head
        self.head = node

    def delete_node(self, data):
            if self.head:
                if self.head.data == data:
                    if self.head.next:
                        self.head = self.head.next
                    else:
                        self.head = None
                else:
                    cur_node = self.head
                    while cur_node.next is not None:
                        
                        if cur_node.next.data == data:
