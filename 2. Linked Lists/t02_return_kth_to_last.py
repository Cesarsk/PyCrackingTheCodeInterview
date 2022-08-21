from linked_list import LinkedList


# O(N) time complexity
def kth_to_last(ll, k):
    p1 = p2 = ll.head
    count = 0

    while p1:
        if count >= k:
            p2 = p2.next

        count += 1
        p1 = p1.next

    return p2


# O(N) space
def kth_last_recursive(ll, k):
    head = ll.head
    counter = 0

    def helper(head, k):
        nonlocal counter
        if not head:
            return None
        helper_node = helper(head.next, k)
        # this increases only from the end of the linked list and starts to count...
        counter = counter + 1
        if counter == k:
            # when found the k-th last element, returns the head
            return head
        return helper_node

    return helper(head, k)


test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)


def test_kth_to_last():
    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        assert kth_to_last(ll, k).value == expected
        assert kth_last_recursive(ll, k).value == expected


if __name__ == "__main__":
    test_kth_to_last()
