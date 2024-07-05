from typing import Optional, List
#5/July/2024

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Verify we have at least 3 items in the list
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        # Store index of critical points
        criticalPoints = []
        index = 0

        # Capture each item
        previous = head
        current = head.next
        

        # Identify min/max points
        while current.next:
            # (Max Check) or (Min Check)
            if (current.val > previous.val and current.val > current.next.val) or (current.val < previous.val and current.val < current.next.val):
                criticalPoints.append(index)

            # Add to index
            index +=1
            previous = previous.next
            current = current.next

        # Ensure more than 2 indexes
        if len(criticalPoints) < 2:
            return [-1,-1]
        
        # Calculate min and max distances between critical points
        # Already sorted in orer of index, max should be last minus first
        maxDistance = criticalPoints[-1] - criticalPoints[0]

        # Min distances should be smallest difference between values
        minDistance = float('inf')
        for i in range(0,len(criticalPoints)-1):
            minDistance = min(minDistance, criticalPoints[i+1] - criticalPoints[i])


        return [minDistance, maxDistance]
    

test_cases = [
[3,1],
[5,3,1,2,5,1,2],
[1,3,2,2,3,2,2,2,7]
]

for i, test_case in enumerate(test_cases):
    results = Solution.nodesBetweenCriticalPoints(test_case)
    print(f"Test Case {i + 1}: merged nodes = {results}")
