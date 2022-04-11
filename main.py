import wordList


words = []
deleteWords = []
greenLetters = []



def clearList():
    for delWord in deleteWords:
        try:
            words.remove(delWord)
        except: 
            pass
    print("done clearwords")
    
    

useExtraWords = input("Would you like to limit the search to the official Wordle wordlist? (y/n)")

if useExtraWords == 'y':
    #words = wordList.tempList
    words = wordList.official
else:
    words = wordList.official + wordList.extra

redLetters = input("Which letters have been eliminated from the puzzle? Do not use a sapce or comma to seperate the letters.  ")

for letter in redLetters:
    for myWord in words:
        if letter in myWord:
            #check if my word is already in deletewords before appneding
            deleteWords.append(myWord)
            
clearList()
deletewords = []


greenCount = input("How many green letters do you know?")
greenLetters = []


for i in range(int(greenCount)):
    toAdd = [
        input("What letter do you know the position of? "),
        int(input("What position is it in? "))
    ]
    greenLetters.append(toAdd)
    

for i in greenLetters:
    for myWord in words:
        if myWord[i[1]-1] != i[0]:
            deleteWords.append(myWord)
            
clearList()   
deletewords = []

    
yellowCount = input("How many yellow letters do you know?")
yellowLetters = []

for i in range(int(yellowCount)):
    toAdd = [
        input("What letter is confirmed but in the wrong position? "),
        input("What positions do you know it is NOT in? ")
    ]
    yellowLetters.append(toAdd)
    
for i in yellowLetters:
    for j in i[1]:
        j = int(j)
        for myWord in words:
            if myWord[j-1] == i[0]:
                deleteWords.append(myWord)
            if i[0] not in myWord:
                deleteWords.append(myWord)
                
clearList()



print(words, "wordsEnd")
