<h1 align="center">Grinding Geek</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 49K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

GeeksforGeeks has introduced a special offer where you can enroll in any course, and if you manage to complete 90% of the course within 90 days, you will receive a refund of 90%.

Geek was fascinated by this offer. This offer was valid for <b>only n days</b>, and <b>each day</b> a <b>new course</b> was available for purchase. Geek decided that if he bought a course on some day, he will <b>complete that course on the same day itself</b> and redeem <b><i>floor[90% of cost of the course]</i></b> amount back. Find the <b>maximum number of courses</b> that Geek can complete in those n days if he had <i><b>total </b></i>amount initially.

<b>Note</b>: On any day, Geek can only buy the new course that was made available for purchase that day.

<b>Example 1:</b>

<pre><b>Input</b>:<br>n = 2<br>total = 10<br>cost = [10, 9]<br><b>Output</b>: 2<br><b>Explanation</b>: <br>Geek can buy the first course for 10 amount, <br>complete it on the same date and redeem 9 back. <br>Next, he can buy and complete the 2nd course too.</pre>

<b>Example 2:</b>

<pre><b>Input</b>:<br>n = 11<br>total = 10<br>cost = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]<br><b>Output</b>: 10<br><b>Explanation</b>: <br>Geek can buy and complete all the courses that cost 1<br> as well as 1 course that cost 10 and 9 course that cost 1.<br></pre>

<b>Your Task:<br></b>This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <b>max_courses</b><b>()</b> that takes <b>N</b> the number of days, the <b>total</b> amount, and the <b>cost</b> array as input argument and return the <b>maximum </b>amount of courses that could be purchased.

<b>Expected Time Complexity:</b> O(n*total)<br><b>Expected Auxiliary Space:</b> O(n*total)<br>

<b>Constraints:<br></b>1 <= n <= 1000<br>0 <= total <= 1000<br>1 <= cost[i] <= 1000


<hr>

### Tags
- **Topic Tags:** `None`
- **Company Tags:** `None`
