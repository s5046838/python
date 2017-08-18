import re # Re is a module for string searching

def file(file): # function for opening the file. Turned into a function for unit testing purposes
  file = open(file, 'r')
  lines = file.readlines()
  return lines

lines = file("dictionary.txt") # Using the file function to read the file.

def same(item, target):# checks tuples and uses the zip function to return the list of tuples
  return len([x for (x, y) in zip(item, target) if x == y]) # Returns items that are identical in the same position in the list

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and #Goes through and searches if pattern matches word
                    word not in list]

def find(word, words, seen, target, path): # Function for checking if letters in the appended list match
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list) # Checks how many letters in the word are being checked using the build function
    if len(list) == 2: #Checks if the length of the list is equal to 2
        return False
  list = sorted([(same(item, target), item) for item in list]) # Goes through the list of tuples in ascending order
  list.reverse() #Goes through and checks the list in reverse
  for (match, item) in list:
    if match >= len(target) - 1: # checks if match is either greater or equal than the len target minus one character
      if match == len(target) - 1: # Checks if match length is the same and appents item into path and returns true.
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in list:
    path.append(item) # Appends item into path
    if find(item, words, seen, target, path): # if any string values are found to match return true
      return True
    path.pop() # If no string values match, remove it from path

while True: # This is used or checking if the users input is correct
  start = input("Enter start word:")
  target = input("Enter target word:")
  words = []
  if start.isnumeric() or target.isnumeric(): # Checks if user's input is numerical
    print("You cannot compare with integers")
    continue
  if start == '' or target == '': #Checks if user's input is empty
    print("Please make sure all inputs are filled")
    continue
  if len(start) == len(target): #Checks if user's input is the same length
    for line in lines:
      word = line.rstrip()
      if len(word) == len(start):
        words.append(word)
    break
  else:
    print("Error: Word sizes dont match")


count = 0
path = [start] #The starting word used to create the list of words
seen = {start : True} #The dictionary key, value stored if it is True
if find(start, words, seen, target, path):  # Shows the total number of words used and the words used to change your start word to the target word.
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")

