<h1 align="center">Concatenate Equal to Target</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 43.73%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 8K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of <b>digit</b> strings nums and a <b>digit</b> string target, return the number of pairs of indices (i,j)<i> </i>(where i != j) such that the <b>concatenation</b> of nums[i] + nums[j] equals <b>target.</b>

<b>Note:</b>

- nums[i] & target consists of digits
- nums[i] & target do not have leading zeros.
<b>Example 1:</b>

<pre><b>Input:</b>
N = 4 
nums[] = {"1","212","12","12"} target = "1212" <b>Output:</b> 3 <b>Explanation:</b> We can obtain target = "1212" by concatenating: nums[0] = "1" with nums[1] = "212" nums[2] = "12" with nums[3] = "12" nums[3] = "12" with nums[2] = "12" </pre>

<b>Example 2:</b>

<pre><b>Input: </b>
N = 3
nums[] = {"11","11","110"} target = "11011" <b>Output:</b> 2 <b>Explanation: </b>We can obtain target = "11011" by concatenating: nums[2] = "110" with nums[0] = "11" nums[2] = "110" with nums[1] = "11"</pre>

<b>Example 3:</b>

<pre><b>Input: </b>
N = 3
nums[] = {"1","1","1"} target = "11" <b>Output:</b> 6 <b>Explanation: </b>We can obtain target = "11" by concatenating: nums[0] = "1" with nums[1] = "1" nums[1] = "1" with nums[0] = "1" nums[0] = "1" with nums[2] = "1" nums[2] = "1" with nums[0] = "1" nums[1] = "1" with nums[2] = "1" nums[2] = "1" with nums[1] = "1"</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>countPairs() </b>which takes<b> </b>the integer <b>N, </b>the string <b>target</b> and the string array <b>nums[] </b>as the input parameters and returns the number of pairs which satisfies the above condition.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>2 ≤ N ≤ 10<sup>5</sup><br>1 ≤ nums[] ≤ 10<sup>5</sup><br>2 ≤ target ≤ 10<sup>5</sup><br>


<hr>

### Tags
- **Topic Tags:** `Strings` `Arrays` `Map`
- **Company Tags:** `None`
