<h1 align="center">Find minimum number of Laptops required</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.13%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 22K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There are <b>N</b> jobs and the start and finish time of the jobs are given in arrays <b>start[]</b> and <b>end[]</b> respectively. Each job requires one laptop and laptops can't be shared. Find the minimum number of laptops required given that you can give your laptop to someone else when you are not doing your job.

<br>
<b>Example 1:</b>

<pre><b>Input:
</b>N = 3
start[] = {1, 2, 3}
end[] = {4, 4, 6}
<b>Output:
</b>3
<b>Explanation:</b>
We can clearly see that everyone's supposed to
be doing their job at time 3. So, 3 laptops
will be required at minimum.
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 3
start[] = {1, 5, 2}
end[] = {2, 6, 3}
<b>Output :</b>
1
<b>Explanation:</b>
All jobs can be done using 1 laptop only.
</pre>

<br>
<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>minLaptops()</b> which takes an integer N and two arrays start and end denoting starting and ending time of N jobs and returns minimum laptops required.

<br>
<b>Expected Time Complexity:</b> O(N*logN)<br>
<b>Expected Auxiliary Space:</b> O(N)

<br>
<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5 </sup><br>
1<sup> </sup>≤ start[i] < end[i] ≤ 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Sorting` `Algorithms`
- **Company Tags:** `Morgan Stanley`

### Related Articles
- [Find Minimum Number Of Laptops Required](https://www.geeksforgeeks.org/find-minimum-number-of-laptops-required/)

### Related Interview Experiences
- [Morgan Stanley Interview Experience For Summer Internship 2021 Off Campus](https://www.geeksforgeeks.org/morgan-stanley-interview-experience-for-summer-internship-2021-off-campus/)
