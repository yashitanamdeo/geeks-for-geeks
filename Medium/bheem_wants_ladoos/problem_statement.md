<h1 align="center">Bheem Wants Ladoos</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 65.19%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 20K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree where each node contains a number of ladoos equal to its value, and a starting node, <b>src,</b> find the maximum sum of ladoos that can be collected within a distance <b>k</b> from the starting node. The value at the starting node, <b>src</b>, should be included in the sum. Each node has a unique number of ladoos.

<b>Examples:</b>

<pre><b>Input:</b>
                   <b>1</b>
                 /    \
                2      <b>9</b>
               /      /  \
              4      <b>5</b>     <b>7</b>
            /   \         /  \
           8     19     20    11
          /     /  \
         30   40   50
src = 9, k = 1
<b>Output: </b>22
<b>Explanation: </b>Initially we're at 9, so sum = 9. In 2nd move we went to 5, sum=9+5=14. In 3rd move we went to 7, sum=14+7=21. In 4th move we went to 1, sum=21+1=22. So, within k distance we can get 22 ladoos.  
</pre>

<pre><b>Input:</b>
                   1
                 /    \
                2      9
               /      /  \
              <b>4</b>      5     7
            /   \         /  \
           8     <b>19</b>     20    11
          /     /  \
         30   <b>40</b>   <b>50</b>
src = 40, k = 2
<b>Output: </b>113
<b>Explanation: </b>Initially we're at 40, so sum = 40. In 2nd move we went to 19, sum=40+19=59. In 3rd move we went to 4, sum=59+4=63. In 4th move we went to 50, sum=63+50=113. So, within K distance we can get 113 ladoos.
</pre>

<pre><b>Input: </b>1
src = 1, k = 1
<b>Output: </b>1</pre>

<b>Constraints:</b><br>1 ≤ number of nodes, src ≤ 10<sup>5<br></sup>1 ≤ node->data ≤ 10<sup>5<br></sup>1 ≤ k ≤ 20

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Tree` `Data Structures`
- **Company Tags:** `None`
