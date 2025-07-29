<h1 align="center">Aggressive Cows</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 59.57%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 152K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array with unique elements of stalls[],<b> </b>which denote the position of a <b>stall</b>. You are also given an integer <b>k</b> which denotes the number of aggressive cows. Your task is to assign <b>stalls </b>to<b> k </b>cows such that the <b>minimum distance </b>between any two of them is the<b> maximum </b>possible.

<b>Examples :</b>

<pre><b>Input: </b>stalls[] = [1, 2, 4, 8, 9], k = 3
<b>Output: </b>3
<b>Explanation: </b>The first cow can be placed at stalls[0], <br>the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows, in this case, is 3, which also is the largest among all possible ways.
</pre>

<pre><b>Input: </b>stalls[] = [10, 1, 2, 7, 5], k = 3
<b>Output: </b>4
<b>Explanation: </b>The first cow can be placed at stalls[0],
the second cow can be placed at stalls[1] and
the third cow can be placed at stalls[4].
The minimum distance between cows, in this case, is 4, which also is the largest among all possible ways.</pre>

<pre><b>Input: </b>stalls[] = [2, 12, 11, 3, 26, 7], k = 5
<b>Output: </b>1
<b>Explanation: </b>Each cow can be placed in any of the stalls, as the no. of stalls are exactly equal to the number of cows.
The minimum distance between cows, in this case, is 1, which also is the largest among all possible ways.</pre>

<b>Constraints:</b><br>2 <= stalls.size() <= 10<sup>6</sup><br>0 <= stalls[i] <= 10<sup>8</sup><br>2 <= k <= stalls.size()

## Expected Complexities
- Time Complexity: O(n log m)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Binary Search` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Assign Stalls To K Cows To Maximize The Minimum Distance Between Them](https://www.geeksforgeeks.org/assign-stalls-to-k-cows-to-maximize-the-minimum-distance-between-them/)
