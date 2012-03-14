def commenter(path,start,stop):
    f=open(path)
    lines=[]
    x=f.readline()
    while x:
        lines.append(x)
        x=f.readline()
    f.close()
    for i in range(start-1,stop):
        lines[i]='#'+lines[i]
    f=open(path, 'w')
    f.writelines(lines)
    f.close()
if __name__=='__main__':
    commenter('asdf.txt',2,4)
