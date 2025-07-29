<h1 align="center">Techfest and the Queue</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.34%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 38K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A Techfest is underway, and each participant is given a ticket with a unique number. Organizers decide to award prize points to everyone who has a ticket ID between <b>a</b> and <b>b</b> (<b>inclusive</b>). The points given to a participant with ticket number <b>x</b> will be the <b>sum of powers of the prime factors </b>of <b>x</b>.

For instance, if points are to be awarded to a participant with ticket number <b>12</b>, the amount of points given out will be equal to <b>the sum of powers in the prime factorization </b>of <b>12</b> (<b>2<sup>2</sup> × 3<sup>1</sup></b>), which will be <b>2 + 1 = 3</b>.

Given <b>a</b> and <b>b</b>, determine the sum of all the points that will be awarded to the participants with ticket numbers between <b>a</b> and <b>b</b> (<b>inclusive</b>).

<b>Example 1:</b>

<pre><b>Input: <br>a</b> = 9<br><b>b</b> = 12
<b>Output: <br></b>8
<b>Explanation: <br></b>For 9, prime factorization is:3<sup>2</sup> <br>So, sum of the powers of primes is: 2
For 10, prime factorization is : 2<sup>1</sup>x5<sup>1</sup> 
So, sum of the powers of primes is: 2
For 11, prime factorization is : 11<sup>1</sup> 
So, sum of the powers of primes is: 1
For 12, prime factorization is : 2<sup>2</sup>x 3<sup>1</sup> 
So, sum of powers of primes is: 3
Therefore the total sum is 2+2+1+3=8.
</pre>

<b>Example 2:</b>

<pre><b>Input: <br></b>a = 24, b = 27
<b>Output: <br></b>11
<b>Explanation: <br></b>For 24, prime factorization is: 2<sup>3</sup>x3<sup>1 <br></sup>So, sum of the powers of primes is: 4
For 25, prime factorization is : 5<sup>2</sup> <br>So, sum of the powers of primes is: 2
For 26, prime factorization is : 13<sup>1</sup>x2<sup>1</sup> <br>So, sum of the powers of primes is: 2
For 27, prime factorization is : 3<sup>3</sup>  <br>So, sum of powers of primes is: 3
Therefore the total sum is 4+2+2+3=11.</pre>

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>sumOfPowers</b><b>() </b>which takes <b>a</b> and <b>b</b> as input parameters and returns the <b>sum </b>of the power of <b>primes </b>that occur in <b>prime factorization </b>of the numbers between <b>a </b>to <b>b (inclusive)</b>.

<b>Expected Time Complexity: </b>O( b*log(b) )<br><b>Expected Space Complexity: </b>O( b*log(b) )

<b>Constraints:</b><br>1 <= a <= b <= 2x10<sup>5</sup><br>1 <= b-a <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Prime Number` `sieve`
- **Company Tags:** `None`

### Related Articles
- [Sieve Of Eratosthenes](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)
