import sys
input = sys.stdin.readline

n, m = map(int, input().split())
password_dict = {}

for _ in range(n):
    url, password = input().split()
    password_dict[url] = password

for _ in range(m):
    url_input = input().strip()
    print(password_dict[url_input])

