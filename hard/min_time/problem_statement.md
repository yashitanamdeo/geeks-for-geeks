<h1 align="center">Min Time</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.75%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>locations[]</b> of size <b>n</b> where<b> locations[i]</b> represents the location of the <b>i<sup>th</sup></b> fruit on the <b>x-axis</b> and also given an array <b>types[]</b>  where <b>types[i]</b> is an <b>integer</b> which represents the type of the <b>i<sup>th</sup></b> fruit. You are initially at coordinate<b> 0</b> and you have to collect <b>all</b> the fruits and then return back to coordinate <b>0</b> again. To move <b>1</b> unit on the x-axis requires <b>1</b> second of time. The only condition is that you have to collect the fruits in a <b>non-decreasing order</b> of their <b>types[i] </b>(for example if <b>i<sup>th</sup></b> fruit has type[i]=1 and<b> j<sup>th</sup> </b>fruit has type[j]=2 then <b>i<sup>th</sup></b> fruit has to be picked before <b>j<sup>th</sup></b> fruit). Find <b>minimum time</b> to collect all fruits in the non-decreasing<b> order</b> of their types and return back to coordinate <b>0</b>.

<b>Note</b>: You can assume it takes no time to pick up fruit and the location of a fruit can be <b>negative</b> also.

<b>Example 1:</b>

<pre><b>Input:</b>
n=4
locations={1,3,5,7}
types={1,2,3,1}
<b>Output:<br></b>18
<b>Explanation:</b>
You start at x=0 and move to x=7 and 
in the way pick fruits of type 1 at x=1 
and x=7 and it took total 7 seconds to 
move from 0->7 now you move to x=3 
in 4 seconds and than to x=5 in 2 seconds 
and than return back to x=0 in 5 seconds.
So overall it took 18 seconds(7+4+2+5).</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
n=4
locations={-4,-3,1,-8}
types={4,2,4,5}
<b>Output:<br></b>24
<b>Explanation:</b>
The optimal way is to way go to x=-3 
in starting than 1 and follow path 
like this  (1)->(-4)->(-8)->(0) and 
total time it takes is 24 .</pre>

<b>Your Task</b>:<br>You don't need to read input or print anything. Your task is to complete the function <b>minTime() </b>which takes an integer <b>n</b>, integer array<b> locations</b> and <b>types</b> and you have to return <b>minimum time</b> to collect all fruits.

<b>Expected Time Complexity:</b> O(n)<br><b>Expected Space Complexity:</b> O(n)

<b>Constraints:</b><br>1<=<b>n</b><=10<sup>5</sup><br>-10<sup>9</sup><=<b>locations[i]</b><=10<sup>9</sup><br>1<=<b>types[i]</b><=10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `None`
