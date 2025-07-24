<h1 align="center">Remove and Reverse</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.43%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 31K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>S </b>which consists of only lowercase English alphabets, you have to perform the below operations:<br>
If the string <b>S</b> contains any repeating character, remove the first repeating character and reverse the string and again perform the above operation on the modified string, otherwise, you stop.<br>
You have to find the final string.

<b>Example 1:</b>

<pre><b>Input:</b> S = "abab"
<b>Output:</b> ba
<b>Explanation:</b>
<b>In 1st operation:</b> The first repeating 
character is a. After Removing the first 
character, S = "bab". After Reversing the 
string, S = "bab".
<b>In 2nd operation:</b> The first repeating 
character is b. After Removing the first 
character, S = "ab". After Reversing the 
string, S = "ba".
Now the string S does not contain any 
repeating character.</pre>

<b>Example 2:</b>

<pre><b>Input:</b> S = "dddd"
<b>Output:</b> d
<b>Explanation:
In 1st operation:</b> The first repeating character 
is d. After Removing the first character, 
S = "ddd". After Reversing the string, S = "ddd". 
<b>In 2nd operation:</b> Similarly, S="dd".
<b>In 3rd operation:</b> Similarly, S="d".
Now the string S does not contain any repeating character.
</pre>

<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>removeReverse( )</b> which accepts a string <b>S</b> input parameter and returns the modified string.

<b>Expected Time Complexity:</b> O(|S|)<br>
<b>Expected Auxiliary Space:</b> O(K), K <= 26.

<b>Constraints:</b><br>
The string contains only lowercase English alphabets.<br>
1 <u><</u> |S| <u><</u> 10<sup>5</sup><br>
|S| denotes the length of the string S.


<hr>

### Tags
- **Topic Tags:** `two-pointer-algorithm` `Arrays` `Strings` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Remove Repeating Chars And Reverse String Until No Repetitions](https://www.geeksforgeeks.org/remove-repeating-chars-and-reverse-string-until-no-repetitions/)
