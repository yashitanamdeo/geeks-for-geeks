<h1 align="center">Bus Conductor</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 75.3%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 22K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are conductor of a bus. You are given two arrays <b>chairs[]</b> and <b>passengers[]</b> of equal length, where <b>chairs[i]</b> is the position of the <b>i<sup>th</sup></b> chair and <b>passengers[j]</b> is the position of the <b>j<sup>th</sup></b> passenger. You may perform the following move any number of times:

- Increase or decrease the position of the <b>i<sup>th</sup></b> passenger by <b>1</b> (i.e., moving the <b>i<sup>th</sup></b> passenger from position <b>x</b> to <b>x+1</b> or <b>x-1</b>)
Return the <b>minimum number of moves</b> required to move each passenger to get a chair such that no two passengers are in the same chair and every passenger gets a chair.

<b>Note:</b> Initially, multiple passengers or chairs may occupy the same position.

<b>Examples:</b>

<pre><b>Input:</b> chairs[] = [3, 1, 5], passengers[] = [2, 7, 4]
<b>Output:</b> 4
<b>Explanation:</b> The passengers are moved as follows:
- The first passenger is moved from position 2 to position 1 using 1 move.
- The second passenger is moved from position 7 to position 5 using 2 moves.
- The third passenger is moved from position 4 to position 3 using 1 move.
In total, 1 + 2 + 1 = 4 moves were used.
</pre>

<pre><b>Input:</b> chairs[] = [2, 2, 6, 6], passengers[] = [1, 3, 2, 6]
<b>Output:</b> 4
<b>Explanation:</b> Note that there are two chairs at position 2 and two chairs at position 6.
The passangers are moved as follows:
- The first passenger is moved from position 1 to position 2 using 1 move.
- The second passenger is moved from position 3 to position 6 using 3 moves.
- The third passenger is not moved.
- The fourth passenger is not moved.
In total, 1 + 3 + 0 + 0 = 4 moves were used.</pre>

<b>Constraints:<br></b>1 ≤ n ≤ 10<sup>5<br></sup>1 ≤ chairs[i], passengers[j] ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Sorting`
- **Company Tags:** `None`

### Related Articles
- [Minimize The Number Of Moves Required To Seat Each Passenger In A Chair](https://www.geeksforgeeks.org/minimize-the-number-of-moves-required-to-seat-each-passenger-in-a-chair/)
