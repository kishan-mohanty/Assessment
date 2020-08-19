
l=[]
maxx=[]

N=int(input())
k=[]
for i in range(N):
    value=input()
    k.append(value)
for value in k:
    if value == "pop":
        if l[len(l)-1]==maxx[len(maxx)-1]:
            l.pop(len(l)-1)
            maxx.pop(len(maxx)-1)
        else:
            stack.l.pop(len(l)-1)
    elif value=="max":
        print(maxx[len(maxx)-1])
    elif "push" in value:
        value=value.split(" ")
        n=int(value[1])
        if len(l)==0:
            l.append(n)
            maxx.append(n)
        else:
            l.append(n)
            if maxx[len(maxx)-1]<=n:
                maxx.append(n)

