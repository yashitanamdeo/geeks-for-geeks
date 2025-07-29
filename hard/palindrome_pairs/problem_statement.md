<h1 align="center">Palindrome Pairs</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 31.71%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of strings arr[] of size N, find if there exists 2 strings arr[i] and arr[j] such that arr[i]+arr[j] is a palindrome i.e the concatenation of string arr[i] and arr[j] results into a palindrome.

<br><b>Example 1:</b>

<pre><b>Input</b>:
N = 6
arr[] = {"geekf", "geeks", "or","keeg", "abc", 
          "bc"}
<b>Output:</b> 1 
<b>Explanation</b>: There is a pair "geekf"
and "keeg".
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 5
arr[] = {"abc", "xyxcba", "geekst", "or", "bc"}
<b>Output: </b>1
<b>Explanation</b>: There is a pair "abc"
and "xyxcba".
</pre>

<br><b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>palindromepair()</b> which takes the array arr[], its size N<b> </b>and returns true if palindrome pair exists and returns false otherwise.<br>The driver code itself prints 1 if returned value is true and prints 0 if returned value is false.<br> 

<b>Expected Time Complexity:</b> O(N*l<sup>2</sup>) where l = length of longest string in arr[]<br><b>Expected Auxiliary Space:</b> O(N*l<sup>2</sup>) where l = length of longest string in arr[]<br> 

<b>Constraints:</b><br>1 ≤ N ≤ 2*10<sup>4</sup><br>1 ≤ |arr[i]| ≤ 10


<hr>

### Tags
- **Topic Tags:** `Trie` `Advanced Data Structure`
- **Company Tags:** `Flipkart` `Amazon`

### Related Articles
- [Palindrome Pair In An Array Of Words Or Strings](https://www.geeksforgeeks.org/palindrome-pair-in-an-array-of-words-or-strings/)

### Related Interview Experiences
- [Flipkart Interview Experience For Software Developer Intern](https://www.geeksforgeeks.org/flipkart-interview-experience-for-software-developer-intern/)
- [Amazon Interview Experience Set 415 Sde 2](https://www.geeksforgeeks.org/amazon-interview-experience-set-415-sde-2/)
