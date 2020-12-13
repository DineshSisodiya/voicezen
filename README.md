# voicezen
voicezen screener problem solutions

formula : `Math.pow(length, 2) * Math.pow((frequency - 1), 0.33)`
1. brute force solution
  first we need to generate all the substring from read text from random_text.txt file and for that the simple solution is to use 3 foreach loops like this
 
  ```python
  str = string
  len = length of the string
  for x in range(1, len+1) :
    for y in range(n-x+1): 
        i = y + x - 1
        sub_str = ""
        for (z = y; z <= i; z++) 
            sub_str += str[z]
  ```
  so the time complexity will be O(n<sup>3</sup>) 
  
 2. we can generate all the substrings in O(n<sup>2</sup>) time complexity
  ```python
  for i in range(len):
    sub_str=""
    for j in range(i,len):
        sub_str+=str[j]
  ```
 
 then to find the highest scored string using the formula these string can be processed with hash map in (not good solution) or trie(optmial soltion) data structure.
 in case of hash map if substring string length is very long it won't be efficient. 
 
 so we will store all the sub strings into TRIE data structure
 if we observe carefully, then rather than generating all the substrings we can generate less no. of substrings like this and tweak the TRIE strutcure a little bit to cover all the strings
 for ex: 
  `str = abac`
  then generated substrings will be 
  <br>a. in normal case
  ` 
    a
    ab
    aba
    abac
    b
    ba
    bac
    a
    ac
    c
   `
  <br>b. in optmial method
  `
    abac
    bac
    ac
    c
  `
  so clearly we can see that in second method (b) we are generation only 4 substrings (equal to string length) very less compared to first method (a)
  so we can save iterations and storage space in this way.
  to cover all other substrings we will mark the frequency = 1 intially in trie node. TRIE structure would look like this
  ```python
  class TrieNode:
    def __init__(self, value): 
        self.value = value
        self.freq = 1
        self.next = {}
        self.parent = None
  ```
  
 by using DFS we will traverse this complete TRIE to find highest scored substring with the formula given and time complexity for DFS is O(N+E) where N is the number of nodes and E is the number of edges.
 to get the actual substring we maintain the node with highest score and use it to traverse back to top and reverse it to get the actual substring.
 
 to calculate score for 3000 characters it takes ~ 1 minute.
 
 
 
 ## how to run program:
 run like normal python file with command : `python main.py`
 it will show instruction to follow on command line.
 enter any choice given in instruction and program will do rest of the things.
 
 I've added the random_text.txt file already because wirting 3GB file taking very long time in python. so for checking the other part first you should enter 2 as a input     choice in command line.


