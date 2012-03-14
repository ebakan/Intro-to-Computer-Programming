import os
def deleter(inp):
    for i in range(1,inp+1):
        os.remove('spaceFiller/'+str(i)+'.txt')
        print(i)
    print('DONE!')

if __name__=='__main__':
    deleter(int(raw_input()))
