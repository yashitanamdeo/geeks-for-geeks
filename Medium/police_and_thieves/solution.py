# Problem Statement: https://www.geeksforgeeks.org/problems/police-and-thieves--141631/1

class Solution:
    def catchThieves(self, arr, k):
       # Step 1: Store positions of all policemen and thieves
        police_positions = []
        thief_positions = []
    
        for i in range(len(arr)):
            if arr[i] == 'P':
                police_positions.append(i)
            elif arr[i] == 'T':
                thief_positions.append(i)
    
        # Step 2: Use two pointers to match
        i = 0  # Pointer for police
        j = 0  # Pointer for thief
        result = 0
    
        while i < len(police_positions) and j < len(thief_positions):
            # If distance between police and thief is within k
            if abs(police_positions[i] - thief_positions[j]) <= k:
                result += 1  # One thief caught
                i += 1
                j += 1
            elif police_positions[i] < thief_positions[j]:
                i += 1  # Move police pointer
            else:
                j += 1  # Move thief pointer
    
        return result

