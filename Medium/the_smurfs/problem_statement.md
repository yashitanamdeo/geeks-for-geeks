<h1 align="center">The Smurfs</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.37%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 15K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A geek once visited a magical island where he found a special creature. He named it as Smurf. He noticed a very strange thing there. The smurfs resembled the primary colors of light. To make it more clear, the primary colors of light are <b>Red</b>(R), <b>Green</b>(G), and <b>Blue</b>(B). He talked to one of the smurfs. The smurfs came to know that he is a good programmer. The smurfs suggested a deal that they will ask him one question and if he is able to answer that question, they will allow the geek to take anything from the island.<br>
The question is as follows:<br>
The smurfs possess a very magical property. When two smurfs of different colors meet with other, they gets converted into a smurf of the third color. How many minimum number of smurfs will be remaining after this transformation? The question looked simple to geek. However, the smurfs put another constraint to make the geek think more. The two smurfs must be adjacent to each other  to make the transformation take place. There are <b>n</b> smurfs the colors of which are given in an array <b>a[]</b>.

<b>Example 1:</b>

<pre><b>Input:</b> n = 5
a = {'R' , 'G', 'B', 'R', 'B'}
<b>Output:</b> 1
<b>Explaination:</b> First 'R' and 'G' makes 'B'. 
Then 'B' and 'R' makes 'G' and that 'G' 
with 'B' at index 2 makes 'R', Now the 'R' 
and the last 'B' makes 'G'.</pre>

<b>Example 2:</b>

<pre><b>Input:</b> n = 2
a = {'R', 'R'}
<b>Output:</b> 2
<b>Explaination:</b> There are two 'R' s. So 
they cannot change to anything else.</pre>

<b>Your Task:</b><br>
You do not need to read input or print anything. Your task is to complete the function <b>findMin()</b> which takes n and a as input parameters and retunrs the minimum number of smurfs existing at the end.

<b>Expected Time Complexity:</b> O(n)<br>
<b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>
1 ≤ n ≤ 1000


<hr>

### Tags
- **Topic Tags:** `Puzzles`
- **Company Tags:** `None`

### Related Articles
- [Find Minimum Elements Considering Possible Transformations](https://www.geeksforgeeks.org/find-minimum-elements-considering-possible-transformations/)
