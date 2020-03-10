T = 10
for test in range(T):
    N = int(input())
    arr = list(input())
    p = 0
    tmp1 = []
    tmp2 = []


    for i in range(len(arr)):
        if '0' <= arr[i] <= '9':
            tmp1.append(arr[i])

        else:
            if arr[i] == '(':
                p = 1
                tmp2.append(arr[i])

            if arr[i] == '+' or arr[i] == '-':

                if tmp2[-1] == '*' or tmp2[-1] == '/':
                    while 1:
                        if tmp2[-1] != '*' or tmp2[-1] == '/':
                            break
                        z = tmp2.pop()
                        if z == '*' or z == '/':
                            y = int(tmp1.pop())
                            x = int(tmp1.pop())

                            if z == '*':
                                xy = x * y
                            if z == '/':
                                xy = x // y

                            tmp1.append(xy)
                if len(tmp2) == 0 or tmp2[-1] == '(' or tmp2[-1] == '+' or tmp2[-1] == '-':

                    tmp2.append(arr[i])
            if arr[i] == '*' or arr[i] == '/':
                if len(tmp2) == 0 or tmp2[-1] == '(' or tmp2[-1] == '+' or tmp2[-1] == '-' or tmp2[-1] == '*' or tmp2[-1] == '/':
                    tmp2.append(arr[i])

            if arr[i] == ')':
                while 1:
                    z = tmp2.pop()
                    if z == '(':
                        break
                    if z != '(':
                        y = int(tmp1.pop())
                        x = int(tmp1.pop())
                        if z == '+':
                            xy = x+y

                        elif z == '-':
                            xy = x-y
                        elif z == '*':
                            xy = x*y
                        elif z == '/':
                            xy = x//y

                        tmp1.append(xy)


    print("#%d" % (test+1), end=" ")
    print(tmp1[0])