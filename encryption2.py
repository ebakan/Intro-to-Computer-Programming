#prob-asg3
#ebakan
class encrypt:
    def __init__(self):
        while True:
            print("Welcome to the Encrypter/Decrypter Program!")
            c=raw_input("Enter 'e' to encrypt a string.\nEnter 'd' to decrypt a string.\nEnter 'q' to quit the program.\n").lower()
            if c=='q':
                print("Thanks for playing!")
                break
            elif c!='e' and c!='d':
                print("That is not a valid input.")
                continue
            tc=raw_input("Enter 't' to read from and write to a text file.\nEnter 'c' to input and output from the command line.\n").lower()
            while True:
                if tc!='t' and tc!='c':
                    print("That is not a valid input.")
                else:
                    break
            if tc=='t':
                f=open(raw_input("Input file path:"))
                i=f.read()
                f.close()
                o=open(raw_input("Output file path:"),'w')
                n=raw_input("Key:")
                o.write(self.crypt(i,n,c))
                o.close()
            if tc=='c':
                s=raw_input("Input:").lower()
                n=raw_input("Key:")
                print('Output:'+self.crypt(s,n,c))

    def crypt(self,inp,key,c):
        x=''
        k=''
        y=0
        for i in inp:
            if y==len(key):
                y=0
            k+=key[y]
            y+=1
        for i in range(len(inp)):
            if inp[i].isalpha():
                if i.isupper():
                    y=65
                else:
                    y=97
                if c=='e':
                    x+=chr((ord(inp[i])+ord(k[i])-y)%26+y)
                else:
                    x+=chr((ord(inp[i])+ord(k[i])-y)%26+y)
            else:
                x+=inp[i]
        return x
if __name__=="__main__":
    e=encrypt()
