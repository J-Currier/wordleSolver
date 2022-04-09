import wordList


words = []
deleteWords = []

useExtraWords = input("Would you like to limit the search to the official Wordle wordlist? (y/n)")

if useExtraWords == 'y':
    words = wordList.tempList
else:
    words = wordList.official + wordList.extra

redLetters = input("Which letters have been eliminated from the puzzle? Do not use a sapce or comma to seperate the letters.  ")


for letter in redLetters:
    for myWord in words:
        if letter in myWord:
            deleteWords.append(myWord)
    print(letter, words)

for delWord in deleteWords:
    try:
        words.remove(delWord)
    except: 
        pass
        
        

print(words)

    
