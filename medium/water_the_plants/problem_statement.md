<h1 align="center">Water the plants</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.22%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 36K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A gallery with plants is divided into <b>n</b> parts, numbered 0, 1, 2, 3, ..., n-1. There are provisions for attaching water sprinklers in every division. A sprinkler with range <b>x</b> at division <b>i</b> can water all divisions from <b>i-x</b> to <b>i+x</b>.

Given an array <b>gallery[]</b> consisting of <b>n</b> integers, where <b>gallery[i]</b> is the range of the sprinkler at partition <b>i</b> (a power of <b>-1</b> indicates no sprinkler attached), return the <b>minimum </b>number of sprinklers that need to be turned on to water the entire gallery. If there is <b>no possible way </b>to water the full length using the given sprinklers, print <b>-1</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
n = 6
gallery[] = {-1, 2, 2, -1, 0, 0}
<b>Output:
</b>2
<b>Explanation: <br></b>Sprinklers at index 2 and 5
can water the full gallery, span of
sprinkler at index 2 = [0,4] and span
of sprinkler at index 5 = [5,5].</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
n = 9
gallery[ ] = {2, 3, 4, -1, 2, 0, 0, -1, 0}
<b>Output:
</b>-1
<b>Explanation: <br></b>No sprinkler can throw water
at index 7. Hence all plants cannot be
watered.</pre>

<b>Example 3:</b>

<pre><b>Input:</b>
n = 9
gallery[ ] = {2, 3, 4, -1, 0, 0, 0, 0, 0}
<b>Output:
</b>3
<b>Explanation: <br></b>Sprinkler at indexes 2, 7 and
8 together can water all plants.</pre>

<b>Your task:</b><br>You do not have to take any input or print anything. Your task is to complete the function <b>min_sprinklers()</b> which takes the array <b>gallery[ ]</b> and the integer <b>n</b> as input parameters and returns the <b>minimum </b>number of sprinklers that need to be turned on to water the entire gallery.

<b>Expected Time Complexity:</b> O( nlog(n) )<br><b>Expected Auxiliary Space:</b> O( n )

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>5</sup><br>gallery[i] ≤ 50


<hr>

### Tags
- **Topic Tags:** `Greedy` `Sorting` `Algorithms`
- **Company Tags:** `Microsoft`

### Related Articles
- [Minimum Sprinkers Required To Be Turned On To Water The Plants](https://www.geeksforgeeks.org/minimum-sprinkers-required-to-be-turned-on-to-water-the-plants/)
