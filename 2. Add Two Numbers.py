class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tail1 = l1
        tail2 = l2
        head = tail =ListNode(0)
        saved=0
        while(tail1 !=None or tail2 !=None):
            val=0
            val += tail1.val if tail1 !=None else 0
            val += tail2.val if tail2 !=None else 0
            val += saved
            print(val)
            tail.next=ListNode(int(str(val)[-1]))
            saved = 0 if val<10 else 1
            if tail1 !=None:tail1 = tail1.next
            if tail2 !=None:tail2 = tail2.next
            tail = tail.next
        if saved == 1 :tail.next=ListNode(saved)
        return head.next
