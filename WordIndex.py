#WordIndex.pydef main():
#Name: Emma Zechmann
#Date: 3/1/2026
#Assignment: word index
  
def main():
  textFile = open("fish.txt", 'r')
  
  words = {} 
  lineNumber = 1 

  for line in textFile:
    line = line.strip()
    lineWords = line.split()

    for word in lineWords:
      word= word.lower()
      word= word.strip(".,?!")

      if word not in words:
        words[word]= [lineNumber]

      else:
        if lineNumber not in words[word]:
          words[word].append(lineNumber)

    lineNumber +=1 

  for word in words:
    print(word, words[word])

  textFile.close()




if __name__ == '__main__':
  main()
