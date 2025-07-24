# Problem Statement: https://practice.geeksforgeeks.org/problems/minimum-swaps/1#



class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
        ans = 0
        sortedNums = sorted(nums)
        store = {}
        
        for i, item in enumerate(nums):
            store[item] = i
        
        for i in range(len(nums)):
            if nums[i] != sortedNums[i]:
                ans +=1
                store[nums[i]] = store[sortedNums[i]]
                nums[store[sortedNums[i]]] = nums[i]
        return ans

#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends