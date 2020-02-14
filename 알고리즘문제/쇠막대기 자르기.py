
T = int(input())

for test in range(T):
    arr = list(input())
    stack = [0]
    ans = 0
    i = 0
    while i < len(arr):
        if arr[i] == '(':
            if arr[i+1] == ')':
                ans += stack[0]
                i += 1
            else:
                stack[0] += 1

        else:
            ans += 1
            stack[0] -= 1
        i += 1

    print("#%d %d" % (test+1, ans))
