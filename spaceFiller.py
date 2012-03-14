#prob-asg1
#ebakan
import os
class filer:
    def looper(self,inp):
        for i in range(1,inp+1):
            f=open('spaceFiller/'+str(i)+'.txt','w')
            f.write('Eric Bakan')
            f.close
            print(i)
        print('DONE!')

    def deleter(self,inp):
        for i in range(1,inp+1):
            os.remove('spaceFiller/'+str(i)+'.txt')
            print(i)
        print('DONE!')
    
    def __init__(self):
        inp=int(raw_input())
        self.looper(inp)
        raw_input()
        self.deleter(inp)
        raw_input()

if __name__=='__main__':
    f=filer()
