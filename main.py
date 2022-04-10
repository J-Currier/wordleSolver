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

useExtraWords = input("Would you like to limit the search to the official Wordle wordlist? (y/n)")

if useExtraWords == 'y':
    words = wordList.tempList
else:
    words = wordList.official + wordList.extra

redLetters = input("Which letters have been eliminated from the puzzle? Do not use a sapce or comma to seperate the letters.  ")


for letter in redLetters:
    for myWord in words:
        if letter in myWord:
            #check if my word is already in deletewords before appneding
            deleteWords.append(myWord)
            
clearList()

greenCount = input("How many green letters do you know?")
greenLetters = []

for i in range(int(greenCount)):
    print(i)
    toAdd = [
        input("What letter do you know the position of? "),
        input("What position is it in? ")
    ]
    greenLetters.append(toAdd)
    

    





print(greenLetters)
print(words)
