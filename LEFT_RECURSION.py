#!/usr/bin/python3
import sys
import string
string.ascii_lowercase
non_terminal=list(string.ascii_lowercase)
op=("+","-","/","*","^","(",")")
x=("|")
n=int(input("Enter the number of terminal :- "))
for i in range(n):
    s=input("Enter the starting terminal :- ")
    p=input("Enter the production  :- ")
    grammer=("grammer is "+s+ "->" +p)
    print(grammer)
    if s[0]==p[0]:
        p=p.split("|")
        p.append("EPS") #THIS IS EPSILON
        print(p)
        print("now the modified grammar with elimination of left recursion")
        f=("1st production is :-"+s+"->"+p[1]+""+s+"`")
        print(f)
        s=("2nd production is :-"+s+"`->"+p[0][1:]+""+s+"`|"+p[-1])
        print(s)
    else:
        print("Grammer is not recursive")
if s in non_terminal:
	print("Grammer is incorrect")
elif s[0]==p[0]:
	print("It Is Recuursive")
elif p[0] in op:
	print("Grammer is not recursive")
else:
	print("Solve")