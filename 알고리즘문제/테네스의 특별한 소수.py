n=1000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False


T = int(input())

for test in range(T):
    D, A, B = map(int, input().split())
    cnt = 0
    strprime = ""

    for i in range(len(primes)):
        if primes[i] < A:
            continue
        if primes[i] > B:
            break

        strprime = str(primes[i])
        if strprime.count(str(D)):
            cnt += 1


    print("#%d %d" % (test+1, cnt))



