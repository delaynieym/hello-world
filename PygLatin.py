#there are still stink bugs

punctList=[",", ".", "!", "?",":", ";"]
vowelList=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def isVowel(lett):
    global vowelList
    if lett in vowelList: return True
    else: return False
    
def isCap(lett):
    if lett[0].upper() == lett[0]: return True
    else: return False
    
def isPunct(lett):
    global punctList
    if lett in punctList: return True
    else: return False
    
def cutoff(word):
    for l in range(len(word)):
        if isVowel(word[l]): return l



def pygLatin(word):
  
  if cutoff(word) != 0: movingLettrs = word[:cutoff(word)]
  else: movingLettrs = ""

  if isPunct(word[-1]):
      punc = word[-1]; word = word[:-1]
  else: punc = ""
  
  if isCap(word[0]): return (word[cutoff(word):] + movingLettrs)[0].upper() + (word[cutoff(word):] + movingLettrs)[1:].lower() + "ay" + punc
  else: return word[cutoff(word):] + movingLettrs + "ay" + punc



while True:
    inputPhrase=input("Enter the phrase you want to be translated into Pyg Latin:\n")
    wordsList=inputPhrase.split(" ")
    
    for word in wordsList:
      print(pygLatin(word), end=" ")
    print("\n")