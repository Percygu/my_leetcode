class Node(object):
    def __init__(self,key = None,val=None):
        self.pre = None
        self.next = None

class LruCache():
    def __init__(self,cap):
        self.cap = cap
        self.hash_map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    # 将节点移动到链表尾部
    def mov_node(self,key):
        if key not in self.hash_map:
            return
        node = self.hash_map[key]
        node.pre.next = node.next
        node.next.pre = node.pre
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node

    def get(self,key):
        if key not in self.hash_map:
            return -1
        self.mov_node(key)
        return self.hash_map[key].val

    def del_node(self):
        self.head.next.next.pre = self.head
        self.head.next = self.head.next.next

    def put(self,key,val):
        if key in self.hash_map:
            self.hash_map[key].val = val
            self.mov_node(key)
        if len(self.hash_map) >= self.cap:
            self.hash_map.pop(key)
        node = Node(key,val)
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node





