<h1 align="center">Alternate Vowel and Consonant String</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.7%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 30K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>S</b> of <b>lowercase</b> english characters. Rearrange characters of the given string such that the vowels and consonants occupy <b>alternate</b> positions and the string so formed should be <b>lexicographically</b> (alphabetically) <b>smallest.</b> <br>
<b>Note: </b>Vowels are 'a', 'e', 'i', 'o' and 'u'. 

<b>Example 1:</b>

<pre><b>Input:</b>
S = "aeroplane"
<b>Output:</b> alanepero
<b>Explanation</b>: <b>a</b>l<b>a</b>n<b>e</b>p<b>e</b>r<b>o  
</b>The vowels and consonants are arranged 
alternatively with vowels shown in bold.
Also, there's no lexicographically smaller
string possible with required conditions.
</pre>

<b>Example 2:</b>

<pre><b>Input</b>: 
S = "mississippi"
<b>Output:</b> -1
<b>Explanation</b>: The number of vowels is 4 
whereas the number of consonants is 7.
Hence, there's no way to arrange the
vowels and consonants alternatively.
</pre>

<br>
<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>rearrange() </b>which takes the string <b>S</b> and its size<b> N</b> as inputs and <b>returns</b> the modified string as stated in the description. If such a modification is not possible, return the string "-1".

<br>
<b>Expected Time Complexity: </b>O(N).<br>
<b>Expected Auxiliary Space: </b>O(2*26).

<br>
<b>Constraints:</b><br>
1 <= N <= 10^6<br>
'a' <= S[ i ] <= 'z'


<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Lexicographically First Alternate Vowel Consonant String](https://www.geeksforgeeks.org/lexicographically-first-alternate-vowel-consonant-string/)
