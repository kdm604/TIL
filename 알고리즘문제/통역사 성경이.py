T = int(input())

for test in range(T):
    N = int(input())
    cnt = 0
    arr = list(input().split())
    ans = [0 for _ in range(N)]
    index = 0


    for i in range(len(arr)):

        b = 0
        c = 0
        s = arr[i]
        p = 0

        for j in range(0, len(s)):
            if s[-1] == '.' or s[-1] == '?' or s[-1] == '!':
                p = 1
            if 'A' <= s[0] <= 'Z':
                c = 1
                if j >0 :
                    if 'A' <= s[j] <= 'Z':
                        b = 1
                        break
                    elif '0' <= s[j] <= '9':
                        b = 1
                        break

        if b == 0 and c == 1:
            cnt += 1

        if p == 1:
            ans[index] = cnt
            index += 1
            cnt = 0

    print("#%d" % (test+1), end=" ")
    for i in range(N):
        print(ans[i], end=" ")
    print()
