<h1 align="center">Can Make Triangle</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 80.26%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 7K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>A[] </b>of <b>N </b>elements, You'd like to know how many triangles can be formed with side lengths equal to adjacent elements from A[].

Construct an array of integers of length N - 2 where ith element is equal to <b>1</b> if it is possible to form a triangle with side lengths<b> A[i]</b>, <b>A[i+1]</b>, and <b>A[i+2]</b>. otherwise <b>0</b>.

<b>Note: </b>A triangle can be formed with side lengths a, b and c if a+b>c and a+c>b and b+c>a.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 4
A[] = {1, 2, 2, 4}
<b>Output:</b>
1 0
<b>Explanation:</b>
output[0] = 1 because we can form a 
triangle with side lengths 1,2 and 2.
output[1] = 0 because 2+2<u><</u>4 so, we cannot 
form a triangle with side lengths 2,2 and 4.
</pre>

<b>Example 2:</b>

<pre><b>Input: </b>
N = 5
A[] = {2, 10, 2, 10, 2}
<b>Output:</b>
0 1 0
<b>Explanation:
</b>output[0] = 0 because 2+2<u><</u>10 so, we cannot
form a triangle with side lengths 2, 10 and 2.<b> </b>
output[1] = 1 we can form a triangle with 
side lengths 10,2 and 10.<b> 
</b>output[1] = 0 because 2+2<u><</u>10 so, we can
form a triangle with side lengths 2, 10 and 2.<b> </b>
</pre>

<b>Your Task:</b><br>
You dont need to read input or print anything. Your task is to complete the function <b>canMakeTriangle() </b>which takes the array <b>A</b> and the integer <b>N </b>as the input parameters, and returns the array of answers.

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>
3 ≤ N ≤ 10<sup>5 </sup><br>
1 ≤ arr[i] ≤ 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Mathematical` `Geometric` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Possible Form Triangle Array Values](https://www.geeksforgeeks.org/possible-form-triangle-array-values/)
