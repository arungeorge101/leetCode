"""
https://leetcode.com/problems/add-two-numbers/
"""

from imp import PY_COMPILED

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def listnode_to_pylist(self, listnode):
        ret = []
        while True:
            ret.append(listnode.val)
            if listnode.next != None:
                listnode = listnode.next
            else:
                return ret

    def pylist_to_listnode(self, pylist, link_count):
        if len(pylist) > 1:
            ret = PY_COMPILED.listnode.ListNode(pylist.pop())
            ret.next = self.pylist_to_listnode(pylist, link_count)
            return ret
        else:
            return PY_COMPILED.listnode.ListNode(pylist.pop(), None)
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_ = self.listnode_to_pylist(l1)
        l2_ = self.listnode_to_pylist(l2)
        
        l1_.reverse()
        n1 = int(''.join([ str(_) for _ in l1_]))
        l2_.reverse()
        n2 = int(''.join([ str(_) for _ in l2_]))
        ret = list(map(int, list(str(n1 + n2))))

        print("result : " + self.pylist_to_listnode(ret, len(ret)))
        return self.pylist_to_listnode(ret, len(ret))

if __name__ == "__main__":
    s = Solution()
    print(s.addTwoNumbers([2,4,3],[5,6,4]))