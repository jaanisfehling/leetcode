/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        char[] char1 = sumList(l1).ToCharArray();
        Array.Reverse(char1);
        string str1 = new string(char1);
        System.Numerics.BigInteger x = System.Numerics.BigInteger.Parse(str1);
                
        char[] char2 = sumList(l2).ToCharArray();
        Array.Reverse(char2);
        string str2 = new string(char2);
        System.Numerics.BigInteger y = System.Numerics.BigInteger.Parse(str2);

        System.Numerics.BigInteger sum = x + y;
        string strSum = sum.ToString();
        char[] charSum = strSum.ToCharArray();
        Array.Reverse(charSum);
        
        return createListNode(charSum, 0);
    }
    public string sumList(ListNode node) {
        if (node.next is null) {
            return node.val.ToString();
        }
        else {
            return node.val.ToString() + sumList(node.next);
        }
    }
    public ListNode createListNode(char[] charArray, int i) {
        if (i == charArray.Length-1) {
            return new ListNode(charArray[i] - '0');
        }
        else {
            ListNode node = createListNode(charArray, i+1);
            Console.WriteLine(node.val);
            return new ListNode(charArray[i] - '0', node);
        }
    }
}
