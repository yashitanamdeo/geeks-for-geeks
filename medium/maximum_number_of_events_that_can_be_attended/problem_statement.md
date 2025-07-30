<h1 align="center">Maximum number of events that can be attended</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 31.89%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 16K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There are <b>N</b> events in Geek's city. You are given two arrays <b>start[]</b> and <b>end[] </b>denoting starting and ending day of the events respectively. Event i starts at start[i] and ends at end[i].<br>
You can attend an event i at any day <b>d</b> between start[i] and end[i] (start[i] ≤ d ≤ end[i]). But you can attend <b>only one event in a day</b>.<br>
Find the maximum number of events you can attend.

 

<b>Example 1:</b>

<pre><b>Input:
</b>N = 3
start[] = {1, 2, 1}
end[] = {1, 2, 2}
<b>Output:
</b>2
<b>Explanation:</b>
You can attend a maximum of two events.
You can attend 2 events by attending 1st event
at Day 1 and 2nd event at Day 2.
</pre>

<b>Example 2:</b>
<pre><b>Input:
</b>N = 3
start[i] = {1, 2, 3}
end[i] = {2, 3, 4} 
<b>Output :</b>
3
<b>Explanation:</b>
You can attend all events by attending event 1
at Day 1, event 2 at Day 2, and event 3 at Day 3.
</pre>

<br>
<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>maxEvents()</b> which takes an integer N and two arrays start[], and end[] of size N as input parameters and returns the maximum number of events that can be attended by you.

<br>
<b>Expected Time Complexity:</b> O(NlogN)<br>
<b>Expected Auxiliary Space:</b> O(N)

<br>
<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ start[i] ≤ end[i] ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Greedy` `Sorting` `Heap` `Data Structures` `Algorithms`
- **Company Tags:** `Adobe`

### Related Articles
- [Find Maximum Meetings In One Room](https://www.geeksforgeeks.org/find-maximum-meetings-in-one-room/)

### Related Interview Experiences
- [Adobe Systems Online Test On Campus Internship](https://www.geeksforgeeks.org/adobe-systems-online-test-on-campus-internship/)
