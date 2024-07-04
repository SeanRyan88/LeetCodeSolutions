# 4/July/2024
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        # Initialise new linked list for response
        solution = ListNode(0)
        current = solution
        
        # Skip initial 0
        head = head.next
        
        # Hold current total
        sumVal = 0
        
        while head is not None:
            if head.val == 0:
                # if 0, add to solution and reset counter
                if sumVal > 0:
                    current.next = ListNode(sumVal)
                    current = current.next
                sumVal = 0

            else:
                # Add value to current total
                sumVal += head.val
            
            # Next node
            head = head.next
        
        return solution.next
 
 test_cases = [
    [0, 3, 1, 0, 4, 5, 2, 0],
    [0, 1, 0, 3, 0, 2, 2, 0]
]

for i, test_case in enumerate(test_cases):
    results = Solution.mergeNodes(test_case)
    print(f"Test Case {i + 1}: merged nodes = {results}")