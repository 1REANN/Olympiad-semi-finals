n,k=map(int,input().split())
setr=k//n
sutun=k%n
qonsu=[]
if setr>0:
    qonsu.append(k-n)
if setr<n-1:
    qonsu.append(k+n)
if sutun>0:
    qonsu.append(k-1)
if sutun<n-1:
    qonsu.append(k+1)
print(sum(qonsu))
#