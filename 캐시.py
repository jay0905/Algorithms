출처: https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return len(cities) * 5

    cache = deque()
    time = 0
    cities = [city.lower() for city in cities]

    for city in cities:
        
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            
            cache.append(city)
            time += 5
                
    return time
            
