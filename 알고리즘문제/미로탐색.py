import sys


dy=[-1,1,0,0]
dx=[0,0,-1,1]

def bfs(y,x):
    visit[y][x]=1
    q=[]
    q.append((y,x))
    while q:
        yx=q.pop(0)
        if yx[0]==N-1 and yx[1]==M-1:
            break
        for i in range(4):
            ny=yx[0]+dy[i]
            nx=yx[1]+dx[i]
            if -1<ny<N and -1<nx<M:
                if sheet[ny][nx] == 1 and visit[ny][nx] == 0:
                    q.append((ny,nx))
                    visit[ny][nx]=visit[yx[0]][yx[1]]+1

N,M=map(int,input().split())
sheet=[[int(x) for x in input()]for y in range(N)]
visit=[[0 for x in range(M)]for y in range(N)]
bfs(0,0)
print(visit[N-1][M-1])