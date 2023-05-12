class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head1 = head
        arr = []

        if k == 0 or head is None:
            return head

        while head1 is not None:
            arr.append(head1.val)
            head1 = head1.next

        if k > len(arr):
            k = k%len(arr) 

        for i in range(k):
            arr = arr[len(arr)-1:] + arr[:len(arr)-1]

        head2 = head
        i = 0
        while head2 is not None:
            head2.val = arr[i]
            head2 = head2.next
            i += 1

        return head
