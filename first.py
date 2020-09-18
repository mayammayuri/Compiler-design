terminal = ["+","*","ε","id","(",")"]
notterminal = ["E","E'","T","T'","F"]
grammar = {
"E":[("T","E'")],
"E'":[("+","T","E'"),("ε",)],
"T":[("F","T'")],
"T'":[("*","F","T'"),("ε",)],
"F":[("(","E",")"),("id",)]
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

def printFirsts():
    print("First:")
    for nont in notterminal:
        print(first(nont))


print("GRAMMAR IS\n")
printGrammar()
printFirsts()
