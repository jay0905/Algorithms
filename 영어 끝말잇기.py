def lose(i, word, words, words_set):
    return words[i-1][-1] != words[i][0] or word in words_set

def solution(n, words):
    words_set = set([words[0]])
    
    for i, word in enumerate(words):
        if i == 0:
            continue
            
        if lose(i, word, words, words_set):
            return [i % n + 1, i // n + 1]
        
        words_set.add(word)
    
    return [0, 0]
