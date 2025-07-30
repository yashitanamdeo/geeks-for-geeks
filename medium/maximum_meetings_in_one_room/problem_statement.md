<h1 align="center">Maximum Meetings in One Room</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 33.57%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 73K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There is one meeting room in a firm. There are <b>N</b> meetings in the form of <b>(S[i], F[i])</b> where <b>S[i]</b> is the start time of meeting <b>i</b> and <b>F[i]</b> is the finish time of meeting <b>i</b>. The task is to find the <b>maximum</b> number of meetings that can be accommodated in the meeting room. You can accommodate a meeting if the start time of the meeting is strictly greater than the finish time of the previous meeting. Print all meeting numbers.

<b>Note: </b>If two meetings can be chosen for the same slot then choose meeting that <b>finishes earlier</b>.

<b>Example 1:</b>

<pre><b>Input:
</b>N = 6
S = {1,3,0,5,8,5}
F = {2,4,6,7,9,9} <b>
Output:
</b>{1,2,4,5}<b>
Explanation:
</b>We can attend the 1st meeting from (1 to 2), then the 2nd meeting from (3 to 4), then the 4th meeting from (5 to 7), and the last meeting we can attend is the 5th from (8 to 9). It can be shown that this is the maximum number of meetings we can attend.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 1
S = {3}
F = {7}
<b>Output:</b>
{1}
<b>Explanation:</b>
Since there is only one meeting, we can attend the meeting.</pre>

<b>Your Task:</b>

You don't need to read input or print anything. Your task is to complete the function <b>maxMeetings()</b> which takes the arrays <b>S</b>, <b>F,</b> and its size <b>N </b>as inputs and returns the meeting numbers we can attend in <b>sorted order</b>.

<b>Expected Time Complexity:</b> O(N*log(N))<br><b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>1 <= N <= 10<sup>5</sup><br>0 <= S[i] <= F[i] <= 10<sup>9</sup><br>Sum of N over all test cases doesn't exceeds 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Greedy` `Sorting` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find Maximum Meetings In One Room](https://www.geeksforgeeks.org/find-maximum-meetings-in-one-room/)
