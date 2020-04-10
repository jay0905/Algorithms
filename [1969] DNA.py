import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
dnas = [input().strip() for _ in range(n)]
s = ""
hd = 0

for i in range(m):
    dna_list = ["A", "C", "G", "T"]
    dna_cnt = [0, 0, 0, 0]
    for dna in dnas:
        if dna[i] == "A":
            dna_cnt[0] += 1
        elif dna[i] == "C":
            dna_cnt[1] += 1
        elif dna[i] == "G":
            dna_cnt[2] += 1
        elif dna[i] == "T":
            dna_cnt[3] += 1

    max_dna = max(dna_cnt)
    max_idx = dna_cnt.index(max_dna)

    s += dna_list[max_idx]
    hd += n - max_dna

print(s)
print(hd)
