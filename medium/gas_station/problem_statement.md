<h1 align="center">Gas Station</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 34.79%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 213K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There are n gas stations along a <b>circular tour</b>. You are given two integer arrays <b>gas[]</b> and <b>cost[]</b>, where <b>gas[i]</b> is the amount of gas available at station <b>i</b> and <b>cost[i]</b> is the gas needed to travel from station <b>i</b> to station (<b>i+1</b>). You have a car with an unlimited gas tank and start with an empty tank at some station. Your task is to return the <b>index </b>of the starting station if it is possible to travel once around the circular route in a clockwise direction without running out of gas at any station; otherwise, return <b>-1</b>.

<b>Note: </b>If a solution exists, it is guaranteed to be unique.

<b>Examples:</b>

<pre><b>Input: </b>gas[] = [4, 5, 7, 4], cost[]= [6, 6, 3, 5]
<b>Output: </b>2<b>
Explanation: </b>Start at gas station at index 2 and fill up with 7 units of gas. Your tank = 0 + 7 = 7<br>Travel to station 3. Available gas = (7 – 3 + 4) = 8.<br>Travel to station 0. Available gas = (8 – 5 + 4) = 7.<br>Travel to station 1. Available gas = (7 – 6 + 5) = 6.<br>Return to station 2. Available gas = (6 – 6) = 0.
</pre>

<pre><b>Input: </b>gas[] = [3, 9], cost[] = [7, 6]<br><b>Output: -</b>1<b>
Explanation: </b>There is no gas station to start with such that you can complete the tour.</pre>

<b>Constraints:<br></b>1 ≤ n ≤ 10<sup>6<br></sup>1 ≤ gas[i], cost[i] ≤ 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Data Structures` `Algorithms` `Greedy`
- **Company Tags:** `Zoho` `Flipkart` `Morgan Stanley` `Amazon` `Microsoft` `FactSet` `Google`

### Related Articles
- [Find A Tour That Visits All Stations](https://www.geeksforgeeks.org/find-a-tour-that-visits-all-stations/)

### Related Interview Experiences
- [Microsoft Interview Experience Set 76 On Campus](https://www.geeksforgeeks.org/microsoft-interview-experience-set-76-on-campus/)
- [Flipkart Interview Experience For Sde 1](https://www.geeksforgeeks.org/flipkart-interview-experience-for-sde-1/)
