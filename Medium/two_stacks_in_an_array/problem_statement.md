<h1 align="center">Two Stacks in an Array</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.49%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 169K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Your task is to implement  2 stacks in one array efficiently. You need to implement 4 methods.

<b>twoStacks : </b>Initialize the data structures and variables to be used to implement  2 stacks in one array.<br><b>push1 </b>: pushes element into the first stack.<br><b>push2 </b>: pushes element into the second stack.<br><b>pop1 </b>: pops an element from the first stack and returns the popped element. If the first stack is empty, it should return -1.<br><b>pop2 </b>: pops an element from the second stack and returns the popped element. If the second stack is empty, it should return -1.<br>

<b>Examples:</b>

<pre><b>Input:
</b>push1(2)
push1(3)
push2(4)
pop1()
pop2()
pop2()
<b>Output: </b>[3, 4, -1]<b>
Explanation:
</b>push1(2) the stack1 will be {2}
push1(3) the stack1 will be {2,3}
push2(4) the stack2 will be {4}
pop1()   the poped element will be 3 from stack1 and stack1 will be {2}
pop2()   the poped element will be 4 from stack2 and now stack2 is empty
pop2()   the stack2 is now empty hence returned -1.</pre>

<pre><b>Input:
</b>push1(1)
push2(2)<br>pop1()
push1(3)
pop1()
pop1()
<b>Output: </b>[1, 3, -1]<b>
Explanation:
</b>push1(1) the stack1 will be {1}
push2(2) the stack2 will be {2}<br>pop1()   the poped element will be 1 from stack1 and stack1 will be empty<br>push1(3) the stack1 will be {3}
pop1()   the poped element will be 3 from stack1 and stack1 will be empty<br>pop1()   the stack1 is now empty hence returned -1.<br></pre>

<pre><b>Input:
</b>push1(2)
push1(3)
push1(4)
pop2()
pop2()
pop2()
<b>Output: </b>[-1, -1, -1]<b>
Explanation:
</b>push1(2) the stack1 will be {2}
push1(3) the stack1 will be {2,3}
push1(4) the stack1 will be {2,3,4}
pop2()   the stack2 is empty hence returned -1.<br>pop2()   the stack2 is empty hence returned -1.<br>pop2()   the stack2 is empty hence returned -1.</pre>

<b>Constraints:</b><br>1 <= number of queries <= 10<sup>4</sup><br>1 <= number of elements in the stack <= 100<br>The sum of the count of elements in both the stacks < size of the given array

## Expected Complexities
- Time Complexity: O(1)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Stack` `Data Structures`
- **Company Tags:** `Microsoft` `Samsung` `Snapdeal` `24*7 Innovation Labs`

### Related Articles
- [Implement Two Stacks In An Array](https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/)

### Related Interview Experiences
- [Microsoft Interview Experience Set 151 Sde 2 3 5 Years Experience](httpss://www.geeksforgeeks.org/microsoft-interview-experience-set-151-sde-2-3-5-years-experience/)
