# Problem Statement: https://practice.geeksforgeeks.org/problems/number-of-islands/1

#User function Template for python3
from typing import List

class Disjoint:
    def __init__(self, n=0):
        self.n = n
        self.array = [-1] * self.n

    def add(self):
        self.array.append(-1)
        self.n += 1

    def find(self, n):
        if self.array[n] < 0:
            return (n,  -self.array[n])
        result = self.find(self.array[n])
        self.array[n] = result[0]
        return result
    
    def union(self, set1, set2):
        parent_of_set1, rank_of_set1 = self.find(set1)
        parent_of_set2, rank_of_set2 = self.find(set2)

        if parent_of_set1 == parent_of_set2:
            return False

        if rank_of_set1 > rank_of_set2:
            self.array[parent_of_set1] += self.array[parent_of_set2]
            self.array[parent_of_set2] = parent_of_set1
            
        else:
            self.array[parent_of_set2] += self.array[parent_of_set1]
            self.array[parent_of_set1] = parent_of_set2
        return True


class Solution:
    def numOfIslands(self, N: int, M : int, operators : List[List[int]]) -> List[int]:
        SEA, ISLAND = 0, 1
        MOVE_X = [0, 0, 1, -1]
        MOVE_Y = [1, -1, 0, 0]
        
        grid = [[SEA]*M for _ in range(N)]
        ans = []
        countIslands = 0
        d = Disjoint(N * M)
        
        for x, y in operators:
            if grid[x][y] == SEA:
                # following row level indexing like C 
                index = x * M + y
                
                for delX, delY in zip(MOVE_X, MOVE_Y):
                    # neighbour positioning
                    newX, newY = x + delX, y + delY
                    newIndex = newX * M + newY
                    
                    if 0 > newX or newX >= N or 0 > newY or newY >= M:
                        continue
                    
                    if grid[newX][newY] == SEA:
                        continue

                    # if neighbour is an island also disconnected from (x, y)
                    # then merging these two meaning reducing one island
                    if d.union(index, newIndex):
                        countIslands -= 1
                # if there are 4 different neighbors around (x, y) 
                # then countIslands will be decremented by 4
                # but actually we need to decremented by 3, so balancing adding 1
                countIslands += 1
            
            # adding countIslands to answer and updating cell to island in grid
            ans.append(countIslands)
            grid[x][y] = ISLAND
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end = ' ')
        print()
            

# } Driver Code Ends