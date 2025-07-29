<h1 align="center">Bit Magic</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.02%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 28K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an integer array <b>arr[]</b> of size <b>n</b> which contains only <b>1</b> and <b>0.</b> Your task is to make the array perfect. An array is said to be <b>perfect</b> if for each <b>i</b> from <b>0</b> to <b>n-1</b> <b>arr[i]==arr[n-1-i]</b> is satisfied. 

To Make the array perfect you are allowed to do the following operation  :

In one operation you can choose two different indexes <b>i</b> and <b>j</b> and set value of both <b>arr[i]</b> and <b>arr[j] </b>to <b>arr[i]^arr[j]</b>.

Your task is to make the array <b>perfect</b> in <b>minimum possible number</b> of operations and return the number of operations.

<b>Note</b>: <b>0-based indexing is used</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
n<b> = </b>4
arr = {1,0,0,0}
<b>Output:
</b>1
<b>Explanation:</b>
We can take index 0 and 3 and apply the operation.
Array becomes {1,0,0,1}.Now the condition is satisfied </pre>

<b>Example 2:</b>

<pre><b>Input:</b>
n = 3
arr = {1,0,1}
<b>Output:</b>
0
<b>Explanation:</b>
condition is satisfied intially. So no operation is required
in this case.</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>bitMagic()</b> which takes an integer <b>n</b> and <b>a binary integers array arr</b> respectively and returns the<b> minimum</b> number of operations required to make the array <b>perfect. </b>

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>
1 <= n<b> </b><= 10^5<br>
0 <= arr[i]<b> </b><=1


<hr>

### Tags
- **Topic Tags:** `Greedy` `Bit Magic` `Data Structures` `Algorithms`
- **Company Tags:** `None`
