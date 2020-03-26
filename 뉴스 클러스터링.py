import math
from collections import Counter

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    
    if len(str1) == 0 and len(str2) == 0:
        return 65536
    
    return math.floor(sum((counter1&counter2).values()) / sum((counter1|counter2).values()) * 65536)

    
       
