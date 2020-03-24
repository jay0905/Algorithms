from collections import deque

def solution(phone_book):
    phone_book = deque(phone_book)
    
    for _ in range(len(phone_book)):
        current_number = phone_book.popleft()
        
        for number in phone_book:
            for x, y in zip(current_number, number):
                if x != y:
                    break
            else:
                return False
                
        phone_book.append(current_number)
    
    return True
