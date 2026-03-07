#WordCount.py
#Name: Emma Zechmann
#Date: 3/1/2026
#Assignment: word count 

def main():
  textFile = open("gettysberg.txt", 'r')
  
  wordCount =0 
  linecount = 0
  charactercount = 0

  for line in textFile:
    words= line.split() 
    wordCount += len(words) 

    linecount += 1
    charactercount += len(line)

  print("Total words:", wordCount)
  print("Total lines: ", linecount)
  print ("Characters:", charactercount)
  

if __name__ == '__main__':
  main()
