#loopassn3
#ebakan
class grader:
    def name(self):
        self.name=raw_input('What is your name?')
        print('Welcome to the grader program, '+self.name+'!')

    def gradeinp(self):
        self.gradenum=int(raw_input('How many total grades?'))
        self.points=int(raw_input('How many points are each assignment out of?'))
        self.total=0
        for i in range(self.gradenum):
            self.total+=int(raw_input('Enter grade:'))

    def grade(self):
        self.avg=((self.total+0.0)/(self.points*self.gradenum))*100
        print(self.name+'\'s grade:\t\t'+str(self.avg)+'%')
        greet=self.name+', you\'re doing '
        if self.avg>=90:
            greet+='great!'
        elif self.avg>=80:
            greet+='good.'
        elif self.avg>=70:
            greet+='average.'
        elif self.avg>=60:
            greet+='badly.'
        else:
            greet+='horribly.'
        print greet

    def __init__(self):
        self.name()
        self.gradeinp()
        self.grade()

if __name__=='__main__':
    try:
        grade=grader()
    except ValueError:
        print('Sorry, you entered an invalid number. Please try again.')
    except ZeroDivisionError:
        print('Wow, you entered zero! You have no need for this program. Goodybe.')
    raw_input()
