<h1 align="center">Median of the Subarrays</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.99%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>A[]</b> of <b>N</b> integers and an integer <b>M</b>.<b> </b>The task is to count the number of subarrays which have median <b>M</b>.<br>
Median of an array is defined as below:

1. If N is odd, the median value is the number that is in the middle after sorting the array.<br>
2. if N is even, the median value is the left of the two middle numbers after sorting the array. 

<b>Example 1:</b>

<pre><b>Input:</b>
N = 5, M = 2
A[] = {2, 1, 3, 5, 4}
<b>Output:</b> 
3
<b>Explanation: 
</b>The subarrays which has median equal to M
are [2], [2,1,3] and [2,1,3,5]

</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 1, M = 1
A[] = {1}
<b>Output: 
</b>1
<b>Explanation: 
</b>The subarrays which has median equal to M
is [1].

</pre>

<b>Your Task: </b><br>
You don't need to read input or print anything. Complete the function<b> countSubarray( )</b> which takes the integer <b>N</b> , the array <b>A[],</b> and the integer <b>M</b> as input parameters and returns the number of subarays. 

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ A[] ≤ 10<sup>5</sup><br>
1 ≤ M ≤ N


<hr>

### Tags
- **Topic Tags:** `Sorting` `Map` `Data Structures` `Algorithms`
- **Company Tags:** `Sprinklr`
