

def dfs(x):
    if x > 10000:
        return
    check[x] += 1
    num = x

    while x >= 1:
        y = x % 10
        num += y
        x //= 10

    dfs(num)
check = [0 for _ in range(1, 100000)]

for z in range(1, 10000):
    dfs(z)

for z in range(1, 10000):
    if check[z] == 1:
        print(z)