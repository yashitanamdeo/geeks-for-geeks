<h1 align="center">Lexicographically smallest string</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.97%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>S</b> consisting of <b>only lowercase characters</b>. Find the lexicographically smallest string after removing <b>exactly</b> <b>k</b> characters from the string. But you have to correct the value of <b>k</b>, i.e., if the length of the string is a <b>power of 2</b>, reduce <b>k by half</b>, else multiply <b>k by 2</b>. You can remove <b>any k</b> character.<br>
<b>NOTE: </b>If it is not possible to remove k (the value of k after correction) characters or if the resulting string is empty return <b>-1</b>. <br>
<br>
<b>Example 1:</b>

<pre><b>Input</b>: S = "fooland", k = 2
<b>Output:</b> "and" 
<b>Explanation</b>: As the size of the string = 7
which is not a power of 2, hence k = 4.
After removing 4 characters from the given 
string, the lexicographically smallest
string is "and".
</pre>

<b>Example 2:</b>

<pre><b>Input: </b>S = "code", k = 4
<b>Output: </b>"cd"
<b>Explanation</b>: As the length of the string = 4, 
which is 2 to the power 2, hence k = 2.
Hence, lexicographically smallest string after 
removal of 2 characters is "cd".</pre>

<br>
<b>Your Task:  </b><br>
You dont need to read input or print anything. Complete the function <b>lexicographicallySmallest() </b>which takes S and k as input parameters and returns the lexicographically smallest string after removing k characters.<br>
<br>
<b>Expected Time Complexity:</b> O(n+k), n is size of the string<br>
<b>Expected Auxiliary Space:</b> O(n)<br>
<br>
<b>Constraints:</b><br>
1<= |S| <=10<sup>5</sup><br>
1<= k <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Strings` `Stack` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Lexicographically Smallest String By Removing Exactly K Characters](https://www.geeksforgeeks.org/lexicographically-smallest-string-by-removing-exactly-k-characters/)
