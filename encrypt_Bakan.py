#prob-asg3
#ebakan
class encrypter:
    #Main Program
    def __init__(self):
        print("Welcome to the Encrypter/Decrypter Program!")
        #runs until user wants to quit (c=='q')
        while True:
            choice=raw_input("Enter 'e' to encrypt a string.\nEnter 'd' to decrypt a string.\nEnter 'q' to quit the program.\n").lower()
            #checks for quit
            if choice=='q':
                print("Thanks for playing!")
                break
            #checks for invalid input -> reloop from top
            elif choice!='e' and choice!='d':
                print("That is not a valid input.")
                continue
            #text/command line input
            #checks for invalid input -> restarts mini-loop until valid input
            while True:
                interface=raw_input("Enter 't' to read from and write to a text file.\nEnter 'c' to input and output from the command line.\n").lower()
                if interface!='t' and interface!='c':
                    print("That is not a valid input.")
                else:
                    break
            #file interface
            if interface=='t':
                f=open(raw_input("Input file path:"))
                s=f.read()
                f.close()
                o=open(raw_input("Output file path:"),'w')
                n=int(raw_input("Step:"))
                o.write(self.crypt(t,n,c))
                o.close()
            #command line interface
            if interface=='c':
                s=raw_input("Input:")
                n=int(raw_input("Step:"))
                print('Output:'+self.crypt(s,n,c))

    #multi-purpose encrypter/decrypter                
    def crypt(self,inp,step,c):
        x=''
        for i in inp:
            #checks for non-alpha chars
            if i.isalpha():
                #checks for upper/lowercase characters
                if i.isupper():
                    y=65
                else:
                    y=97
                #checks for encrypt/decrypt function
                if c=='e':
                    x+=chr((ord(i)+step-y)%26+y)
                else:
                    x+=chr((ord(i)-step-y)%26+y)
            #if char is not alpha
            else:
                x+=i
        return x
    
if __name__=="__main__":
    e=encrypter()
