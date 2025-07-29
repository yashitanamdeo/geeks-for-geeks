<h1 align="center">Maximum Identical Bowls</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.52%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 29K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There are <b>N</b> bowls containing cookies. In one operation, you can take one cookie from any of the non-empty bowls and put it into another bowl. If the bowl becomes empty you discard it. You can perform the above operation any number of times. You want to know the <b>maximum</b> number of bowls you can have with an identical number of cookies.

<b>Note: </b>All the non-discarded bowls should contain the identical number of cookies.

<b>Example 1:</b>

<pre><b>Input</b>:
N = 3
arr[] = {3, 1, 5}
<b>Output:</b> 3
<b>Explanation</b>: We can put 2 cookies one by one from the <br>3rd bowl and put them into the 2nd bowl.Now the array
becomes {3, 3, 3}. Each bowl now contains 3 cookies.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 4
arr[] = {1, 2, 6, 5}
<b>Output: </b>2
<b>Explanation</b>: We can take 6 cookies one by one from the <br>3rd bowl and put them into 1st bowl, now the array becomes 
{7, 2, 0, 5}. We discard the 3rd array as it becomes
 empty. Hence, arr={7, 2, 5}. Now, we take 5 cookies 
one by one from 3rd bowl and put them into the 2nd bowl. <br>Hence arr={7, 7, 0}. Discarding 3rd empty bowl, number of 
bowls containing identical number of cookies i.e 7 is 2.
</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>getMaximum()</b> which takes the array arr[] and its size N as input parameters and returns the maximum number of bowls we can have with an identical number of cookies. 

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 <= N <= 10<sup>5</sup><br>1 <= arr[i] <= 10<sup>9</sup><br>Array may contain duplicate elements.


<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures` `Algorithms`
- **Company Tags:** `None`
