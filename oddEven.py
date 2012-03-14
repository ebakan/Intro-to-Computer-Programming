def oddEven(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
while __name__=='__main__':
    try:
        print oddEven(int(raw_input()))
    except ValueError:
        print "Sorry, that's not an integer"
    except OverflowError:
        print "Sorry, that number is too big"
