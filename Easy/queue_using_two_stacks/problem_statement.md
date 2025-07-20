<h1 align="center">Queue using two Stacks</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.89%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 139K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Implement a Queue using 2 stacks<b> s1</b> and<b> s2</b> .<br>A Query <b>q </b>is of 2 Types<br><b>(i)</b> 1 x (a query of this type means  pushing <b>'x'</b> into the queue)<br><b>(ii)</b> 2   (a query of this type means to pop element from queue and print the poped element)

<b>Note :</b> If there is no element return -1 as answer while popping.

<b>Examples :</b>

<pre><b>Input: </b>q=5, queries[][]=[[1, 2], [1, 3], [2], [1, 4], [2]]
<b>Output: </b>[2, 3]<b><br></b><b>Explanation: 
</b>In the first testcase
[1 2] the queue will be [2]
[1 3] the queue will be [2 3]
[2]   poped element will be 2 the queue 
will be [3]
[1 4] the queue will be [3 4]
[2 ]  poped element will be 3.
</pre>

<pre><b>Input: </b>q = 4, queries[][] = [[1, 2], [2], [2], [1, 4]]
<b>Output: </b>[2, -1]
<b>Explanation: 
</b>In the second testcase 
[1, 2] the queue will be [2]
[2]   poped element will be [2] and 
    then the queue will be empty
[2]   the queue is empty and hence -1
[1, 4] the queue will be [4].</pre>

<b>Constraints:</b><br>1 <=<b> </b>q <= 100<br>1 <= x <= 100

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Stack` `Queue` `STL` `Data Structures`
- **Company Tags:** `Flipkart` `Morgan Stanley` `Accolite` `Amazon` `Microsoft` `D-E-Shaw` `Hike` `MakeMyTrip` `Oracle` `Walmart` `Goldman Sachs` `MAQ Software` `Adobe` `InfoEdge` `InMobi`

### Related Articles
- [Queue Using Stacks](https://www.geeksforgeeks.org/queue-using-stacks/)

### Related Interview Experiences
- [Maq Software Interview Experience Set 10 On Campus](https://www.geeksforgeeks.org/maq-software-interview-experience-set-10-on-campus/)
- [Walmart Lab Interview Experience Set 8 Off Campus 3 Years Experience](https://www.geeksforgeeks.org/walmart-lab-interview-experience-set-8-off-campus-3-years-experience/)
- [Makemytrip Interview Experience Set 9 Off Campus For Sr Android Developer](https://www.geeksforgeeks.org/makemytrip-interview-experience-set-9-off-campus-for-sr-android-developer/)
- [Adobe Interview Experience Set 48 Campus](https://www.geeksforgeeks.org/adobe-interview-experience-set-48-campus/)
