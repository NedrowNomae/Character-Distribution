"""
distribution.py
Author: Eamon
Credit: stackoverflow

Assignment: character distribution

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
#from collections import Counter
string = input("Please enter a string of text (the bigger the better): ")
letters = list(string)
q=0
w=0
e=0
r=0
t=0
y=0
u=0
i=0
o=0
p=0
a=0
s=0
d=0
f=0
g=0
h=0
j=0
k=0
l=0
z=0
x=0
c=0
v=0
b=0
n=0
m=0
Q = len(letters)
for W in range(0,Q):
    if letters[W] == "q" or letters[W] == "Q":
        q = q + 1
    elif letters[W] == "w" or letters[W] == "W":
        w = w + 1
    elif letters[W] == "e" or letters[W] == "E":
        e = e + 1
    elif letters[W] == "r" or letters[W] == "R":
        r = r + 1
    elif letters[W] == "t" or letters[W] == "T":
        t = t + 1
    elif letters[W] == "y" or letters[W] == "Y":
        y = y + 1
    elif letters[W] == "u" or letters[W] == "U":
        u = u + 1
    elif letters[W] == "i" or letters[W] == "I":
        i = i + 1
    elif letters[W] == "o" or letters[W] == "O":
        o = o + 1
    elif letters[W] == "p" or letters[W] == "P":
        p = p + 1
    elif letters[W] == "a" or letters[W] == "A":
        a = a + 1
    elif letters[W] == "s" or letters[W] == "S":
        s = s + 1
    elif letters[W] == "d" or letters[W] == "D":
        d = d + 1
    elif letters[W] == "f" or letters[W] == "F":
        f = f + 1
    elif letters[W] == "g" or letters[W] == "G":
        g = g + 1
    elif letters[W] == "h" or letters[W] == "H":
        h = h + 1
    elif letters[W] == "j" or letters[W] == "J":
        j = j + 1
    elif letters[W] == "k" or letters[W] == "K":
        k = k + 1
    elif letters[W] == "l" or letters[W] == "L":
        l = l + 1
    elif letters[W] == "z" or letters[W] == "Z":
        z = z + 1
    elif letters[W] == "x" or letters[W] == "X":
        x = x + 1
    elif letters[W] == "c" or letters[W] == "C":
        c = c + 1
    elif letters[W] == "v" or letters[W] == "V":
        v = v + 1
    elif letters[W] == "b" or letters[W] == "B":
        b = b + 1
    elif letters[W] == "n" or letters[W] == "N":
        n = n + 1
    elif letters[W] == "m" or letters[W] == "M":
        m = m + 1
list = [q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m]
E = len(list)
sor = list
T = 0
for R in range(0,E-1):
    if sor[R] == 0:
        T = T + 1
for Y in range(0,T):
    sor.remove(0)
#print(T)
#print("sor: " + str(sor))
ros = sorted(sor)
ros.reverse()
#print("ros" + str(ros))
numms = []
for S in ros:
    if S not in numms:
        numms.append(S)
#print(numms)
qwert = ""
A = len(numms)
for D in range(0,A):
    if numms[D] == a:
        qwert = a*"a"
        print(qwert)
    if numms[D] == b:
        qwert = b*"b"
        print(qwert)
    if numms[D] == c:
        qwert = c*"c"
        print(qwert)
    if numms[D] == d:
        qwert = d*"d"
        print(qwert)
    if numms[D] == e:
        qwert = e*"e"
        print(qwert)
    if numms[D] == f:
        qwert = f*"f"
        print(qwert)
    if numms[D] == g:
        qwert = g*"g"
        print(qwert)
    if numms[D] == h:
        qwert = h*"h"
        print(qwert)
    if numms[D] == i:
        qwert = i*"i"
        print(qwert)
    if numms[D] == j:
        qwert = j*"j"
        print(qwert)
    if numms[D] == k:
        qwert = k*"k"
        print(qwert)
    if numms[D] == l:
        qwert = l*"l"
        print(qwert)
    if numms[D] == m:
        qwert = m*"m"
        print(qwert)
    if numms[D] == n:
        qwert = n*"n"
        print(qwert)
    if numms[D] == o:
        qwert = o*"o"
        print(qwert)
    if numms[D] == p:
        qwert = p*"p"
        print(qwert)
    if numms[D] == q:
        qwert = q*"q"
        print(qwert)
    if numms[D] == r:
        qwert = r*"r"
        print(qwert)
    if numms[D] == s:
        qwert = s*"s"
        print(qwert)
    if numms[D] == t:
        qwert = t*"t"
        print(qwert)
    if numms[D] == u:
        qwert = u*"u"
        print(qwert)
    if numms[D] == v:
        qwert = v*"v"
        print(qwert)
    if numms[D] == w:
        qwert = w*"w"
        print(qwert)
    if numms[D] == x:
        qwert = x*"x"
        print(qwert)
    if numms[D] == y:
        qwert = y*"y"
        print(qwert)
    if numms[D] == z:
        qwert = z*"z"
        print(qwert)