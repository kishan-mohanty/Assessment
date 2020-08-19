s=input()

def checkbracket(s):
    l = []
    stack = []
    for value in s:
        l.append(value)
    print(l)
    for i in range(len(l)):
        if l[i]=="(" or l[i]=="{" or l[i]=="[":
            stack.append(l[i])
        elif l[i]==")"or l[i]=="}"or l[i]=="]":
            if len(stack)==0:
                v=i+1
                return v
            elif stack[len(stack)-1]=="(":
                if l[i]==")":
                    stack.remove("(")
                else:
                    v=i+1
                    return v
            elif stack[len(stack)-1]=="[":
                if l[i]=="]":
                    stack.remove("[")
                else:
                    v=i+1
                    return v
            elif stack[len(stack)-1]=="{":
                if l[i]=="}":
                    stack.remove("{")
                else:
                    v =i+1
                    return v

    if len(stack)==0:
        return "Sucess"

k=checkbracket(s)
print(k)




