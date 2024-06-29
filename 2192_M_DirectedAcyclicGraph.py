from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize the answer list with n empty lists
        answer = [[] for _ in range(n)]
        # print("Answer = ", answer)
        
        # Identify Connections
        # print("Edges")
        # print(edges)
        for x in range(len(edges)):
            # print("Test for", edges[x])
            # print("Add ", edges[x][0], " to ", edges[x][1])
            answer[edges[x][1]].append(edges[x][0])
        # print(answer)

        # Add missing values (transitive ancestors)
        def find_ancestors(node, ancestors):
            for ancestor in answer[node]:
                if ancestor not in ancestors:
                    ancestors.add(ancestor)
                    find_ancestors(ancestor, ancestors)


        # Sort
        # print("Sorting")
        for x in range(n):
            ancestors = set()
            find_ancestors(x, ancestors)
            answer[x] = sorted(ancestors)
        
        # print(answer)
        
        return answer

# Example usage
solution = Solution()
n = 5
edges = [[0, 1], [0, 2], [1, 3], [1, 4]]
print(solution.getAncestors(n, edges))  # Output should show the connections for each node

