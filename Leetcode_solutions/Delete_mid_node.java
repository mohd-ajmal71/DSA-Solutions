class Solution {
    public ListNode deleteMiddle(ListNode head) 
    {
        ListNode slow=head;
        ListNode fast =head;
        ListNode temp=null;
        if(head.next==null)
        {  
            return null;
           
        }
        else if(head.next.next==null )
        {
            head.next=null;
            return head;
           
        }

        while(fast!=null && fast.next!=null)
        {
            temp=slow;
            slow=slow.next;
            fast=fast.next.next;
            

        }
        temp.next=temp.next.next;
        return head;
        
    }
}