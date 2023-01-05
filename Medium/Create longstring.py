class Solution():

    def longestString(self, arr, n):

         #your code goes here

        arr.sort()

        max=""

        dict={}

        dict[""]=1

        for i in range(n):

            if arr[i][:-1] in dict:

                dict[arr[i]]=1

                if len(max)<len(arr[i]):

                    max=arr[i]

        return max
