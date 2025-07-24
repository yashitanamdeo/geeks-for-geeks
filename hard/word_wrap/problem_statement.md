<h1 align="center">Word Wrap</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 29.74%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 47K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b>, where <b>arr[i]</b> denotes the number of characters in one word. Let <b>k</b> be the limit on the number of characters that can be put in one line (line width). Put line breaks in the given sequence such that the lines are printed neatly.<br>Assume that the length of each word is smaller than the line width. When line breaks are inserted there is a possibility that extra spaces are present in each line. The extra spaces include spaces put at the end of every line <b>except the last one</b>. 

You have to <b>minimize </b>the following total cost where <b>total cost </b>= Sum of cost of all lines, where cost of line is = (Number of extra spaces in the line)<sup>2</sup>.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [3,2,2,5], k = 6
<b>Output: </b>10
<b>Explanation</b>: Given a line can have 6 characters,
Line number 1: From word no. 1 to 1
Line number 2: From word no. 2 to 3
Line number 3: From word no. 4 to 4
So total cost = (6-3)<sup>2</sup> + (6-2-2-1)<sup>2</sup> = 3<sup>2</sup>+1<sup>2</sup> = 10. As in the first line word length = 3 thus extra spaces = 6 - 3 = 3 and in the second line there are two word of length 2 and there already 1 space between two word thus extra spaces = 6 - 2 -2 -1 = 1. As mentioned in the problem description there will be no extra spaces in the last line. Placing first and second word in first line and third word on second line would take a cost of 0<sup>2</sup> + 4<sup>2</sup> = 16 (zero spaces on first line and 6-2 = 4 spaces on second), which isn't the minimum possible cost.
</pre>

<pre><b>Input: </b>arr[] = [3,2,2], k = 4
<b>Output: </b>5
<b>Explanation: </b>Given a line can have 4 characters,
Line number 1: From word no. 1 to 1
Line number 2: From word no. 2 to 2
Line number 3: From word no. 3 to 3
Same explaination as above total cost = (4 - 3)<sup>2</sup> + (4 - 2)<sup>2</sup> = 5<b>.</b>  </pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 500<br>1 ≤ arr[i] ≤ 1000<br>max(arr[i]) ≤ k ≤ 2000

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Flipkart` `Microsoft`

### Related Articles
- [Word Wrap Problem Dp 19](https://www.geeksforgeeks.org/word-wrap-problem-dp-19/)
- [Word Wrap Problem Space Optimized Solution](https://www.geeksforgeeks.org/word-wrap-problem-space-optimized-solution/)
