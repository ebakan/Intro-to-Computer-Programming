from random import randrangeclass tictactoe():    def __init__(self):        while True:            self.gameLoop()            if not self.playAgain():                break                def printGrid(self):        print('  1  2  3')        for i in range(3):            print (str(i+1)+' '+self.grid[i][0]+'  '+self.grid[i][1]+'  '+self.grid[i][2])    def error(self):        print('Sorry, you entered something wrong. Please try again.')    def newGrid(self):        self.grid=[['-','-','-'],                   ['-','-','-'],                   ['-','-','-']]    def playercomp(self):        while True:            inp=raw_input('Would you like to play with 1 player or 2 players? (1/2)')            if inp=='1':                return True                break            elif inp=='2':                break            else:                self.error()            def compAssess(self,user):        winMoves=[]        blockMoves=[]        if user == 'X':            other = 'O'        elif user == 'O':            other = 'X'        if self.grid[0][0]==self.grid[1][0]==user and self.grid[2][0]=='-':            winMoves.append(7)        if self.grid[0][0]==self.grid[0][1]==user and self.grid[0][2]=='-':            winMoves.append(3)        if self.grid[0][0]==self.grid[2][0]==user and self.grid[1][0]=='-':            winMoves.append(4)        if self.grid[0][0]==self.grid[0][2]==user and self.grid[0][1]=='-':            winMoves.append(2)        if self.grid[0][0]==self.grid[1][1]==user and self.grid[2][2]=='-':            winMoves.append(9)        if self.grid[0][0]==self.grid[2][2]==user and self.grid[1][1]=='-':            winMoves.append(5)                if self.grid[0][1]==self.grid[0][0]==user and self.grid[0][2]=='-':            winMoves.append(3)        if self.grid[0][1]==self.grid[0][2]==user and self.grid[0][0]=='-':            winMoves.append(1)        if self.grid[0][1]==self.grid[1][1]==user and self.grid[2][1]=='-':            winMoves.append(8)        if self.grid[0][1]==self.grid[2][1]==user and self.grid[1][1]=='-':            winMoves.append(5)                if self.grid[0][2]==self.grid[0][1]==user and self.grid[0][0]=='-':            winMoves.append(1)        if self.grid[0][2]==self.grid[1][1]==user and self.grid[2][0]=='-':            winMoves.append(7)        if self.grid[0][2]==self.grid[1][2]==user and self.grid[2][2]=='-':            winMoves.append(9)        if self.grid[0][2]==self.grid[0][0]==user and self.grid[0][1]=='-':            winMoves.append(2)        if self.grid[0][2]==self.grid[2][2]==user and self.grid[1][2]=='-':            winMoves.append(6)        if self.grid[0][2]==self.grid[2][0]==user and self.grid[1][1]=='-':            winMoves.append(5)               if self.grid[1][0]==self.grid[0][0]==user and self.grid[2][0]=='-':            winMoves.append(7)        if self.grid[1][0]==self.grid[2][0]==user and self.grid[0][0]=='-':            winMoves.append(1)        if self.grid[1][0]==self.grid[1][1]==user and self.grid[1][2]=='-':            winMoves.append(6)        if self.grid[1][0]==self.grid[1][2]==user and self.grid[1][1]=='-':            winMoves.append(5)                if self.grid[1][1]==self.grid[0][0]==user and self.grid[2][2]=='-':            winMoves.append(9)        if self.grid[1][1]==self.grid[0][1]==user and self.grid[2][1]=='-':            winMoves.append(8)        if self.grid[1][1]==self.grid[0][2]==user and self.grid[2][0]=='-':            winMoves.append(7)        if self.grid[1][1]==self.grid[1][0]==user and self.grid[1][2]=='-':            winMoves.append(6)        if self.grid[1][1]==self.grid[1][2]==user and self.grid[1][0]=='-':            winMoves.append(4)        if self.grid[1][1]==self.grid[2][0]==user and self.grid[0][2]=='-':            winMoves.append(3)        if self.grid[1][1]==self.grid[2][1]==user and self.grid[0][1]=='-':            winMoves.append(2)        if self.grid[1][1]==self.grid[2][2]==user and self.grid[0][0]=='-':            winMoves.append(1)                if self.grid[1][2]==self.grid[0][2]==user and self.grid[2][2]=='-':            winMoves.append(9)        if self.grid[1][2]==self.grid[2][2]==user and self.grid[0][2]=='-':            winMoves.append(3)        if self.grid[1][2]==self.grid[1][0]==user and self.grid[1][1]=='-':            winMoves.append(5)        if self.grid[1][2]==self.grid[1][1]==user and self.grid[1][0]=='-':            winMoves.append(4)        if self.grid[2][0]==self.grid[1][0]==user and self.grid[0][0]=='-':            winMoves.append(1)        if self.grid[2][0]==self.grid[0][0]==user and self.grid[1][0]=='-':            winMoves.append(4)        if self.grid[2][0]==self.grid[2][1]==user and self.grid[2][2]=='-':            winMoves.append(9)        if self.grid[2][0]==self.grid[2][2]==user and self.grid[2][1]=='-':            winMoves.append(8)        if self.grid[2][0]==self.grid[1][1]==user and self.grid[0][2]=='-':            winMoves.append(3)        if self.grid[2][0]==self.grid[0][2]==user and self.grid[1][1]=='-':            winMoves.append(5)        if self.grid[2][1]==self.grid[2][0]==user and self.grid[2][2]=='-':            winMoves.append(9)        if self.grid[2][1]==self.grid[2][2]==user and self.grid[2][0]=='-':            winMoves.append(7)        if self.grid[2][1]==self.grid[1][1]==user and self.grid[0][1]=='-':            winMoves.append(2)        if self.grid[2][1]==self.grid[0][1]==user and self.grid[1][1]=='-':            winMoves.append(5)        if self.grid[2][2]==self.grid[2][1]==user and self.grid[2][0]=='-':            winMoves.append(7)        if self.grid[2][2]==self.grid[1][2]==user and self.grid[0][2]=='-':            winMoves.append(3)        if self.grid[2][2]==self.grid[2][0]==user and self.grid[2][1]=='-':            winMoves.append(8)        if self.grid[2][2]==self.grid[0][2]==user and self.grid[1][2]=='-':            winMoves.append(6)        if self.grid[2][2]==self.grid[1][1]==user and self.grid[0][0]=='-':            winMoves.append(1)        if self.grid[2][2]==self.grid[0][0]==user and self.grid[1][1]=='-':            winMoves.append(5)        if self.grid[0][0]==self.grid[1][0]==other and self.grid[2][0]=='-':            blockMoves.append(7)        if self.grid[0][0]==self.grid[0][1]==other and self.grid[0][2]=='-':            blockMoves.append(3)        if self.grid[0][0]==self.grid[2][0]==other and self.grid[1][0]=='-':            blockMoves.append(4)        if self.grid[0][0]==self.grid[0][2]==other and self.grid[0][1]=='-':            blockMoves.append(2)        if self.grid[0][0]==self.grid[1][1]==other and self.grid[2][2]=='-':            blockMoves.append(9)        if self.grid[0][0]==self.grid[2][2]==other and self.grid[1][1]=='-':            blockMoves.append(5)                if self.grid[0][1]==self.grid[0][0]==other and self.grid[0][2]=='-':            blockMoves.append(3)        if self.grid[0][1]==self.grid[0][2]==other and self.grid[0][0]=='-':            blockMoves.append(1)        if self.grid[0][1]==self.grid[1][1]==other and self.grid[2][1]=='-':            blockMoves.append(8)        if self.grid[0][1]==self.grid[2][1]==other and self.grid[1][1]=='-':            blockMoves.append(5)                if self.grid[0][2]==self.grid[0][1]==other and self.grid[0][0]=='-':            blockMoves.append(1)        if self.grid[0][2]==self.grid[1][1]==other and self.grid[2][0]=='-':            blockMoves.append(7)        if self.grid[0][2]==self.grid[1][2]==other and self.grid[2][2]=='-':            blockMoves.append(9)        if self.grid[0][2]==self.grid[0][0]==other and self.grid[0][1]=='-':            blockMoves.append(2)        if self.grid[0][2]==self.grid[2][2]==other and self.grid[1][2]=='-':            blockMoves.append(6)        if self.grid[0][2]==self.grid[2][0]==other and self.grid[1][1]=='-':            blockMoves.append(5)            if self.grid[1][0]==self.grid[0][0]==other and self.grid[2][0]=='-':            blockMoves.append(7)        if self.grid[1][0]==self.grid[2][0]==other and self.grid[0][0]=='-':            blockMoves.append(1)        if self.grid[1][0]==self.grid[1][1]==other and self.grid[1][2]=='-':            blockMoves.append(6)        if self.grid[1][0]==self.grid[1][2]==other and self.grid[1][1]=='-':            blockMoves.append(5)                if self.grid[1][1]==self.grid[0][0]==other and self.grid[2][2]=='-':            blockMoves.append(9)        if self.grid[1][1]==self.grid[0][1]==other and self.grid[2][1]=='-':            blockMoves.append(8)        if self.grid[1][1]==self.grid[0][2]==other and self.grid[2][0]=='-':            blockMoves.append(7)        if self.grid[1][1]==self.grid[1][0]==other and self.grid[1][2]=='-':            blockMoves.append(6)        if self.grid[1][1]==self.grid[1][2]==other and self.grid[1][0]=='-':            blockMoves.append(4)        if self.grid[1][1]==self.grid[2][0]==other and self.grid[0][2]=='-':            blockMoves.append(3)        if self.grid[1][1]==self.grid[2][1]==other and self.grid[0][1]=='-':            blockMoves.append(2)        if self.grid[1][1]==self.grid[2][2]==other and self.grid[0][0]=='-':            blockMoves.append(1)                if self.grid[1][2]==self.grid[0][2]==other and self.grid[2][2]=='-':            blockMoves.append(9)        if self.grid[1][2]==self.grid[2][2]==other and self.grid[0][2]=='-':            blockMoves.append(3)        if self.grid[1][2]==self.grid[1][0]==other and self.grid[1][1]=='-':            blockMoves.append(5)        if self.grid[1][2]==self.grid[1][1]==other and self.grid[1][0]=='-':            blockMoves.append(4)        if self.grid[2][0]==self.grid[1][0]==other and self.grid[0][0]=='-':            blockMoves.append(1)        if self.grid[2][0]==self.grid[0][0]==other and self.grid[1][0]=='-':            blockMoves.append(4)        if self.grid[2][0]==self.grid[2][1]==other and self.grid[2][2]=='-':            blockMoves.append(9)        if self.grid[2][0]==self.grid[2][2]==other and self.grid[2][1]=='-':            blockMoves.append(8)        if self.grid[2][0]==self.grid[1][1]==other and self.grid[0][2]=='-':            blockMoves.append(3)        if self.grid[2][0]==self.grid[0][2]==other and self.grid[1][1]=='-':            blockMoves.append(5)        if self.grid[2][1]==self.grid[2][0]==other and self.grid[2][2]=='-':            blockMoves.append(9)        if self.grid[2][1]==self.grid[2][2]==other and self.grid[2][0]=='-':            blockMoves.append(7)        if self.grid[2][1]==self.grid[1][1]==other and self.grid[0][1]=='-':            blockMoves.append(2)        if self.grid[2][1]==self.grid[0][1]==other and self.grid[1][1]=='-':            blockMoves.append(5)        if self.grid[2][2]==self.grid[2][1]==other and self.grid[2][0]=='-':            blockMoves.append(7)        if self.grid[2][2]==self.grid[1][2]==other and self.grid[0][2]=='-':            blockMoves.append(3)        if self.grid[2][2]==self.grid[2][0]==other and self.grid[2][1]=='-':            blockMoves.append(8)        if self.grid[2][2]==self.grid[0][2]==other and self.grid[1][2]=='-':            blockMoves.append(6)        if self.grid[2][2]==self.grid[1][1]==other and self.grid[0][0]=='-':            blockMoves.append(1)        if self.grid[2][2]==self.grid[0][0]==other and self.grid[1][1]=='-':            blockMoves.append(5)                if winMoves:            self.chooseMove(user,winMoves[randrange(len(winMoves))])        elif blockMoves:            self.chooseMove(user,blockMoves[randrange(len(blockMoves))])        else:            while True:                i=randrange(3)                k=randrange(3)                if self.grid[i][k]=='-':                    self.grid[i][k]=user                    break    def chooseMove(self,user,move):        if move==1:            self.grid[0][0]=user        elif move==2:            self.grid[0][1]=user        elif move==3:            self.grid[0][2]=user        elif move==4:            self.grid[1][0]=user        elif move==5:            self.grid[1][1]=user        elif move==6:            self.grid[1][2]=user        elif move==7:            self.grid[2][0]=user        elif move==8:            self.grid[2][1]=user        elif move==9:            self.grid[2][2]=user            def winlose(self,user):        if ((self.grid[0][0]==self.grid[0][2]==self.grid[0][1]==user) or            (self.grid[1][0]==self.grid[1][2]==self.grid[1][1]==user) or            (self.grid[2][0]==self.grid[2][2]==self.grid[2][1]==user) or            (self.grid[0][0]==self.grid[2][0]==self.grid[1][0]==user) or            (self.grid[0][1]==self.grid[2][1]==self.grid[1][1]==user) or            (self.grid[0][2]==self.grid[2][2]==self.grid[1][2]==user) or            (self.grid[0][0]==self.grid[2][2]==self.grid[1][1]==user) or            (self.grid[0][2]==self.grid[2][0]==self.grid[1][1]==user)):            return True        def userGo(self,user):        while True:            x=int(input('Horizontal Row:'))-1            while x!=0 and x!=1 and x!=2:                self.error()                x=int(input('Horizontal Row:'))-1            y=int(input('Vertical Column:'))-1            while y!=0 and y!=1 and y!=2:                self.error()                y=int(input('Vertical Column:'))-1            if self.grid[x][y]=='-':                self.grid[x][y]=user                break            else:                print('Sorry, that space is already taken.')    def catsgame(self):        openSpaces=0        for i in range(3):            for k in range(3):                if self.grid[i][k]=='-':                    openSpaces+=1        if not openSpaces:            return True            def xyChoose(self):        inp=raw_input("Do you want to be X or O (X goes first)?").upper()        while inp!='X' and inp!='O':            self.error()            inp=raw_input("Do you want to be X or O?").upper()        if inp=='X':            self.player='X'            self.computer='O'        elif inp=='O':            self.player='O'            self.computer='X'    def playerLoop(self,mode,user):        if mode==0:            print('Player\'s Turn:')        if mode==1:            print('X\'s Turn:')        if mode==2:            print('O\'s Turn:')        while True:            try:                self.userGo(user)                break            except ValueError:                self.error()        self.printGrid()        if self.winlose(user):            return True    def compLoop(self,user):        print('Computer\'s Turn:')        self.compAssess(user)        self.printGrid()        if self.winlose(user):            return True    def pveLoop(self):        self.newGrid()        self.xyChoose()        if self.player=='X':            self.printGrid()            while True:                if self.playerLoop(0,'X'):                    print('Player Wins!')                    break                if self.catsgame():                    print('It\'s a Cat\'s Game!')                    break                if self.compLoop('O'):                    print('Computer Wins!')                    break                if self.catsgame():                    print('It\'s a Cat\'s Game!')                    break                        elif self.computer=='X':            while True:                if self.compLoop('X'):                    print('Computer Wins!')                    break                if self.catsgame():                    print('It\'s a Cat\'s Game!')                    break                if self.playerLoop(0,'O'):                    print('Player Wins!')                    break                if self.catsgame():                    print('It\'s a Cat\'s Game!')                    break    def pvpLoop(self):        self.newGrid()        self.printGrid()        while True:            if self.playerLoop(1,'X'):                print('X Wins!')                break            if self.catsgame():                print('It\'s a Cat\'s Game!')                break            if self.playerLoop(2,'O'):                print('O Wins!')                break            if self.catsgame():                print('It\'s a Cat\'s Game!')                break    def playAgain(self):        while True:            inp=raw_input('Would you like to play again? (y/n)').lower()            if inp=='y':                return True                break            elif inp=='n':                break            else:                self.error()    def gameLoop(self):        if self.playercomp():            self.pveLoop()        else:            self.pvpLoop()if __name__=='__main__':    game=tictactoe()