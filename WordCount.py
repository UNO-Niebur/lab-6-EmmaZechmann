#WordCount.py
#Name: Emma Zechmann
#Date: 3/1/2026
#Assignment: word count 

def main():
  textFile = open("gettysberg.txt", 'r')
  
  wordCount =0 
  for line in textFile:
    words= line.split() 
    wordCount += len(words) 

  print("Total words:", wordCount)
  

if __name__ == '__main__':
  main()
