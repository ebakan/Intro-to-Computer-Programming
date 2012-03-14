f=open('wordCount.txt')
t=f.read()
f.close()
out=0
if len(t)!=0:
    for i in range(len(t)):
        if t[i] == " " and t[i-1] != " ":
            out+=1
    out+=1
print out
raw_input()
