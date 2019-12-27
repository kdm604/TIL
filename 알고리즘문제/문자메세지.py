import sys

P, W = map(int, input().split())

key = [
    [],
    [' '],
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L'],
    ['M', 'N', 'O'],
    ['P', 'Q', 'R', 'S'],
    ['T', 'U', 'V'],
    ['W', 'X', 'Y', 'Z']
]
lastkey = [0]
ans = 0

arr = list(input())

for i in range(len(arr)):
    for j in range(1, 10):
        if arr[i] in key[j]:
            if lastkey[-1] == j and j != 1:
                ans += W
            lastkey.append(j)
            for k in range(len(key[j])):
                if arr[i] == key[j][k]:
                    ans += (k+1)*P


print(ans)
