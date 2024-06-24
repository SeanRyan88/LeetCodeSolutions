class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(seat - student) for seat, student in zip(seats, students))

# Test cases
test_cases = [
    ([3, 1, 5], [2, 7, 4]),
    ([4, 1, 5, 9], [1, 3, 2, 6]),
    ([2, 2, 6, 6], [1, 3, 2, 6])
]

solution = Solution()
for i, (seats, students) in enumerate(test_cases):
    result = solution.minMovesToSeat(seats, students)
    print(f"Test Case {i + 1}: seats = {seats}, students = {students} => Min Moves = {result}")