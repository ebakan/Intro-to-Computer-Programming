def invest(investment,interest,years):
    out=investment*interest**years
    return out
while __name__=='__main__':
    investment=int(raw_input())
    interest=1+(float(raw_input())/100)
    years=int(raw_input())
    print invest(investment,interest,years)
