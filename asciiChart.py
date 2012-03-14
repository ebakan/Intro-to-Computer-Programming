#prob-asg2
#ebakan
class asciiChart:
    def __init__(self):
        print("  WELCOME TO ERIC BAKAN'S ASCII CHART GENERATOR")
        self.ascii()
        raw_input()
    def ascii(self):
        cols=8
        print('  '+'*'*(cols*15-14)+'  ')
        for i in range(32):
            x='  |  '
            for k in range(1,cols):
                x+=chr(i+32*k)+' '
                if (i+32*k)<100:
                    x+=' '
                if (i+32*k)==127:
                    x+=' '
                x+=str(i+32*k)+' '+hex(i+32*k)+'  |  '
            print(x)
        print('  '+'*'*(cols*15-14)+'  ')

if __name__=='__main__':
    ascii=asciiChart()
    
