import string
import sys
import pandas as pd
from tabulate import tabulate

terminal = ["(","a","ε",")"]
notterminal = ["S","L","L'"]
grammar = {
"S":[("(","L",")"),("a")],
"L":[("S","L'")],
"L'":[(",","S","L"),("ε",)],

}

def isTerminal(s):
    return s in terminal

def isNonTerminal(s):
    return s in notterminal

def findSymbol(s):
    results = {}
    for nont in grammar:#for the grammar 
        for production in grammar[nont]:#for production symbol
            for symbol in production:
                if s in production:
                    try:
                        results[nont]+=[production]
                    except KeyError:
                        results[nont]=[production]
    return results

#for first
def first(s):
    firsts = []
    for production in grammar[s]:   
        if(isTerminal(production[0])):      
            firsts.append(production[0])
        elif(isNonTerminal(production[0])):
            firsts+=first(production[0])
    return firsts



def printGrammar():
    for rule in grammar:
        str_rule = rule + " -> "
        for production in grammar[rule]:
            for symbol in production:
                str_rule+=symbol
            str_rule+="|"
        str_rule = str_rule[:-1]
        print(str_rule)
First_list={}
def First_add( key, value): 
        First_list[key] = value
def printFirsts():
    print("First:")
    for nont in notterminal:
        First_add((nont),(first(nont)))
    df = pd.DataFrame(First_list)
    print(tabulate(df.T, headers="keys"))
    #print(tabulate(First_list),"table")

 
#folloow
def follow(s):
    follows = []
    if s == next(iter(grammar)):
        follows.append("$")
    found = findSymbol(s)
    for nont in found:
        for production in found[nont]:
            if(production.index(s) < len(production)-1):
                nxt = production[production.index(s)+1]
                if(isTerminal(nxt)):
                    follows.append(nxt)
                elif(isNonTerminal(nxt)):
                    nxt = first(nxt)
                    if("ε" in nxt):
                        nxt += follow(nont)
                    follows+= nxt
            else:
                if(s != nont):
                    follows = follow(nont)
    follows = list(set(follows))
    if("ε" in follows):
        follows.remove("ε")
    return follows
Follow_list={}
def Follow_add( key, value): 
        Follow_list[key] = value
def printFollows():
    print("Follow is as follows:")
    for nont in notterminal:
        Follow_add(nont,follow(nont))
        #Follow_list+(nont,follow(nont))

    print(tabulate(Follow_list),"table")
def check_left(p):
    for i in p : 
        if i==p[i]:
            print("the grammar is left recursive")
            non_terminal=list(string.ascii_lowercase)
            op=("+","-","/","*","^","(",")")
            x=("|")
            p=p.split("|")
            p.append("EPS") #THIS IS EPSILO
            print("now the modified grammar with elimination of left recursion")
            f=("1st production is :-"+s+"->"+p[1]+""+s+"`")
            print(f)
            s=("2nd production is :-"+s+"`->"+p[0][1:]+""+s+"`|"+p[-1])
            print(s)
        else:
            print("The grammar is not left recursive")
            break
        

print("GRAMMAR IS\n")
check_left(grammar)
printGrammar()
printFirsts()
printFollows()

