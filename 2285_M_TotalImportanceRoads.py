class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        # Create a blank array for each city
        degrees = [0] * n
        for road in roads:
            degrees[road[0]] += 1
            degrees[road[1]] += 1

        # Sort cities by number of degrees and assign values
        sorted_cities = sorted(range(n), key=lambda x: degrees[x], reverse=True)
        city_value = [0] * n
        for i, city in enumerate(sorted_cities):
            city_value[city] = n - i

        # Calculate value of each road
        total_value = 0
        for road in roads:
            total_value += city_value[road[0]] + city_value[road[1]]

        return total_value

# Example 
solution = Solution()
N = 5
roads = [[0, 1], [0, 2], [1, 2], [1, 3], [3, 4]]
print(solution.maximumImportance(N, roads))  
