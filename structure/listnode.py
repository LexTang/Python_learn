class Node:
    def __init__(self, val, idx=None):
        self.val = val
        self.next = idx


class ListNode:
    def __init__(self):
        self.head = None

    # 插入节点到链表末尾
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # 插入节点到链表头部
    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    # 删除第一个匹配值的节点
    def delete(self, val):
        if not self.head:
            return

        if self.head.value == val:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == val:
                current.next = current.next.next
                return
            current = current.next

    # 打印链表内容
    def print_list(self):
        current = self.head
        while current:
            print(current.val, end="----")
            current = current.next
        print("None")


if __name__ == '__main__':
    # 创建链表
    my_list = ListNode()
    # 插入节点到链表末尾
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    # 打印链表：1 -> 2 -> 3 -> None
    my_list.print_list()
