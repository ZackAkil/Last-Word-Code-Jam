# solution to last word puzzle from code jam Round 1A 2016
# pass command line parameters of input file name and output file name
# e.g python last_word.py A-small-practice.in A-small-practice.out
# By Zack Akil 28/04/2016 

import sys

def lastWord( s ):
   output = "" + s[0]
   for x in range(1, len(s)):
       if ord(output[0]) <= ord(s[x]):
           output = s[x] + output
       else:
           output += s[x]
   return output

print (len(sys.argv))

if len(sys.argv) >=3:
  inputFile = sys.argv[1]
  outputFile = sys.argv[2]
else:
  inputFile = input('Enter input file name: ')
  outputFile = input('Enter output file name: ')

f = open(inputFile, 'r')
rows = int(f.readline())

w = open(outputFile, 'w')
for x in xrange(0,rows):
	w.write('Case #{}: {}'.format(x+1, lastWord(f.readline().rstrip())))
	if x < rows - 1:
		 w.write('\n')
