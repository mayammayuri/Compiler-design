import re
import keyword
commentarr=[]
specialarr=[]
variablearr=[]
numberarr=[]
keywordarr=[]
opparr=[]
libarr=[]
comcon=0
lino=0
 
key=["main()","void","print","int","float","String","iostream","stdio","namespace","std","using","cout","cin"]

 
with open("lab2.txt") as fp: 
    Lines = fp.readlines() 
    for line in Lines: 
        lino=lino+1
        comment=re.search("^//|/\*.*\*/$|\s//|^[(\"]",line) 
        if comment:
            comcon=comcon+1
            commentarr.append(line)
        
        
        for word in line.split(): 
            lib=re.search("^#",word)
            special=re.match("[+]|>>*|<<*|[(\"]+|<|>",word)
            number=re.match("[0-9]",word)
            opp=re.match("[+]",word)
            x = re.findall("\S", word)
            var=re.match("[a-n]|^[int]&^[float]&^[#include]&^[print]&^[main]&^[return]&^[(\"]&^[using namespace std]",word)                       

            if any(w in word for w in key ):
                keywordarr.append(word)
            #if keyword.iskeyword(word):
                #keywordarr.append(word)
            elif var:
                variablearr.append(word)
            if lib:
                libarr.append(line)
            if special:
                specialarr.append(word)
            if number:
                numberarr.append(word)
            if opp:
                opparr.append(word)

    #print("length is:",len(commentarr))
    print("Comments:")
    for i in range(len(commentarr)):
            print("         ",commentarr[i])
    print("Variables:")
    for i in range(len(variablearr)):
            print("         ",variablearr[i])
    print("Numbers :")
    for i in range(len(numberarr)):
            print("         ",numberarr[i])
    print("Operators:")
    for i in range(len(opparr)):
            print("         ",opparr[i])
    print("Special characters:")
    for i in range(len(specialarr)):
            print("         ",specialarr[i])
    print("Keywords:")
    for i in range(len(keywordarr)):
            print("         ",keywordarr[i])
    print("Libraries:")
    for i in range(len(libarr)):
            print("         ",libarr[i])
    


            


 
