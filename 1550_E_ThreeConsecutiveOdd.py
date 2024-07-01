class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0
        for num in arr:
            if num % 2 != 0:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False
    
# Test case
test_cases = [1,2,34,3,5,7]

# Run Solution
solution = Solution()
print(solution.threeConsecutiveOdds(test_cases))







