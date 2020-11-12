from collections import OrderedDict
import string
from collections import deque
from tabulate import tabulate
from decimal import Decimal 
import numpy as np
import networkx as nx
import math  
import operator

grammar = OrderedDict()
def parser(parsetbl,Istring,startvar,non_terminals,terminals,tab_list):#parsing alrotihm function
    count=0
    numer=[]
    lengthof=len(tab_list)
    new_lengthof=int(math.sqrt(lengthof))
    i=1
    for i in range(new_lengthof):
        if(i==new_lengthof):
            break 
        else:
            numer.append(new_lengthof*i)
    #for i, val in enumerate(numer): 
    #    numer[i]=val+4
    row={}
    row=dict(zip(terminals,numer))
    clist2=[]
    count=0
    for i in numer:
        clist2.append(count)
        count+=1
    column={}
    column=dict(zip(terminals,clist2))    
    stack=[]
    stack.append("$")

    
    for i in Istring:
            print(stack)
            #last = operator.itemgetter(-1)
            j=stack[-1]
            if (i==j) and ((i=="$") and (j=="$")):

                print("complete parsing")

                break
            
            else:
                key1=column.get(i)
                key2=row.get(j)
                key=key1+key2
                result=tab_list[key]
                if(result=="<"):
                    print("appeneded")
                    stack.append(i)
                elif(result==">"):
                    while(True):
                        print("popped")
                        stack.pop()
                        print(stack)
                        j=stack[-1]
                        key1=column.get(i)
                        key2=row.get(j)
                        key=key1+key2
                        result=tab_list[key]
                        
                        if(result=="<"):
                            print("appeneded")
                            stack.append(i)
                            print(stack)
                            break
                        if(result=="-"):
                            print("\n\nSuccessful parsing")
                            break

def find(point,grammar):
    for key in grammar.keys():
        for exp in grammar[key]:
                item_list=[]
                item_list[:0]=exp 
                for i, item in enumerate(item_list[:-1]):
                    if(item==point):
                        if(key==item_list[i-1]):
                            return(">")
                        elif(key==item_list[i+1]):
                            return("<")
                        
def op_table(grammar,terminals,non_terminals):
    tab_list=[]
    x= Decimal('Infinity') # this is id
    
    for i in terminals:
        for j in terminals:
            if (i=="x" and j=="x") or (i=="$" and j=="$"):
                tab_list.append("-")
            elif (i=="x" and j!="x") or (i!="$" and j=="$"):
                tab_list.append(">")
            elif (i!="x" and j=="x") or (i=="$" and j!="$"):
                tab_list.append("<")
            elif (i==j):
                tab_list.append(find(i,grammar))
            elif(i!=j):
                for x, item in enumerate(terminals[:-1]):
                    for opr in range(len(terminals)-1):
                        if(x+opr<len(terminals)):
                            if(i==item and j==terminals[x+opr]):
                                tab_list.append("<")
                            elif(i==terminals[x+opr] and j==item):
                                tab_list.append(">")
            else:
                tab_list.append("@")
    result=np.reshape(tab_list, (len(terminals), len(terminals)))
    header=[]
    for x in terminals:
        header.append(x)
    print(tabulate(result,header,tablefmt="orgtbl"))
    final=tabulate(result,header)
    input_string=""
    inputtt=open('F:\EBOOKS\Third year\Compiler design\lab\string.txt')
    for i in inputtt:
        input_string=input_string.join(i)
    print("This is the input string",input_string)
    print("\n\nparsing starts\n\n")
    parser(final,input_string,start,non_terminals,terminals,tab_list)

        



def check_dict(grammar,terminals,non_terminals):
    count=0
    for key in grammar.keys():
        for exp in grammar[key]:
            item_list=[]
            item_list[:0]=exp 
            for i, item in enumerate(item_list[:-1]):
                if (item=="Epsilon"):
                    print("Contains ϵ, NOT A OPERATOR GRAMMAR ")
                    break
                
                if(item in non_terminals and item_list[i+1] in non_terminals):
                    print("TWO TERMINALS SIDE BY SIDE")
                    print("Changed grammar")
                    itemnew=grammar.get(item)
                    express=str(exp)
                    for temp in itemnew:
                        grammar[key]=express.replace(express,temp)
                    show_dict(grammar)
                elif(item not in non_terminals and item_list[i+1] not in non_terminals):
                    grammar[key]=exp
                
                else:
                    count=count+1
    if(count!=0):
        print("Operator Grammar check")
        op_table(grammar,terminals,non_terminals)

def isterminal(char):
    if(char.isupper() or char == "`"):
        return False
    else:
        return True
def insert(grammar, lhs, rhs):
    if(lhs in grammar and rhs not in grammar[lhs] and grammar[lhs] != "null"):
        grammar[lhs].append(rhs)
    elif(lhs not in grammar or grammar[lhs] == "null"):
        grammar[lhs] = [rhs]
    return grammar
def show_dict(dictionary):
    for key in dictionary.keys():
        print(key+"  :  ", end = "")
        for item in dictionary[key]:
            if(item == "`"):
                print("Epsilon, ", end = "")
            else:
                print(item+"| ", end = "")
        print("\b\b")
f = open('F:\EBOOKS\Third year\Compiler design\lab\grammar.txt')
for i in f:
    i = i.replace("\n", "")
    lhs = ""
    rhs = ""
    flag = 1
    for j in i:
        if(j=="~"):
            flag = (flag+1)%2
            continue
        if(flag==1):
            lhs += j
        else:
            rhs += j
    grammar = insert(grammar, lhs, rhs)


terminals = []
for i in grammar:
    for rule in grammar[i]:
        for char in rule:
            
            if(isterminal(char) and char not in terminals):
                terminals.append(char)
non_terminals = list(grammar.keys())
start = list(grammar.keys())[0]

terminals.append("$")
print(terminals,"TERMINAS")
show_dict(grammar)
check_dict(grammar,terminals,non_terminals)