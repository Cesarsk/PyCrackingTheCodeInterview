from linked_list import LinkedList


def intersection(list1, list2):
    # if tail is not available it's possible to scroll both list and check the final node
    if list1.tail is not list2.tail:
        return False

    # if len is not available it's possible to scroll the list and count the elements
    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list2) < len(list1) else list1

    # cut away the node so that both list have the same length
    diff = len(longer) - len(shorter)
    shorter_node, longer_node = shorter.head, longer.head

    for _ in range(diff):
        longer_node = longer_node.next

    # find the intersection node
    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node  # or shorter_node

def test_linked_list_intersection():
    shared = LinkedList()
    shared.add_multiple([1, 2, 3, 4])

    a = LinkedList([10, 11, 12, 13, 14, 15])
    b = LinkedList([20, 21, 22])

    a.tail.next = shared.head
    a.tail = shared.tail
    b.tail.next = shared.head
    b.tail = shared.tail

    # should be 1
    assert intersection(a, b).value == 1
