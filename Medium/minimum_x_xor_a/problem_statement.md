<h1 align="center">Minimum X (xor) A</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.06%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two integers <b>A</b> and <b>B</b>, the task is to find an integer <b>X</b> such that <b>(X XOR A)</b> is minimum possible and the count of set bit in <b>X</b> is equal to the count of set bits in <b>B</b>.

<b>Example 1:</b>

<pre><b>Input:</b> 
A = 3, B = 5
<b>Output:</b> 3
<b>Explanation:</b>
Binary(A) = Binary(3) = 011
Binary(B) = Binary(5) = 101
The XOR will be minimum when x = 3
i.e. (3 XOR 3) = 0 and the number
of set bits in 3 is equal
to the number of set bits in 5.</pre>

<b>Example 2:</b>

<pre><b>Input:</b> 
A = 7, B = 12
<b>Output:</b> 6
<b>Explanation:</b>
(7)<sub>2</sub>= 111
(12)<sub>2</sub>= 1100
The XOR will be minimum when x = 6 
i.e. (6 XOR 7) = 1 and the number 
of set bits in 6 is equal to the 
number of set bits in 12.</pre>

<b>Your task :</b>
You don't need to read input or print anything. Your task is to complete the function <b>minVal()</b> that takes integer A and B as input and returns the value of X according to the question.
 
<b>Expected Time Complexity : </b>O(log MAX(A,B))
<b>Expected Auxiliary Space : </b>O(1)
 
<b>Constraints :</b>
1 <= A, B <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Bit Magic` `Data Structures`
- **Company Tags:** `Adobe`

### Related Articles
- [Find A Number X Such That X Xor A Is Minimum And The Count Of Set Bits In X And B Are Equal](https://www.geeksforgeeks.org/find-a-number-x-such-that-x-xor-a-is-minimum-and-the-count-of-set-bits-in-x-and-b-are-equal/)

### Related Interview Experiences
- [Adobe Interview Experience Adobe For Women](https://www.geeksforgeeks.org/adobe-interview-experience-adobe-for-women/)
