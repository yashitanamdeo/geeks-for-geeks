<h1 align="center">Capacity To Ship Packages Within D Days</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.14%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 26K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> of <b>n</b> weights. Find the least weight capacity of a boat to ship all weights within <b>d</b> days.<br>The i<sup>th</sup> weight has a weight of arr[i]. Each day, we load the boat with weights given by arr[i].We may not load more weight than the maximum weight capacity of the ship.<br><br><b>Note: </b>You have to load weights on the boat in the given order.

 

<b>Example 1:</b>

<pre><b>Input:
</b>n = 3
arr[] = {1, 2, 1}
d = 2
<b>Output:
</b>3
<b>Explanation:</b>
We can ship the weights in 2 days
in the following way:-
Day 1- 1,2
Day 2- 1
</pre>

<b>Example 2:</b>
<pre><b>Input:
</b>n = 3
arr[] = {9, 8, 10}
d = 3
<b>Output:</b>
10
<b>Explanation:</b>
We can ship the weights in 3 days
in the following way:-
Day 1- 9
Day 2- 8
Day 3- 10
</pre>

 

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>leastWeightCapacity()</b> which takes 2 integers n, and d, and an array arr of size n as input and returns the least weight capacity of the boat required.

<br><b>Expected Time Complexity:</b> O(n*log(Sum of weights - max(list of weights))<br><b>Expected Auxiliary Space:</b> O(1)

<br><b>Constraints:</b><br>1 ≤ d ≤ n ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Binary Search` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon` `D-E-Shaw`

### Related Articles
- [Capacity To Ship Packages Within D Days](https://www.geeksforgeeks.org/capacity-to-ship-packages-within-d-days/)

### Related Interview Experiences
- [D E Shaw Interview Experience For Software Engineer Off Campus 2020](https://www.geeksforgeeks.org/d-e-shaw-interview-experience-for-software-engineer-off-campus-2020/)
