#loops-asgn1
#ebakan
import random
def guess(inp):
    randomNumber=random.randrange(inp)+1
    ans=0
    while ans != randomNumber:
        ans=int(raw_input('Guess:'))
        if ans == 0:
            print('You exited.\n')
            break
        elif ans == randomNumber:
            print('You got the answer right!\n')
            break
        elif ans < randomNumber:
            print('Go higher')
        elif ans > randomNumber:
            print('Go lower')
while __name__=='__main__':
    try:
        print('Enter 0 to exit.')
        guess(int(raw_input('Pick the max:')))
    except ValueError:
        print ("Sorry, that's not an integer.\n")
