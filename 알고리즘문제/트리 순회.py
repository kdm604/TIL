def preorder_traverseF(T):
    print(chr(65 + T), end="")
    if nxn[T][1]:
        preorder_traverseF(nxn[T][1]-1)
    if nxn[T][2]:
        preorder_traverseF(nxn[T][2]-1)


def preorder_traverseM(T):
    if nxn[T][1]:
        preorder_traverseM(nxn[T][1]-1)
    print(chr(65+T), end="")
    if nxn[T][2]:
        preorder_traverseM(nxn[T][2]-1)

def preorder_traverseL(T):
    if nxn[T][1]:
        preorder_traverseL(nxn[T][1]-1)
    if nxn[T][2]:
        preorder_traverseL(nxn[T][2]-1)
    print(chr(65+T), end="")


N = int(input())


nxn = [[0 for _ in range(4)]for _ in range(N)]

for z in range(N):
    nxn[z] = list(input().split())

for i in range(N):
    for j in range(3):
        if 'A' <=nxn[i][j] <= 'Z':
            nxn[i][j] = ord(nxn[i][j]) - 64
        else:
            nxn[i][j] = 0
nxn.sort(key=lambda x: x[0])
preorder_traverseF(0)
print()
preorder_traverseM(0)
print()
preorder_traverseL(0)
