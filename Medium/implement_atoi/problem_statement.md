<h1 align="center">Implement Atoi</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 32.58%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 280K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b>, the objective is to <b>convert</b> it into <b>integer format</b> without utilizing any built-in functions. Refer the below steps to know about <b>atoi()</b> function.

<b>Cases for atoi() conversion:</b>

1. Skip any leading whitespaces.
1. Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
1. Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
1. If the integer is greater than 2<sup>31</sup> – 1, then return 2<sup>31</sup> – 1 and if the integer is smaller than -2<sup>31</sup>, then return -2<sup>31</sup>.
<b>Examples:</b>

<pre><b>Input: </b>s = "-123"
<b>Output: -</b>123<br><b>Explanation: </b>It is possible to convert -123 into an integer so we returned in the form of an integer<br></pre>

<pre><b>Input: </b>s = "  -"
<b>Output: </b>0<br><b>Explanation: </b>No digits are present, therefore the returned answer is 0.<br></pre>

<pre><b>Input: </b>s = " 1231231231311133"
<b>Output: </b>2147483647<br><b>Explanation: </b>The converted number will be greater than 2<sup>31</sup> – 1, therefore print 2<sup>31</sup> – 1 = 2147483647.
</pre>

<pre><b>Input: </b>s = "-999999999999"
<b>Output: -</b>2147483648<br><b>Explanation: </b>The converted number is smaller than -2<sup>31</sup>, therefore print -2<sup>31</sup> = -2147483648.</pre>

<pre><b>Input: </b>s = "  -0012gfg4"
<b>Output: </b>-12<b>
Explanation:</b> After ignoring leading zeros nothing is read after -12 as a non-digit character ‘g’ was encountered.</pre>

<b>Constraints:</b><br>1 ≤ |s| ≤ 15

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Strings` `Design-Pattern` `Data Structures`
- **Company Tags:** `Morgan Stanley` `Amazon` `Microsoft` `Payu` `Adobe` `Code Brew`

### Related Articles
- [Write Your Own Atoi](https://www.geeksforgeeks.org/write-your-own-atoi/)
