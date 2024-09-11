# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous

# Function to print the linked list
def printList(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Main function to test reverseList
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original List:")
    printList(head)

    # Reversing the linked list
    solution = Solution()
    reversed_head = solution.reverseList(head)

    print("Reversed List:")
    printList(reversed_head)
