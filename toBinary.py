def convertBinary(num):
    out=""
    pwr=0
    tf=True
    for i in range(0,num):
        if 2**i>num:
            pwr=i-1
            break
    for i in range(pwr,-1,-1):
        if num-2**i>=0:
          out+="1"
          num-=2**i
        else:
            out+="0"
    return out
def tryfunc():
    try:
        print convertBinary(int(raw_input()))
    except ValueError:
        print "Sorry, that's not an integer"
    except OverflowError:
        print "Sorry, that number is too big"
while __name__ == '__main__':
    tryfunc()
