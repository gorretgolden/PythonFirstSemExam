#   Question 3 string manipulation
str = "geeks quiz practice code "

# Function to reverse words of string 
def reversed_string(str): 
  
# splitted words
    splitted_characters = str.split(' ') 
  
# reversing the string and joing it
    
    new_string = ' '.join(reversed(splitted_characters)) 
    return new_string 
  
if __name__ == "__main__": #Using built-in method main
    print ("Output:",reversed_string(str))