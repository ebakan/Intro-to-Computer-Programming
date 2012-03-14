def factor(num):
    out=''
    for i in range(1,num+1):
        if num % i == 0:
            out += str(i)+" "
    return out
while __name__=='__main__':
    try:
        print factor(int(raw_input()))
    except ValueError:
        print "Sorry, that is not an integer"    
    except OverflowError:
        print "Sorry, that number is too big"
