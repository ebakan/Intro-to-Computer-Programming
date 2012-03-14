#fun-asgn2
#ebakan & vsingh
def capitalize(inp):
    out=inp[0].upper()
    for i in range(1,len(inp)):
        if inp[i-1]==' ':
            out+=inp[i].upper()
        else:
            out+=inp[i]
    return out
if __name__=='__main__':
    print capitalize(raw_input('Input a string:'))
