"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere
in the "right partition"; it does not need to appear between the left and right partitions.

EXAMPLE
Input:  3   -> 5    -> 8   -> 5      -> 10   -> 2 -> 1      [partition=5]
Output: 3   -> 1    -> 2   -> 10     -> 5    -> 5 -> 8
"""


def partition(ll, x):
    current = ll.tail = ll.head
    while current:
        next_node = current.next
        current.next = None  # detach current node because it will be moved in one of the two partitions
        if current.value < x:
            # left partition
            current.next = ll.head  # attach next element to head
            ll.head = current  # the element becomes the head
        else:
            ll.tail.next = current  # attach to tail
            ll.tail = current  # the element becomes the head
        current = next_node  # IMPORTANT: keep the original "order" to successfully loop all the elements of the ll

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None
