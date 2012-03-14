#funasg1
#ebakan
class funGreet():
    def __init__(self):
        self.displayHeader()
        self.displayGreeting(raw_input("What is your name?"), raw_input("What school are you from?"))
    def displayHeader(self):
        print("Welcome to the Function Greeter Program!\nCoded by Eric Bakan")
    def displayGreeting(self,name,school):
        print("Welcome, "+name+" from "+school+".")
        if school.lower()=='bellarmine' or school.lower()=='bell' or school.lower()=='bcp':
            print("Congratulations, you go to the greatest school in the world")

if __name__=='__main__':
    greeter=funGreet()
