class ListNode:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """
        添加元素
        :param data:
        :return:
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def is_empty(self):
        """
        判断是否为空
        :return:
        """
        if self.head is None:
            return True
        else:
            return False

    def insert(self, index, data):
        """
        插入元素
        :param index:
        :param data:
        :return:
        """
        if self.head is None:
            return "空链表"
        node_index = 0
        node = self.head
        while node_index < index-1:
            node = node.next
            if node is None:
                return "索引大于链表长度"
            node_index += 1
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def remove(self, index):
        """
        删除指定位置元素
        :param index:
        :return:
        """
        if self.head is None:
            return "空链表"
        # 删除头元素
        if index == 0:
            self.head = self.head.next
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        node_index = 0
        node = self.head
        while node_index < index-1:
            node = node_index
            if node is None:
                return "索引大于链表长度"
            node_index += 1
        node.next = node.next.next
        if node.next is None:
            self.tail = node

    def size(self):
        """
        链表长度
        :return:
        """
        node = self.head
        node_index = 0
        while node is None:
            node = node.next
            node_index += 1
        return node_index

    def search(self, data):
        """
        查询元素是否存在
        :param data:
        :return:
        """
        node = self.head
        node_index = 0
        while node is None:
            if node.data == data:
                return True
            node = node.next
            node_index += 1
        return False


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
