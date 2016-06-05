# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

string = sys.stdin.readline()

flags = [False] * 26

for w in string:
    if w.isalpha():
        i = ord(w.lower()) - ord('a') 
        flags[i] = True;

res = 'pangram'
for flag in flags:
    if not flag:
        res = 'not pangram'
        break
        
print res
