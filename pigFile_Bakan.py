#lists-asg5
#ebakan
class pigConverter:
    def __init__(self):
        out=''
        print("Welcome to the Pig Latin File Translator!")
        array=self.txtIn(raw_input('Name of the file you would like to translate:'))
        lst=[]
        for i in array:
            lst+=i.split()
        #lst=self.charfinder(lst)
        print lst
        for i in lst:
            out+=(self.convertToPig(i))+' '
        print out
        #self.txtOut(raw_input('Name of the file you would like to write to:'),out)
        
    def convertToPig(self,inp):
        for i in range(len(inp)):
            if (inp[i].lower()=='a' or
                inp[i].lower()=='e' or
                inp[i].lower()=='i' or
                inp[i].lower()=='o' or
                inp[i].lower()=='u' or
                inp[i].lower()=='y'):
                inp+=inp[0:i]+'ay'
                return inp[i:]
                break

    def txtIn(self,inp):
        f=open(inp)
        t=f.readlines()
        f.close()
        print t
        return t

    def txtOut(self,inp,out):
        f=open(inp, 'w')
        f.write(out)
        f.close()

    def nfinder(self,inp):
        for k in inp:
            for i in range(len(k)):
                if (inp[i-1]+inp[i])=='\\n':
                    print inp
                    
    def charfinder(self,inp):
        for i in range(len(inp)):
            if not inp[i].isalpha():
                del inp[i]

if __name__=='__main__':
    converter=pigConverter()
