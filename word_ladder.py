import re # Re is a module for string searching
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t]) # checks tuples and uses the zip function to return the list of tuples

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and #Goes through and searches if pattern matches word
                    word not in list]

def find(word, words, seen, target, path): # Function for checking if letters in the appended list match
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list) # Checks how many letters in the word are being checked
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list]) # Goes through the list of tuples in ascending order
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

def file(file): # function for opening the file. Turned into a function for unit testing purposes
  file = open(file, 'r')
  lines = file.readlines()
  return lines

lines = file("dictionary.txt") # Using the file function to read the file.

while True:
  start = input("Enter start word:") # User's starting word
  target = input("Enter target word:") # User's finishing word
  words = []
  for line in lines:
    word = line.rstrip() # strips the words in teh dictionary of whitespace etc
    if len(word) == len(start):
      words.append(word) # Appends the stripped word into the words array if starting word has the same length as it.

  break

count = 0
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):  # Shows the total number of words used and the words used to change your start word to the target word.
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")

