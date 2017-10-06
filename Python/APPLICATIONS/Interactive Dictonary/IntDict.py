import json

dictread = json.load(open("data.json",'r'))

#try:
#    print(dictread[input("Enter a Word : ")])
#except Exception as e:
#    print("No Such word ")

def translate(word):
    if word in dictread:
        print(dictread[word])
    else:
        print("No Such word exist")

word = input("Enter a word:")

translate(word.lower())
