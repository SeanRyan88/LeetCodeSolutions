class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        sol = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j +=1
            elif nums1[i] < nums2[j]:
                i +=1
            else:
                sol.append(nums1[i])
                i +=1
                j +=1
        return sol
    

# Test cases
test_cases = [
    ([1, 2, 2, 1], [2, 2]),
    ([4, 9, 5], [9, 4, 9, 8, 4]),
]

solution = Solution()
for i, (nums1, nums2) in enumerate(test_cases):
    result = solution.intersect(nums1, nums2)
    print(f"Test Case {i + 1}: intersection = {result}")
