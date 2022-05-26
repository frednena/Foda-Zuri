# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True
from collections import Counter


def find_anagrams(str1, str2):
    return Counter (str1) == Counter (str2)

        
 #main code
if __name__ == "__main__" :
    str1 = 'race'
    str2 = 'care'
    print (find_anagrams (str1, str2)) 
