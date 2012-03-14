def convertDecimal(dat):
     lst=list(dat)
     num=list(dat)
     out=0
     tf=True
     for i in range(len(lst)):
          if lst[len(lst)-i-1] == "1" or lst[len(lst)-i-1] == "0":
               num[i]=lst[len(lst)-i-1]
          else:
               tf=False
     if tf==True:
          for i in range(len(num)-1,-1,-1):
               if num[i] == "1":
                   out+=2**i
          return out
     else:
          return "The given input was not a valid binary value. Please try again."
while __name__ == '__main__':
     print convertDecimal(raw_input())
