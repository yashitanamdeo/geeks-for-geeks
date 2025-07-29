<h1 align="center">Scrambled String</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 59.4%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings <b>S1</b> and <b>S2</b> of equal length, the task is to determine if S2 is a scrambled form of S1.

<b>Scrambled string:</b> Given string <b>str</b>, we can represent it as a binary tree by partitioning it into two non-empty substrings recursively.<br>Below is one possible representation of str = <b>coder:</b><br> <img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/707514/Web/Other/5360f3bd-09bb-4f9d-9c84-be3844091359_1685087790.png" alt="" title=""/><br>To scramble the string, we may choose any non-leaf node and swap its two children. <br>Suppose, we choose the node <b>co</b> and swap its two children, it produces a scrambled string <b>ocder</b>.<br>Similarly, if we continue to swap the children of nodes <b>der</b> and <b>er</b>, it produces a scrambled string <b>ocred</b>.

<b>Note:</b> Scrambled string is not the same as an Anagram.

Print "Yes" if S2 is a scrambled form of S1 otherwise print "No".

<b>Example 1:</b>

<pre><b>Input:</b> S1="coder", S2="ocder"
<b>Output:</b> Yes
<b>Explanation:</b> ocder is a scrambled 
form of coder.

    ocder
   /    \
  oc    der
 / \    
o   c  

As "ocder" can represent it 
as a binary tree by partitioning 
it into two non-empty substrings.
We just have to swap 'o' and 'c' 
to get "coder".
</pre>

<b>Example 2:</b>

<pre><b>Input:</b> S1="abcde", S2="caebd" 
<b>Output:</b> No
<b>Explanation:</b> caebd is not a 
scrambled form of abcde.</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. You only need to complete the function<b> isScramble</b><b>() </b>which takes two strings S1 and S2 as input and returns a boolean value.

<b>Expected Time Complexity: </b>O(N<sup>2</sup>)<br><b>Expected Auxiliary Space:</b> O(N<sup>2</sup>)

<b>Constrains: </b>

- S1.length = S2.length
- S1.length<=31
- S1 and S2 consist of lower-case English letters.


<hr>

### Tags
- **Topic Tags:** `Strings` `Recursion` `Divide and Conquer` `Tree` `Data Structures` `Algorithms`
- **Company Tags:** `Nutanix`

### Related Articles
- [Check If A String Is A Scrambled Form Of Another String](https://www.geeksforgeeks.org/check-if-a-string-is-a-scrambled-form-of-another-string/)
