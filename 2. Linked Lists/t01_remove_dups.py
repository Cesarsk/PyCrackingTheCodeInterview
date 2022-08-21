from linked_list import LinkedList


# This takes O(n) in time and O(n) in space
def remove_dups(ll):
    datas = set()
    current = ll.head
    previous = None

    while current:
        if current.value in datas:
            # remove the node
            previous.next = current.next
        else:
            datas.add(current.value)
            previous = current

        # jump to next element
        current = current.next

    ll.tail = previous
    return ll


# This takes O(n^2) in time and O(1) in space since there's no need of the buffer
def remove_dups_follow_up(ll):
    slow = fast = ll.head

    while slow:
        fast = slow
        while fast.next:
            if fast.next.value == slow.value:
                fast.next = fast.next.next
            else:
                fast = fast.next
        slow = slow.next

    ll.tail = fast  # set the tail
    return ll


# generating the list
ll = LinkedList.generate(k=5, min_value=0, max_value=3)
print(ll)
remove_dups_follow_up(ll)
print(ll)
