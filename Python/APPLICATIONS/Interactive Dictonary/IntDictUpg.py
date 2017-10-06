import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

dictread = json.load(open("data.json",'r'))
def translate(word):
    if word in dictread:
        print(dictread[word])
    elif len(get_close_matches(word,dictread.keys(),n=5,cutoff=0.8))>0:
        lstmatches = get_close_matches(word,dictread.keys(),n=5,cutoff=0.8)
        #print(dictread[lstmatches[0]])
        yn = input("Did you mean %s ? Enter Y for Yes/N for No :" %lstmatches[0])
        if(yn.lower() == 'y'):
            print(dictread[lstmatches[0]])
        elif(yn.lower()=='n'):
            otherChoice = input("Did you meant any of these : %s" %lstmatches)
            if otherChoice in dictread:
                print(dictread[otherChoice.lower()])
            else :
                print ("Wrong choice selected")
        else :
            print("please check you entered value")

    #for words in lstmatches:

word = input("Enter a word:")

translate(word.lower())
