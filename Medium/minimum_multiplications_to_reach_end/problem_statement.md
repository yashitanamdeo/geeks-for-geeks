<h1 align="center">Minimum Multiplications to reach End</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.94%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 168K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given <b>start</b>, <b>end</b> and an array <b>arr</b> of <b>n</b> numbers. At each step, <b>start</b> is multiplied with any number in the array and then mod operation with <b>100000</b> is done to get the new start. 

Your task is to find the minimum steps in which <b>end</b> can be achieved starting from <b>start</b>. If it is not possible to reach <b>end</b>, then return <b>-1</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
arr[] = {2, 5, 7}
start = 3, end = 30
<b>Output:</b>
2
<b>Explanation:</b>
Step 1: 3*2 = 6 % 100000 = 6 
Step 2: 6*5 = 30 % 100000 = 30
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
arr[] = {3, 4, 65}
start = 7, end = 66175
<b>Output:</b>
4
<b>Explanation:</b>
Step 1: 7*3 = 21 % 100000 = 21 
Step 2: 21*3 = 63 % 100000 = 63 
Step 3: 63*65 = 4095 % 100000 = 4095 
Step 4: 4095*65 = 266175 % 100000 = 66175
</pre>

<b>Your Task:<br></b>You don't need to print or input anything. Complete the function <b>minimumMultiplications()</b> which takes an integer array <b>arr</b>, an integer <b>start</b> and an integer<b> end</b> as the input parameters and returns an integer, denoting the minumum steps to reach in which <b>end</b> can be achieved starting from <b>start</b>.

<b>Expected Time Complexity:</b> O(10<sup>5</sup>)<br><b>Expected Space Complexity:</b> O(10<sup>5</sup>)

<b>Constraints:</b>

- 1 <= n <= 10<sup>4</sup>
- 1 <= arr[i] <= 10<sup>4</sup>
- 1 <= start, end < 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Graph` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Minimum Steps To Reach End From Start By Performing Multiplication And Mod Operations With Array Elements](https://www.geeksforgeeks.org/minimum-steps-to-reach-end-from-start-by-performing-multiplication-and-mod-operations-with-array-elements/)
