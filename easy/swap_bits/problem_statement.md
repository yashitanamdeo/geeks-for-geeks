<h1 align="center">Swap bits</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 69.18%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 7K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a number X and two positions (from right side) in binary representation of X, write a program that swaps N bits at given two positions and returns the result.

 

<b>Example 1:</b>

<pre><b>Input</b>:
X = 47
P1 = 1
P2 = 5
N = 3
<b>Output:</b> 227
<b>Explanation</b>:
The 3 bits starting from the second bit 
(from the right side) are swapped with 3 bits
starting from 6th position (from the right side) </pre>

<pre>X = 47 (00101111)
[001]0[111]1
ANS = [111]0[001]1
ANS = 227 (11100011)
Hence, the result is 227.  
</pre>

 

<b>Example 2:</b>

<pre><b>Input:</b>
X = 28
P1 = 0
P2 = 3
N = 2
<b>Output: </b>7</pre>

<br><b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>swapBits()</b> which takes the integer X, integer P1, integer P2, and integer N<b> </b>as input parameters and returns the new integer after swapping. <br><br><b>Expected Time Complexity:</b> O(1)<br><b>Expected Auxiliary Space:</b> O(1)<br> 

<br><b>Constraints:</b><br>1 ≤ X ≤ 200<br>0 ≤ P1 < P2 ≤ 11<br>1 ≤ N ≤ 5<br><br>


<hr>

### Tags
- **Topic Tags:** `Bit Magic` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Swap Bits In A Given Number](https://www.geeksforgeeks.org/swap-bits-in-a-given-number/)
