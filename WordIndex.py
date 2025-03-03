#WordIndex.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  linenum = 0
  
  words = {} #create an empty dictionary
  for line in textFile:
    linenum += 1 
    wordList = line.split()
    for w in wordList:
      w = w.lower()
      w = w.replace(",", "")
      w = w.replace(".", "")
      w = w.replace("/n","")
      w = w.replace("!", "")

      if w in words:
        if linenum not in words[w]:
          words[w].append(linenum)
      else:
        words[w] = [linenum]
  for word in words:
    print(word, words[word])

  
  # words["fish"] = [2]     #add a list to the dictionary
  #print ("fish" in words) #is the word there now?
  #words["fish"].append(5) #add to an existing list
  #print(words)


if __name__ == '__main__':
  main()