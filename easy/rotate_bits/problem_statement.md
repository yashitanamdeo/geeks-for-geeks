<h1 align="center">Rotate Bits</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 20.8%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 87K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an integer <b>N</b> and an integer <b>D</b>, rotate the binary representation of the integer N by D<b> </b>digits to the <b>left </b>as well as <b>right </b>and return the results in their <b>decimal representation </b>after each of the rotation.<br>Note: Integer N is stored using <b>16 bits</b>. i.e. 12 will be stored as 0000000000001100. <b>Output array</b> should follow <b>{leftrotation, rightrotation}.</b>

<b>Examples :</b>

<pre><b>Input: </b>n = 28, d = 2
<b>Output: </b>[112, 7]
<b>Explanation</b>: 28 in Binary is: 0000000000011100. Rotating left by 2 positions, it becomes 0000000001110000 = 112 (in decimal). Rotating right by 2 positions, it becomes 0000000000000111 = 7 (in decimal).
</pre>

<pre><b>Input</b>: n = 29, d = 2
<b>Output:</b> [116, 16391]
<b>Explanation</b>: 29 in Binary is: 0000000000011101. Rotating left by 2 positions, it becomes 0000000001110100 = 116 (in decimal). Rotating right by 2 positions, it becomes 010000000000111 = 16391 (in decimal).<br></pre>

<pre><b>Input</b>: n = 11, d = 10
<b>Output:</b> [11264, 704]</pre>

<b>Constraints:<br></b>1 <= n <  2<sup>16</sup><br>1 <= d <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(1)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Strings` `Bit Magic` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Rotate Bits Of An Integer](https://www.geeksforgeeks.org/rotate-bits-of-an-integer/)
