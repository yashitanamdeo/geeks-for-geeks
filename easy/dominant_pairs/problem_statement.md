<h1 align="center">Dominant Pairs</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.57%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 36K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array of integers of size <b>n </b>where n being <b>even</b>.. You have to calculate the number of <b>dominate pairs (i,j)</b> . Where a pair is called dominant if ( <b>0<=i<n/2, n/2<=j<n, arr[i]>=5*arr[j] </b>) these relation are fulfilled.  For example  in arr=[10,3,3,1] index i=0, j=3 form a dominating pair<b><b> </b></b>

<b><b><b>Note </b>: <b>0</b> based </b></b>indexing is used  and n is <b><b><b>even </b></b></b>

<b><b>Example 1:</b></b>

<pre><b><b><b>Input:</b>
</b></b>n=4
arr={10,2,2,1}<b><b>
<b>Output:
</b></b></b>2<b><b>
<b>Explanation:</b>
</b></b>As we can see index i=0 and j=2 where
arr[0]>=5*arr[2] (10>=5*2)is fulfilled so
this forms a dominant pair and in same
manner index i=0 and j=3 forms dominant
pair.So total 2 dominant pairs.</pre>

<b><b>Example 2:</b></b><b><b> </b></b>

<pre><b><b><b>Input:</b>
</b></b>n=6
arr={10,8,2,1,1,2}<b><b>
<b>Output:
</b></b></b>5<b><b>
</b></b><b>Explanation:</b>
As we can see index i=0 and j=3 where
arr[0]>=5*arr[3] (10>=5*1) is fulfilled so
this forms a dominant pair and in same
manner (0,4),(0,5),(1,3),(1,4) also form
dominant pair.So total 5 dominant pairs.</pre>

<b><b><b>Your Task:</b></b></b><br>
You don't need to read input or print anything. Your task is to complete the function <b>dominantPairs()</b> which takes an <b>integer n</b> and <b>an array</b> of integers <b>arr</b> respectively and returns the <b>count </b>of dominate pairs.

<b>Expected Time Complexity:</b> O(nlogn)<br>
<b>Expected Auxiliary Space:</b> O(1)<br>
<br>
<b>Constraints:</b><br>
1 <= <b>n</b><= 10^4<br>
-10^4<=<b>arr[i]</b><= 10^4<br>
The sum of n over all test cases won't exceed 10^6


<hr>

### Tags
- **Topic Tags:** `two-pointer-algorithm` `Sorting` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find The Number Of Dominant Pairs](https://www.geeksforgeeks.org/find-the-number-of-dominant-pairs/)
