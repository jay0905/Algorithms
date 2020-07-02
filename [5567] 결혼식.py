import sys
input = sys.stdin.readline

def count_invite_members(relationships):
    invite_members = set()

    for friend in relationships[1]:
        invite_members.add(friend)

        for friend_friend in relationships[friend]:
            invite_members.add(friend_friend)

    return len(invite_members) - 1

n = int(input())
m = int(input())

relationships = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    relationships[a].append(b)
    relationships[b].append(a)

print(count_invite_members(relationships))
