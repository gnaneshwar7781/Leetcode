class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        right = dummy
        while(right.next and right.next.next):
            if(right.next.val == right.next.next.val):
                variable = right.next.val
                while(right.next != None and right.next.val == variable):
                    right.next = right.next.next
            else:
                right = right.next
        return dummy.next
            


        
        

       
        
