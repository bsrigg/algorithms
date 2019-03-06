def bracesvalid(mylist):
    stack=[]
    for i in mylist:
        if i in ("{","[","("):
            stack.append(i)
        elif i == "]":
            if len(stack)>0 and stack[-1] == "[":
                stack.pop()
            else:
                return False
        elif i == "}":
            if len(stack)>0 and stack[-1] == "{":
                stack.pop()
            else:
                return False
        elif i == ")":
            if len(stack)>0 and stack[-1] == "(":
                stack.pop()
            else:
                return False
    return len(stack) == 0
print(bracesvalid("[{({})}]}"))
    
