from linked_list import LinkedList


def sum_lists(l1, l2):
    curr_1 = l1.head
    curr_2 = l2.head

    remainder = 0

    while curr_1 and curr_2:
        part_sum = (curr_1.value + curr_2.value)
        curr_1.value = part_sum % 10 + remainder
        remainder = part_sum // 10

        curr_1 = curr_1.next
        curr_2 = curr_2.next

    l2.tail = curr_1.next
    return l1.head


def example():
    ll_a = LinkedList.generate(4, 0, 9)
    ll_b = LinkedList.generate(3, 0, 9)
    print(ll_a)
    print(ll_b)
    current = sum_lists(ll_a, ll_b)
    while current:
        print(current)
        current = current.next

    # print(sum_lists_followup(ll_a, ll_b))


if __name__ == "__main__":
    example()
