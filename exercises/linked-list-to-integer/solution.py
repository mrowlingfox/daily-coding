# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        string = ""
        n = node
        while True:
            string += str(n.val)
            if n.next is None:
                return int(string, 2)
            n = n.next