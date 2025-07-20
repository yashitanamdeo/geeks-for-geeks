<h1 align="center">Maximum Possible Value</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.61%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two arrays <b>A[]</b> and <b>B[]</b> of same length <b>N</b>. There are N types of sticks of lengths specified. Each stick of length <b>A[i] </b>is present in <b>B[i]</b> units (i=1 to N). You have to construct the squares and rectangles using these sticks. Each unit of a stick can be used as length or breadth of a rectangle or as a side of square. A single unit of a stick can be used only once.

Let <b>S</b> be the sum of lengths of all sticks that are used in constructing squares and rectangles. The task is to calculate the maximum possible value of S.

<b>Note</b>: The element in array <b>A[] </b>is always unique.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 4
A[] = {3,4,6,5}
B[] = {2,3,1,6}
<b>Output:</b> 
38
<b>Explanation: 
</b>There are 2 sticks of length 3.
There are 3 sticks of length 4.
There is a 1 stick of length 6.
There are 6 sticks of length 5.
One square can be made using 4 sticks of
4th kind (5*4=20)
A rectangle can be made using 2 sticks of 
4th kind and 2 sticks of 2nd kind (5*2+4*2=18)
<b>S</b> = 20 + 18 = 38

</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 1
A[] = {3}
B[] = {2}
<b>Output: 
</b>0
<b>Explanation: 
</b>There are only 2 sticks of length 3 which are 
not enough to make the square or rectangle.
</pre>

<b>Your Task: </b><br>
You don't need to read input or print anything. Complete the function<b> maxPossibleValue( )</b> which takes the integer <b>N</b>, the array <b>A[],</b> and the array <b>B[]</b> as input parameters and returns the maximum possible value of S. 

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>6</sup><br>
1 ≤ A[] ≤ 10<sup>6</sup><br>
1 ≤ B[] ≤ 10<sup>2</sup>


<hr>

### Tags
- **Topic Tags:** `Mathematical` `Algorithms`
- **Company Tags:** `Sprinklr`

### Related Articles
- [Maximizing Stick Utilization For Square And Rectangle Construction](https://www.geeksforgeeks.org/maximizing-stick-utilization-for-square-and-rectangle-construction/)
