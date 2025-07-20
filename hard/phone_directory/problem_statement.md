<h1 align="center">Phone directory</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 25.68%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 45K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a list of contacts <b>contact[]</b> of length <b>n</b> where each contact is a string which exist in a phone directory and a query string <b>s</b>. The task is to implement a search query for the phone directory. Run a search query for each prefix <b>p</b> of the query string <b>s </b>(<i>i.e.</i> from  index 1 to |s|) that prints all the distinct contacts which have the same prefix as p in <b>lexicographical increasing order</b>. Please refer the explanation part for better understanding.<br><b>Note: </b>If there is no match between query and contacts, print "0".

<b>Example 1:</b>

<pre><b>Input:</b> 
n = 3
contact[] = {"geeikistest", "geeksforgeeks", 
"geeksfortest"}
s = "geeips"
<b>Output:</b>
geeikistest geeksforgeeks geeksfortest
geeikistest geeksforgeeks geeksfortest
geeikistest geeksforgeeks geeksfortest
geeikistest
0
0
<b>Explaination:</b> By running the search query on 
contact list for "g" we get: "geeikistest", 
"geeksforgeeks" and "geeksfortest".
By running the search query on contact list 
for "ge" we get: "geeikistest" "geeksforgeeks"
and "geeksfortest".
By running the search query on contact list 
for "gee" we get: "geeikistest" "geeksforgeeks"
and "geeksfortest".
By running the search query on contact list 
for "geei" we get: "geeikistest".
No results found for "geeip", so print "0". 
No results found for "geeips", so print "0".</pre>

<b>Your Task:</b><br>You do not need to read input or print anything. Your task is to complete the function <b>displayContacts()</b> which takes <b>n, contact[ ] </b>and<b> s</b> as input parameters and returns a list of list of strings for required prefixes. If some prefix has no matching contact return "0" on that list.

<b>Expected Time Complexity:</b> O(|s| * n * max|contact[i]|)<br><b>Expected Auxiliary Space:</b> O(n * max|contact[i]|)

<b>Constraints:</b><br>1 ≤ T ≤ 100, T = number of test cases<br>1 ≤ n ≤ 50<br>1 ≤ |contact[i]| ≤ 50<br>1 ≤ |s| ≤ 6


<hr>

### Tags
- **Topic Tags:** `Map` `Trie` `Data Structures` `Advanced Data Structure`
- **Company Tags:** `Amazon` `Microsoft` `Snapdeal`

### Related Articles
- [Implement A Phone Directory](https://www.geeksforgeeks.org/implement-a-phone-directory/)

### Related Interview Experiences
- [Microsoft Interview Experience Set 128 Campus Internship](https://www.geeksforgeeks.org/microsoft-interview-experience-set-128-campus-internship/)
