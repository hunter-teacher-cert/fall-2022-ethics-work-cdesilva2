import re

def find_name(line):
  #pattern = r'([A-Z][a-z])'
  pattern = r'([A-Z][a-z]+(?:\.)?(?=\s[A-Z])(?:\s[A-Z][a-z]+)+)'
  result = re.findall(pattern,line)
  return result 
  
file = open("names.txt")
for line in file.readlines():
  result = find_name(line)
  print(result)
  