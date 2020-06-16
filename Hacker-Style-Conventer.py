#coding:utf-8
import random
def main():
    I = Input()                                     # Read input string
    R = converter(list(I))                          # string to list, then replace list elements
    strOutput = "" + "".join(R)                     # return list to output string
    return strOutput

def Input():
    L = input()
    return L


def converter(stringList):
    for i in range(0, len(stringList)):
        
        # random upper or lower
        if random.randint(0,1):
            stringList[i] = upper(stringList[i])
        else:
            stringList[i] = lower(stringList[i])
            pass

        # replace character
        if stringList[i] == 'a':
            if random.randint(0,1):
                stringList[i] = "@"
                pass
            else:
                stringList[i] = "λ"
                pass

        elif stringList[i] == 'A':
            if random.randint(0,1):
                stringList[i] = "4"
                pass
            else:
                stringList[i] = "λ"
                pass

        elif stringList[i] == 'b':
            stringList[i] = "6"
            pass

        elif stringList[i] == 'B':
            stringList[i] = "8"
            pass

        elif stringList[i] == 'i':
            stringList[i] = "1"
            pass

        elif stringList[i] == 'I':
            stringList[i] = "1"
            pass

        elif stringList[i] == 'l':
            stringList[i] = "1"
            pass

        elif stringList[i] == 'o':
            stringList[i] = "0"
            pass

        elif stringList[i] == 'O':
            stringList[i] = "0"
            pass

        elif stringList[i] == 's':
            stringList[i] = "$"
            pass
        
        elif stringList[i] == 'S':
            stringList[i] = "$"
            pass
        
        #elif stringList[i] == 'y':
        #    stringList[i] = "¥"
            pass

        #elif stringList[i] == 'Y':
        #    stringList[i] = "¥"
            pass
   

    return stringList

def lower(char):
    char_ascii = ord(char)
    if 65 <= char_ascii <= 90:
        char_ascii = char_ascii + 32
    return chr(char_ascii)

def upper(char):
    char_ascii = ord(char)
    if 97 <= char_ascii <= 122:
        char_ascii = char_ascii - 32
    return chr(char_ascii)

if __name__=="__main__":
    print("--------------------------------------")
    print("Welcome to Hacker style converter, Input Ctrl+C to exit.")
    while 1:
        print("--------------------------------------")
        print("Input your normal sentence or name:")
        print("Output:", main())
        print("--------------------------------------")
        pass
    
