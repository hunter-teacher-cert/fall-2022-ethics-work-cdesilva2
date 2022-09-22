# binsearch.py
# Christopher De Silva 
# CSCI 77800 Fall 2022
# collaborators: N/A
# consulted: N/A

#The focus of this program is to create an array of numbers. Using recurssion,perform a binary search locating the given number and outputting their location in the array. 

def binsearch(data, value):
  target_index = binsearch_recursive(data, value, 0, len(data) - 1)
  print("%s is at index: %s" % (value, target_index))

#Takes the array data, value looking for and the low index and high index of that value. This is done recursively. 
def binsearch_recursive(data, value, low_index, high_index):
  
  if high_index >= low_index:
    middle_index = int((low_index + high_index) / 2)
    if value == data[middle_index]:
      return middle_index
    elif value > data[middle_index]:
      return binsearch_recursive(data, value, middle_index + 1, high_index)
    elif value < data[middle_index]:
      return binsearch_recursive(data, value, low_index, middle_index - 1)
  return -1

data = [1, 3, 5, 6, 10] #creates the pre-populated array
print("Array Inputs: %s" % data) # print the populated array 
binsearch(data, 6) # search for 6, Output 3 
binsearch(data, 10) #search for 10, Output 4
binsearch(data, 1) #search for 1, Output 0
binsearch(data, 10000) # number not in the data set should output -1