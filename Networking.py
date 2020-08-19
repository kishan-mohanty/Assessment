value=input().split(" ")
S=int(value[0])
N=int(value[1])
d={}
Output=[]
for i in range(N):
    value=input().split()
    k=int(value[0])
    v=int(value[1])
    if k not in d:
        d[k]=[v]
        Output.append(k)

    elif k in d:
        d[k].append(v)
        if len(d[k])>S:
            Output.append(-1)
        else:
            Output.append(k)
for value in Output:
    print(value)




