<h1 align="center">Easy Task</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.05%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b> whose length is <b>n</b> and array <b>queries</b> of length <b>q</b> where each elements of queries is either of <b>type</b> <b>1</b> <b>query</b> or <b>type 2 query</b> which is explained ahead.

There are two types of query.<br>
<br>
<b>Query type 1</b> : <b>["1",ind,char]</b>  "<b>1"</b> denotes this is type <b>1 query</b>. In this query you have to change the character at index <b>ind </b>in s<b> </b>to character <b>char</b>.<b>(Data type of ind,char is string in input)</b><br>
<br>
<b>Query Type 2:</b> <b>["2",left,right,k]</b>  "<b>2" </b>denotes this is type <b>2 query</b>. In this query you have to return <b>kth lexographically</b> largest character  in the subtring of <b>s (it is the kth largest </b>character<b> in sorted order , not the kth distinct </b>character<b>)</b> starting from index <b>left</b> and ending at index<b> right both left and right are inclusive</b>. <b>(Data type of left,right,k is string in input)</b>

You have to perform each query in the <b>same order</b> as given in <b> queries</b> and return an array <b>res</b> such that res array contains <b>the answer for each type2 query</b> <b>in same order as it appeared in queries</b>.

<b>Note</b> : <b>0</b> based indexing is used.

<b>Example 1:</b>

<pre><b>Input:</b>
<b>n</b>=4
<b>s</b>="abab"
<b>q</b>=2
<b>queries</b>={{"1","2","d"},{"2","1","3","1"}}
<b>Output:</b> 
{"d"}
<b>Explanation:</b>
First query is of type 1 so after changing character at index 2 
to d  s becomes <b>abdb</b> . Now Second query is of type 2 in which 
the 1st(k=1) lexographically largest character is <b>"d" in substring "bdb"(s[1:3])</b>. So we 
returned a array with result of type 2 query <b>{"d"}</b>.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
<b>n</b>=3
<b>s</b>="aaa"
<b>q</b>=3
<b>querie</b>s={{"1","1","e"},{"1","2","c"},{"2","1","2","2"}}
<b>Output:</b>
{"c"}
<b>Explanation:</b>
After applying first two queries s becomes <b>aec</b>. Now for 
the last query which is a type 2 second largest character 
in subtring s starting from index 1 to ending at index 2 is <b>"c"</b>.</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>easyTask()</b> which takes an integer <b>n</b>,string <b>s</b>,an integer <b>q</b> and an array <b>queries</b> which contains  queries of<b> </b><b>type1</b> and <b>type2</b>  respectively and returns an array <b>res</b> such that res array contains the <b>answer for each type2 query in</b> <b>same order as it appeared in queries.</b>

<b>Expected Time Complexity: O(N+(Q*logN))<br>
Expected Space Complexity: O(N)</b>

<br>
<b>Constraints:</b><br>
1<=<b>n</b><=5*10^4<br>
1<=<b>q</b><=10^5<br>
0<=<b>int(left)</b><=<b>int(right)</b><=n-1<br>
0<=<b>int(index)</b><=n-1<br>
1<=<b>int(k)</b><=right-left+1<br>
<b>s</b> and <b>char</b> contains lowercase <b>english letters</b><br>
The sum of <b>n</b> over all test cases won't exceed <b>5*10^4.</b>


<hr>

### Tags
- **Topic Tags:** `Segment-Tree` `Advanced Data Structure`
- **Company Tags:** `None`
