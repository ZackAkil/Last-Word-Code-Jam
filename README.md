# Last Word - Code Jam Solution
Solution to the last word puzzle from [google code jam Round 1A 2016](https://code.google.com/codejam/contest/4304486/dashboard)

##The problem
On the game show The Last Word, the host begins a round by showing the contestant a string S of uppercase English letters. The contestant has a whiteboard which is initially blank. The host will then present the contestant with the letters of S, one by one, in the order in which they appear in S. When the host presents the first letter, the contestant writes it on the whiteboard; this counts as the first word in the game (even though it is only one letter long). After that, each time the host presents a letter, the contestant must write it at the beginning or the end of the word on the whiteboard before the host moves on to the next letter (or to the end of the game, if there are no more letters).

For example, for S = CAB, after writing the word C on the whiteboard, the contestant could make one of the following four sets of choices:

- put the A before C to form AC, then put the B before AC to form BAC
- put the A before C to form AC, then put the B after AC to form ACB
- put the A after C to form CA, then put the B before CA to form BCA
- put the A after C to form CA, then put the B after CA to form CAB

The word is called the last word when the contestant finishes writing all of the letters from S, under the given rules. The contestant wins the game if their last word is the last of an alphabetically sorted list of all of the possible last words that could have been produced. For the example above, the winning last word is CAB (which happens to be the same as the original word). For a game with S = JAM, the winning last word is MJA.

You are the next contestant on this show, and the host has just showed you the string S. What's the winning last word that you should produce?

##Solution theory
The script executes a brute force play through of each game using the tactic of placing the next character at the front if it is of lower or equal alphabetical order to the current character at the front.

##Usage
To use the solution: run the python script from a terminal passing it the name of the input file followed by the desired name of the output file.   

```
$ /User python last_word.py C-small-practice.in small-output.out
```
