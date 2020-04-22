from itertools import combinations

word = input()
index = [n for n in range(len(word) - 1)]
candidates = []

index_combi = combinations(index, 2)

for combi in index_combi:
    w1 = word[0:combi[0] + 1][::-1]
    w2 = word[combi[0] + 1:combi[1] + 1][::-1]
    w3 = word[combi[1] + 1:len(word)][::-1]

    candidates.append(w1 + w2 + w3)

candidates.sort()
print(candidates[0])
