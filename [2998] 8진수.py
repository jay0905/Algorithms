n = input()
answer = ''

while len(n) % 3 != 0:
    n = '0' + n

for i in range(0, len(n) - 2, 3):
    if n[i:i+3] == '000':
        answer += '0'
    elif n[i:i+3] == '001':
        answer += '1'
    elif n[i:i+3] == '010':
        answer += '2'
    elif n[i:i+3] == '011':
        answer += '3'
    elif n[i:i+3] == '100':
        answer += '4'
    elif n[i:i+3] == '101':
        answer += '5'
    elif n[i:i+3] == '110':
        answer += '6'
    elif n[i:i+3] == '111':
        answer += '7'

print(answer)
