#fun-asg10
#ebakan
def convertToPig(word):
    for i in range(len(word)):
        if (word[i].lower()=='a' or
            word[i].lower()=='e' or
            word[i].lower()=='i' or
            word[i].lower()=='o' or
            word[i].lower()=='u' or
            word[i].lower()=='y'):
            word+=word[0:i]+'ay'
            return word[i:]
            break
while __name__=='__main__':
    print(convertToPig(raw_input("Enter a word to translate:")))
