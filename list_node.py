class ListNode:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """
        判断是否为空
        :return:
        """
        if self.head is None:
            return True
        else:
            return False

    def append(self, val):
        """
        末尾添加元素
        :param val:
        :return:
        """
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def iter(self):
        """
        遍历，生成一个生成器
        :return:
        """
        if self.head is Node:
            return
        node = self.head
        yield node.val
        while node.next is not None:
            node = node.next
            yield node.val

    def index(self, index, value):
        """
        指定位置插入元素
        :param index:
        :param value:
        :return:
        """
        node = self.head
        node_index = 0
        if node is None:
            return "空链表"
        # 获取前一个元素
        while node_index < index - 1:
            node = node.next
            if node is None:
                return "索引大于链表长度"
            node_index += 1
        # 创建新节点
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        if new_node.next is Node:
            self.tail = new_node

    def remove(self, index):
        """
        删除元素
        :param index:
        :return:
        """
        node = self.head
        node_index = 0
        if node is None:
            return "空链表"
        # 删除头节点时
        if index == 0:
            self.head = node.next
            return
        # 链表只有一个节点时
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        # 获取前一个元素
        while node_index < index-1:
            node = node.next
            if node is None:
                return "索引大于链表长度"
            node_index += 1
        # 上个元素的next指向下个元素
        node.next = node.next.next
        if node.next is None:  # 删除最后一个节点时，tail设置为前一个元素
            self.tail = node

    def size(self):
        """
        返回元素个数
        :return:
        """
        node = self.head
        node_index = 0
        # 获取前一个元素
        while node is not None:
            node = node.next
            node_index += 1
        return node_index

    def __str__(self):
        """
        打印输出
        :return:
        """
        value = ""
        node = self.head
        # 获取前一个元素
        while node is not None:
            value += "{}{}".format(str(node.val), "-->")
            node = node.next
        return value

    def search(self, value):
        """
        搜索元素，返回True和False
        :param value:
        :return:
        """
        node = self.head
        found = False
        # 获取前一个元素
        while node is not None and not found:
            if node.val == value:
                found = True
            node = node.next
        return found


class Node:
    """
    节点类
    """

    def __init__(self, val):
        self.val = val
        self.next = None


if __name__ == '__main__':
    list_node_1 = ListNode()
    a = list_node_1.is_empty()
    print(a)
    list_node_1.append(10)
    list_node_1.append(20)
    for i in list_node_1.iter():
        print(i)
    print("-"*20)
    list_node_1.index(1, "你好")
    print(list_node_1)
    for i in list_node_1.iter():
        print(i)
    print("-"*20)
    list_node_1.remove(0)
    for i in list_node_1.iter():
        print(i)
    print("-"*20)
    print(list_node_1.size())
    print(list_node_1)
    print(list_node_1.search("你好"))
    print(list_node_1.search("不好"))
