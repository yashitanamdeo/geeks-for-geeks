<h1 align="center">Save Your Life</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 59.25%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 23K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>w</b>, integer array <b>b,</b>  character array <b>x </b>and an integer <b>n</b>. <b>n</b> is the size of array <b>b</b> and array <b>x</b>. Find a substring which has the sum of the ASCII values of its every character, as maximum. ASCII values of some characters are redefined.<br>
<b>Note:</b><b> </b>Uppercase & lowercase both will be present in the string <b>w</b>. Array <b>b</b> and Array <b>x</b> contain corresponding redefined ASCII values. For each i, b[i] contain redefined ASCII value of character <b>x[i]</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
W = abcde
N = 1
X[] = { 'c' }
B[] = { -1000 }
<b>Output:</b>
de
<b>Explanation:
</b>Substring "de" has the
maximum sum of ascii value,
including c decreases the sum value
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
W = dbfbsdbf 
N = 2
X[] = { 'b','s' }
B[] = { -100, 45  }
<b>Output:</b>
dbfbsdbf
<b>Explanation:
</b>Substring "dbfbsdbf" has the maximum
sum of ascii value.
</pre>

<br>
<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>maxSum()</b> which takes string <b>W</b>, character array <b>X</b>, integer array <b>B</b>, integer <b>N</b> as length of array <b>X</b> and <b>B</b> as input parameters and returns the substring with the maximum sum of ascii value.<br>
 

<b>Expected Time Complexity: </b>O(|W|)<br>
<b>Expected Auxiliary Space: </b>O(1)

<br>
<b>Constraints:</b>

1<=|W|<=100000<br>
1<=|X|<=52<br>
-1000<=B<sub>i</sub><=1000

Each character of W and A will be from a-z, A-Z.


<hr>

### Tags
- **Topic Tags:** `Kadane` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Substring With Maximum Ascii Sum When Some Ascii Values Are Redefined](https://www.geeksforgeeks.org/substring-with-maximum-ascii-sum-when-some-ascii-values-are-redefined/)
