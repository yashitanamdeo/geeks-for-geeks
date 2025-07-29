<h1 align="center">Max Equal sum of 3 Stacks</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.71%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 48K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given three stacks <b>S1</b>, <b>S2</b> & <b>S3</b> of size <b>N1</b>, <b>N2 </b>& <b>N3 </b>respectively, having only <b>Positive </b>Integers. The task is to find the possible equal <b>maximum sum</b> of the stacks with the removal of top elements allowed. Stacks are represented as an array, and the first index of the array represents the top element of the stack.

<b>Example 1:</b>

<pre><b>Input:
</b>N1 = 3, N2 = 4, N3 = 2
S1 = {4,2,3}
S2 = {1,1,2,3}
S3 = {1,4}<b>
Output:</b>
5<b>
Explanation:
</b>We can pop 1 element from the 1st stack, and 2
elements from the 2nd stack. Now remaining elements
yield the equal sum of the three stacks, that is 5.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N1 =2, N2 = 1, N3 = 3
S1 = {4,7}
S2 = {10}
S3 = {1,2,3}<b>
Output:
</b>0<b>
Explanation:
</b>We will never get an equal sum after popping
some elements, so the answer will be 0.
</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>maxEqualSum()</b> which takes the arrays <b>S1[], S2[], </b>and<b> S3[]</b> and their sizes <b>N1, N2, </b>and<b> N3 </b>as inputs and returns the maximum equal sum we can obtain.

<b>Expected Time Complexity:</b> O(N1+N2+N3)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 <= N1, N2, N3 <= 10<sup>5</sup><br>1 <= S1[i], S2[i], S3[i] <= 10<sup>3</sup><br>The sum, N1+N2+N3 doesn't exceed 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Greedy` `Stack` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find Maximum Sum Possible Equal Sum Three Stacks](https://www.geeksforgeeks.org/find-maximum-sum-possible-equal-sum-three-stacks/)
