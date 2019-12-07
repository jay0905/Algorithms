'''
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를 찾았다. 
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''

n, m = map(int, input().split())

board = []

for i in range(n):
    board.append(input())

wMin = bMin = tempMin = 0
min = 64

for i in range(n-7):
    for j in range(m-7):
        for k in range(i, i+8):
            # W의 경우
            for l in range(j, j+8):
                if (k+l-i-j) % 2 == 0: # 이때는 보드판이 W여야 함
                    if board[k][l] != 'W':
                        wMin += 1
                else:
                    if board[k][l] != 'B':
                        wMin += 1
             # B의 경우
            for l in range(j, j+8):
                if (k+l-i-j) % 2 == 0: # 이때는 보드판이 B여야 함
                    if board[k][l] != 'B':
                        bMin += 1
                else:
                    if board[k][l] != 'W':
                        bMin += 1
        tempMin = wMin if wMin < bMin else bMin
        min = tempMin if tempMin < min else min
        wMin = bMin = tempMin = 0

print(min)
